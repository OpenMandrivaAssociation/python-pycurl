%define module curl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.19.5
Release:	1
Group:		Development/Python
License:	LGPLv2+
Url:		http://pycurl.sourceforge.net
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
Patch2:		pycurl-7.19.5-link.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(python3)
Provides:	python-pycurl = %{version}-%{release}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%setup -qn pycurl-%{version}
chmod a-x examples/*py
%apply_patches

%build
env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" python setup.py build

%check
export PYTHONPATH=%{buildroot}%{py_platsitedir}
python -c 'import py%{module}; print(py%{module}.version)'

%install
python setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
 
%files
%doc COPYING-LGPL COPYING-MIT ChangeLog README.rst examples doc
%{py_platsitedir}/*

