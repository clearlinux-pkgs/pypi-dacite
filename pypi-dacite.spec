#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dacite
Version  : 1.6.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/f9/bf/3f0912b4cfd861cd0fb7278c2b8d5bfb0c613ec1b7922e25e4115287b73a/dacite-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/bf/3f0912b4cfd861cd0fb7278c2b8d5bfb0c613ec1b7922e25e4115287b73a/dacite-1.6.0.tar.gz
Summary  : Simple creation of data classes from dictionaries.
Group    : Development/Tools
License  : MIT
Requires: pypi-dacite-python = %{version}-%{release}
Requires: pypi-dacite-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# dacite
[![Build Status](https://travis-ci.org/konradhalas/dacite.svg?branch=master)](https://travis-ci.org/konradhalas/dacite)
[![Coverage Status](https://coveralls.io/repos/github/konradhalas/dacite/badge.svg?branch=master)](https://coveralls.io/github/konradhalas/dacite?branch=master)
[![License](https://img.shields.io/pypi/l/dacite.svg)](https://pypi.python.org/pypi/dacite/)
[![Version](https://img.shields.io/pypi/v/dacite.svg)](https://pypi.python.org/pypi/dacite/)
[![Python versions](https://img.shields.io/pypi/pyversions/dacite.svg)](https://pypi.python.org/pypi/dacite/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package python
Summary: python components for the pypi-dacite package.
Group: Default
Requires: pypi-dacite-python3 = %{version}-%{release}

%description python
python components for the pypi-dacite package.


%package python3
Summary: python3 components for the pypi-dacite package.
Group: Default
Requires: python3-core
Provides: pypi(dacite)

%description python3
python3 components for the pypi-dacite package.


%prep
%setup -q -n dacite-1.6.0
cd %{_builddir}/dacite-1.6.0
pushd ..
cp -a dacite-1.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408681
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
