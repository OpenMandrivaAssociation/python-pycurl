%define module curl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.19.0
Release:	15
Group:		Development/Python
License:	LGPLv2+
Url:		http://pycurl.sourceforge.net
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
# Ugly hack to get libs necessary to compile libcurl 
#   but avoid linking with libcurl.a
Patch0:		pycurl-7.19.0-no-static-libcurl.patch
Patch1:		python-curl-fix-do_curl_reset-refcount.patch
Patch2:		pycurl-7.19.0-link.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(python)
Provides:	python-pycurl = %{version}-%{release}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%setup -qn pycurl-%{version}
chmod a-x examples/*
%apply_patches

%build
env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" %{__python} setup.py build

%check
%{__python} tests/test_internals.py -q

%install
%{__python} setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
 
%files
%doc COPYING ChangeLog README TODO examples doc tests
%{python_sitearch}/*

