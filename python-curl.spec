%define name python-curl
%define version 7.16.4
%define release %mkrel 1
%define oname pycurl

Summary: PycURL -- cURL library module for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pycurl.sourceforge.net/download/%{oname}-%{version}.tar.gz
License: LGPLv2.1+
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://pycurl.sourceforge.net/
BuildRequires: curl-devel
BuildRequires: curl >= 7.13.2
BuildRequires: python-devel

%description
This module provides Python bindings for the cURL library.

%prep
%setup -q -n %oname-%version

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf %buildroot installed-docs
python setup.py install --root=$RPM_BUILD_ROOT
mv %buildroot%_datadir/doc/pycurl installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc installed-docs/*
%py_platsitedir/curl/
%py_platsitedir/*


