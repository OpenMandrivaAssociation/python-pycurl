%define module pycurl

Summary:	A Python interface to libcurl
Name:		python-pycurl
Version:	7.45.7
Release:	1
Group:		Development/Python
License:	LGPL-2.0-or-later OR MIT
Url:		https://pycurl.io
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
#Patch1:		pycurl-7.43.0-link.patch
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%rename	python-curl

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info
chmod a-x examples/*py

%build
export CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%check
export PYTHONPATH=%{buildroot}%{py_platsitedir}
python -c 'import %{module}; print(%{module}.version)'

%install
%py_install

%files
%doc %{_docdir}/pycurl
%doc README.rst
%license COPYING-MIT COPYING-LGPL
%{python_sitearch}/%{module}-%{version}.dist-info
%{python_sitearch}/%{module}.*.so
%{python_sitearch}/curl
