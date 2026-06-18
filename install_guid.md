# GEOS Installation Guide — Conda Environment on Ubuntu (No Sudo)

This guide documents how to build GEOS (formerly GEOSX) from source inside a conda environment on Ubuntu 22.04 without sudo access. It includes a clean install recipe and a detailed troubleshooting section covering every issue encountered during the process.

**System tested on:**
- Ubuntu 22.04 (glibc 2.35)
- System GCC 11.4.0
- Conda 23.7.4 (Anaconda)
- No sudo/root access

---

## Table of Contents

1. [Clean Install Steps](#clean-install-steps)
2. [Problems Encountered and Solutions](#problems-encountered-and-solutions)

---

## Clean Install Steps

These are the final, working steps incorporating all fixes. Follow these from scratch for a clean build.

### 1. Create and Activate Conda Environment

```bash
conda create -n geos -y
source ~/anaconda3/etc/profile.d/conda.sh
conda activate geos
```

### 2. Install All Dependencies

Install everything upfront to avoid mid-build failures:

```bash
# Core build tools
conda install -y -c conda-forge cmake python git-lfs make

# MPI stack
conda install -y -c conda-forge openmpi openmpi-mpicc openmpi-mpicxx

# Linear algebra
conda install -y -c conda-forge openblas lapack

# Fortran compiler (needed by scotch and superlu_dist)
conda install -y -c conda-forge gfortran

# Parser generators (needed by scotch)
conda install -y -c conda-forge bison flex

# Compression library (needed by GEOS)
conda install -y -c conda-forge zlib

# CRITICAL: Upgrade sysroot to 2.28+ (see Problem #3 below)
conda install -y -c conda-forge "sysroot_linux-64>=2.28"
```

**Important:** Do NOT upgrade sysroot beyond your system's glibc version. If your system has glibc 2.35, sysroot 2.28 is safe. Sysroot 2.39 will cause runtime glibc version mismatches (see Problem #4).

### 3. Fix Conda Sysroot Linker Scripts (CRITICAL)

Conda's sysroot ships with linker scripts written for RHEL/CentOS (`/lib64/` paths). On Ubuntu, these paths don't exist. The sysroot's own linker handles this via `--sysroot`, but when system tools interact with these scripts, they fail.

**You must restore the original sysroot linker scripts** so they use sysroot-relative paths (which conda's linker resolves correctly):

```bash
SYSROOT=$CONDA_PREFIX/x86_64-conda-linux-gnu/sysroot

# Verify libm.so linker script has /lib64/ paths (sysroot-relative)
cat $SYSROOT/usr/lib64/libm.so
# Should contain: GROUP ( /lib64/libm.so.6  AS_NEEDED ( /usr/lib64/libmvec_nonshared.a /lib64/libmvec.so.1 ) )

# Verify libc.so linker script has /lib64/ paths (sysroot-relative)
cat $SYSROOT/usr/lib64/libc.so
# Should contain: GROUP ( /lib64/libc.so.6 /usr/lib64/libc_nonshared.a  AS_NEEDED ( /lib64/ld-linux-x86-64.so.2 ) )
```

If these files contain Ubuntu-style paths like `/usr/lib/x86_64-linux-gnu/`, revert them to `/lib64/` paths. The sysroot has the actual `.so.6` files in `$SYSROOT/lib64/`, so these relative paths are correct when conda's linker uses `--sysroot`.

### 4. Set Up Directory Structure and Clone Repositories

```bash
mkdir -p ~/codes && cd ~/codes

# Clone GEOS
git clone https://github.com/GEOS-DEV/GEOS.git
cd GEOS
git lfs install
git submodule init
git submodule update
cd ..

# Clone thirdPartyLibs
git clone https://github.com/GEOS-DEV/thirdPartyLibs.git
cd thirdPartyLibs
git lfs install
git lfs pull
git submodule init
git submodule update
cd ..
```

### 5. Create the Host Configuration File

Create `~/codes/GEOS/host-configs/conda-geos.cmake`:

```cmake
set( CONFIG_NAME "conda-geos" )

# Compilers - use conda's GCC toolchain consistently
set(CMAKE_C_COMPILER "$ENV{CONDA_PREFIX}/bin/x86_64-conda-linux-gnu-gcc" CACHE PATH "")
set(CMAKE_CXX_COMPILER "$ENV{CONDA_PREFIX}/bin/x86_64-conda-linux-gnu-g++" CACHE PATH "")
set(ENABLE_FORTRAN ON CACHE BOOL "" FORCE)
set(CMAKE_Fortran_COMPILER "$ENV{CONDA_PREFIX}/bin/gfortran" CACHE PATH "")

# MPI
set(ENABLE_MPI ON CACHE PATH "")
set(MPI_C_COMPILER "$ENV{CONDA_PREFIX}/bin/mpicc" CACHE PATH "")
set(MPI_CXX_COMPILER "$ENV{CONDA_PREFIX}/bin/mpicxx" CACHE PATH "")
set(MPIEXEC "$ENV{CONDA_PREFIX}/bin/mpirun" CACHE PATH "")

# BLAS and LAPACK
set( BLAS_LIBRARIES "$ENV{CONDA_PREFIX}/lib/libopenblas.so" CACHE PATH "" FORCE )
set( LAPACK_LIBRARIES "$ENV{CONDA_PREFIX}/lib/liblapack.so" CACHE PATH "" FORCE )

# CUDA and OpenMP
set( ENABLE_CUDA OFF CACHE PATH "" FORCE )
set( ENABLE_OPENMP OFF CACHE PATH "" FORCE )

# TPLs
set( ENABLE_TRILINOS OFF CACHE PATH "" FORCE )
set( ENABLE_CALIPER OFF CACHE PATH "" FORCE )
set( ENABLE_DOXYGEN OFF CACHE BOOL "" FORCE)
set( ENABLE_MATHPRESSO OFF CACHE BOOL "" FORCE )

if(NOT ( EXISTS "${GEOS_TPL_DIR}" AND IS_DIRECTORY "${GEOS_TPL_DIR}" ) )
   set(GEOS_TPL_DIR "${CMAKE_SOURCE_DIR}/../../thirdPartyLibs/install-${CONFIG_NAME}-release" CACHE PATH "" FORCE )
endif()

include(${CMAKE_CURRENT_LIST_DIR}/tpls.cmake)
```

> **Note:** Replace `$ENV{CONDA_PREFIX}` with the actual absolute path (e.g., `/home/username/anaconda3/envs/geos`) if cmake doesn't resolve it at configure time.

### 6. Patch thirdPartyLibs for Hypre Build Issues

Before building, apply two patches to `~/codes/thirdPartyLibs/CMakeLists.txt`:

**Patch 1 — Fix `ar` flags for hypre (Problem #5):**

Find the hypre configure block (search for `config_hypre_for_geos`) and add `AR` with proper flags:

```cmake
  find_program(HYPRE_AR NAMES x86_64-conda-linux-gnu-ar ar)
  file(WRITE ${PROJECT_BINARY_DIR}/config_hypre_for_geos "\
  ./configure \
  AR=\"${HYPRE_AR} -rcu\" \
  CC=${HYPRE_C_COMPILER} \
  ...
```

**Patch 2 — Disable Fortran for hypre (Problem #6):**

In the same configure block, remove the `FC` and `FCFLAGS` lines and add `--disable-fortran`:

```cmake
  # Remove these two lines:
  # FC=${HYPRE_Fortran_COMPILER} \
  # FCFLAGS=\"${HYPRE_Fortran_FLAGS}\" \
  
  # Add this line instead:
  --disable-fortran \
```

### 7. Build Third-Party Libraries

```bash
cd ~/codes/thirdPartyLibs
python scripts/config-build.py -hc ../GEOS/host-configs/conda-geos.cmake -bt Release
cd build-conda-geos-release
make -j$(nproc)
```

This takes 30-60+ minutes depending on your system.

### 8. Build GEOS

```bash
cd ~/codes/GEOS
python scripts/config-build.py -hc host-configs/conda-geos.cmake -bt Release
cd build-conda-geos-release
make -j$(nproc)
```

> **Note:** You may see an XML validation error at the very end for `function_examples.xml`. This is a schema mismatch in an example file and does not affect the build. The `geosx` binary is fully functional.

### 9. Verify Installation

```bash
./bin/geosx --help
```

### 10. Run a Simulation

```bash
# Single process
./bin/geosx -i ../../inputFiles/singlePhaseFlow/incompressible_1d.xml -o output

# Parallel (4 processes)
mpirun -np 4 ./bin/geosx -i ../../inputFiles/singlePhaseFlow/3D_10x10x10_compressible_smoke.xml -x 2 -y 2 -z 1 -o output
```

---

## Problems Encountered and Solutions

### Problem #1: Missing Bison (scotch build failure)

**Symptom:**
```
CMake Error at src/CMakeLists.txt:84 (message):
  Bison required to compile Scotch and PT-Scotch
```

**Cause:** The scotch graph partitioning library requires the Bison parser generator at build time. It was not installed in the conda environment.

**Fix:**
```bash
conda install -y -c conda-forge bison flex
```

---

### Problem #2: Compiler Toolchain Mismatch (conduit build failure)

**Symptom:**
```
error: 'timespec_get' has not been declared in '::'
```
Hundreds of identical errors from `ctime` header in conduit, and other TPLs.

**Cause:** We initially set `CMAKE_C_COMPILER=/usr/bin/gcc` (system GCC 11.4) but conda's OpenMPI wraps conda's GCC 15.2 (`x86_64-conda-linux-gnu-gcc`). When system GCC 11 includes conda GCC 15's C++ standard library headers, they expect C11 features (`timespec_get`) that the system's glibc headers don't expose in the same way. This is a fundamental mismatch between system compiler and conda's headers.

**Fix:** Use conda's GCC 15 as the C/C++ compiler consistently, so the compiler and its headers match:

```cmake
set(CMAKE_C_COMPILER "/path/to/conda/envs/geos/bin/x86_64-conda-linux-gnu-gcc" CACHE PATH "")
set(CMAKE_CXX_COMPILER "/path/to/conda/envs/geos/bin/x86_64-conda-linux-gnu-g++" CACHE PATH "")
```

**Key lesson:** When using conda's MPI (which wraps conda's GCC), always use conda's GCC as the C/C++ compiler too. Never mix system GCC with conda's MPI.

---

### Problem #3: Ancient Conda Sysroot (timespec_get still missing)

**Symptom:** Same `timespec_get` error even after switching to conda's GCC 15.

**Cause:** Conda installed `sysroot_linux-64` version 2.12 (glibc 2.12), which is extremely old. The `timespec_get` function was added in glibc 2.17 / C11. Conda's GCC 15 headers expected it, but the ancient sysroot didn't have it.

**Fix:**
```bash
conda install -y -c conda-forge "sysroot_linux-64>=2.28"
```

**Warning:** Do not install a sysroot newer than your system's glibc. For example, if your system has glibc 2.35, sysroot 2.39 will produce binaries that require glibc 2.38+ at runtime (see Problem #4).

**How to check your system glibc version:**
```bash
ldd --version | head -1
```

---

### Problem #4: Sysroot Too New — Runtime GLIBC Version Mismatch (VTK failure)

**Symptom:**
```
vtkWrapHierarchy-9.4: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found
```

**Cause:** We upgraded the sysroot to 2.39, but the system only has glibc 2.35. VTK's build tools were compiled and linked against glibc 2.38 headers/stubs from the sysroot. At runtime, these tools couldn't find glibc 2.38 on the system.

**Fix:** Downgrade sysroot to 2.28 — new enough for `timespec_get` (glibc 2.17+) but old enough that binaries run on the system (glibc 2.35):

```bash
conda install -y -c conda-forge "sysroot_linux-64==2.28"
```

**Rule of thumb:** `sysroot version <= system glibc version`. Check system glibc with `ldd --version`.

---

### Problem #5: Hypre `ar` Flag Error

**Symptom:**
```
x86_64-conda-linux-gnu-ar: invalid option -- 'H'
make: *** [Makefile:148: libHYPRE_utilities.a] Error 1
```

**Cause:** Hypre's Makefile invokes `ar` as `${AR} $@ ${OBJS}`, which expands to:
```
x86_64-conda-linux-gnu-ar libHYPRE_utilities.a file1.o file2.o ...
```

Without explicit operation flags (like `-rcu`), `ar` interprets the filename `libHYPRE_utilities.a` as option characters. The `H` in `HYPRE` is not a valid `ar` flag, causing the error.

Hypre's configure auto-detects `AR` from the environment without adding operation flags. System `ar` on some platforms tolerates this; conda's `ar` does not.

**Fix:** Patch `thirdPartyLibs/CMakeLists.txt` to pass `AR` with operation flags to hypre's configure:

```cmake
find_program(HYPRE_AR NAMES x86_64-conda-linux-gnu-ar ar)
# In the config_hypre_for_geos file(WRITE ...) block, add:
AR=\"${HYPRE_AR} -rcu\" \
```

---

### Problem #6: Hypre Fortran/C Linking Failure

**Symptom:**
```
configure: error: linking to Fortran libraries from C fails
```

And deeper in `config.log`:
```
/usr/bin/ld: cannot find /lib64/libm.so.6: No such file or directory
```

**Cause:** This is a complex interaction between three components:

1. **Conda's gfortran** uses conda's linker (`collect2` -> `x86_64-conda-linux-gnu-ld`) which has `--sysroot` support. Inside the sysroot, `/lib64/libm.so.6` exists, so pure Fortran compilation works.

2. **Hypre's configure** runs a Fortran/C interoperability test. It compiles C code with `mpicc` and links it against Fortran libraries (`-lgfortran -lm -lquadmath`).

3. The Fortran libraries pull in `-lm`, which resolves to the sysroot's `libm.so` linker script. This script references `/lib64/libm.so.6` (sysroot-relative path). But hypre's autoconf test somehow invokes the **system linker** (`/usr/bin/ld`) which doesn't use `--sysroot`, so it looks for `/lib64/libm.so.6` literally — which doesn't exist on Ubuntu.

This is fundamentally a mixed-toolchain linker issue that cannot be fixed by setting `LD` or `LIBRARY_PATH` because autoconf runs the link test through `$CC`, and the linker choice is internal to the compiler driver.

**Fix:** Disable Fortran in hypre. GEOS does not need hypre's Fortran bindings:

```cmake
# In thirdPartyLibs/CMakeLists.txt, in the hypre configure block:
# Remove: FC=${HYPRE_Fortran_COMPILER}
# Remove: FCFLAGS="${HYPRE_Fortran_FLAGS}"
# Add:    --disable-fortran
```

---

### Problem #7: Missing zlib (GEOS configure failure)

**Symptom:**
```
Could NOT find ZLIB (missing: ZLIB_LIBRARY) (found version "1.2.11")
```

**Cause:** GEOS requires zlib for compression support. It was not installed in the conda environment.

**Fix:**
```bash
conda install -y -c conda-forge zlib
```

---

### Problem #8: XML Validation Error at End of GEOS Build

**Symptom:**
```
function_examples.xml fails to validate
XML validation failed
make: *** [CMakeFiles/geosx_validate_all_xml_files] Error 1
```

**Cause:** A schema mismatch in one example XML file (`function_examples.xml`). The file uses `SymbolicFunction` but the schema only expects `MultivariableTableFunction` or `TableFunction`.

**Impact:** None. This is a cosmetic issue in an example file. The `geosx` binary is fully built and functional.

**Fix:** No fix needed. Verify the binary works with:
```bash
./build-conda-geos-release/bin/geosx --help
```

---

## Quick Reference: Environment Variables

If you ever need to override MPI compiler wrappers (e.g., to use system GCC instead of conda's GCC):

```bash
export OMPI_CC=/usr/bin/gcc      # Override C compiler inside mpicc
export OMPI_CXX=/usr/bin/g++     # Override C++ compiler inside mpicxx
```

**Warning:** This causes mixed-toolchain issues (see Problems #5 and #6). Only use this if you understand the implications.

---

## Quick Reference: Useful Diagnostic Commands

```bash
# Check compiler versions
gcc --version
x86_64-conda-linux-gnu-gcc --version
mpicc --showme

# Check system glibc version
ldd --version

# Check conda sysroot version
conda list | grep sysroot

# Check if sysroot has timespec_get
grep timespec_get $CONDA_PREFIX/x86_64-conda-linux-gnu/sysroot/usr/include/time.h

# Verify linker scripts (should use /lib64/ paths for sysroot-relative resolution)
cat $CONDA_PREFIX/x86_64-conda-linux-gnu/sysroot/usr/lib64/libm.so
cat $CONDA_PREFIX/x86_64-conda-linux-gnu/sysroot/usr/lib64/libc.so

# Test Fortran compiler works
echo 'program test; print *, "hello"; end program' > /tmp/test.f90
gfortran /tmp/test.f90 -o /tmp/test_f && /tmp/test_f

# Test MPI Fortran works
mpif90 /tmp/test.f90 -o /tmp/test_mpif && /tmp/test_mpif
```
