%define module curl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.43.0
Release:	1
Group:		Development/Python
License:	LGPLv2+
Url:		http://pycurl.sourceforge.net
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
Patch2:		pycurl-7.19.5-link.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python)
Provides:	python-pycurl = %{version}-%{release}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%package -n python2-curl
Summary:        A Python interface to libcurl
Group:          Development/Python
License:        LGPLv2+

%description -n python2-curl
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features

%prep
%setup -qc
mv pycurl-%{version} python2
pushd python2

chmod a-x examples/*py
%apply_patches

popd

cp -a python2 python3

%build
pushd python2

env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" python2 setup.py build
popd

pushd python3
env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" python3 setup.py build

%check
export PYTHONPATH=%{buildroot}%{py_platsitedir}
python -c 'import py%{module}; print(py%{module}.version)'

%install

pushd python2
python2 setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
popd

pushd python3
python setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
 
%files
%doc python2/COPYING-LGPL python2/COPYING-MIT python2/ChangeLog python2/README.rst python2/examples python2/doc
%{py_platsitedir}/*

%files -n python2-curl
%doc python2/COPYING-LGPL python2/COPYING-MIT python2/ChangeLog python2/README.rst python2/examples python2/doc
%{py2_platsitedir}/

