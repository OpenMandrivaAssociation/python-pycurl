%define module pycurl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.45.1
Release:	1
Group:		Development/Python
License:	LGPLv2+
Url:		http://pycurl.io
Source0:	https://files.pythonhosted.org/packages/source/p/pycurl/pycurl-%{version}.tar.gz
Patch1:		pycurl-7.43.0-link.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(openssl)
%rename	python-curl

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%prep
%autosetup -p1 -n pycurl-%{version}
chmod a-x examples/*py

%build
export CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL"
%py_build

%check
export PYTHONPATH=%{buildroot}%{py_platsitedir}
python -c 'import %{module}; print(%{module}.version)'

%install
python setup.py install --skip-build --root=%{buildroot} --optimize=2
 
%files
%{py_platsitedir}/pycurl*.egg-info
%{py_platsitedir}/pycurl.*.so
%{py_platsitedir}/curl
%doc %{_docdir}/pycurl
