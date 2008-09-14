%define module curl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.19.0
Release:	%mkrel 1
Group:		Development/Python
License:	LGPLv2+
URL:		http://pycurl.sourceforge.net
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  curl-devel >= 7.16.0
%py_requires -d
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%setup -qn pycurl-%{version}
chmod a-x examples/*

%build
env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" %{__python} setup.py build

%check
%{__python} tests/test_internals.py -q

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README TODO examples doc tests
%{python_sitearch}/*
