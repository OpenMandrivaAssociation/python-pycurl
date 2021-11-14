%define module pycurl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.44.1
Release:	1
Group:		Development/Python
License:	LGPLv2+
Url:		http://pycurl.io
Source0:	https://files.pythonhosted.org/packages/47/f9/c41d6830f7bd4e70d5726d26f8564538d08ca3a7ac3db98b325f94cdcb7f/pycurl-7.44.1.tar.gz
Patch1:		pycurl-7.43.0-link.patch
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(openssl)
%rename	python-curl

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features.

%package -n python2-%{module}
Summary:        A Python interface to libcurl
Group:          Development/Python
License:        LGPLv2+

%description -n python2-%{module}
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module. PycURL is mature, very fast, and supports a lot
of features

%prep
%setup -qc
mv pycurl-%{version} python2
pushd python2

chmod a-x examples/*py
%autopatch -p1

popd

cp -a python2 python3

%build
pushd python2

env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" python2 setup.py build
popd

pushd python3
env CFLAGS="%{optflags} -DHAVE_CURL_OPENSSL" %py3_build

%check
export PYTHONPATH=%{buildroot}%{py_platsitedir}
python -c 'import %{module}; print(%{module}.version)'

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

%files -n python2-%{module}
%doc python2/COPYING-LGPL python2/COPYING-MIT python2/ChangeLog python2/README.rst python2/examples python2/doc
%{py2_platsitedir}/
