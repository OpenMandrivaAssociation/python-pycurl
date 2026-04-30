%define module pycurl
%bcond tests 1

Name:		python-pycurl
Summary:	A Python interface to libcurl
Version:	7.46.0
Release:	1
License:	LGPL-2.1-or-later OR MIT
Group:		Development/Python
URL:		https://pycurl.io
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Upstream repo: https://github.com/pycurl/pycurl

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

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info
chmod a-x examples/*py

%build -p
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%install -a
# Remove files installed into wrong location
rm -rf %{buildroot}%{_docdir}/pycurl

%check
export PYTHONPATH=%{buildroot}%{python_sitearch}
%__python -c 'import %{module}; print(%{module}.version)'

%files
%doc README.rst examples doc/*.rst
%{python_sitearch}/curl
%{python_sitearch}/%{module}.*.so
%{python_sitearch}/%{module}-%{version}.dist-info
