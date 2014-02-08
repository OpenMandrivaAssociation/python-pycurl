%define module curl

Summary:	A Python interface to libcurl
Name:		python-%{module}
Version:	7.19.0
Release:	11
Group:		Development/Python
License:	LGPLv2+
URL:		http://pycurl.sourceforge.net
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
# Ugly hack to get libs necessary to compile libcurl 
#   but avoid linking with libcurl.a
Patch0:		pycurl-7.19.0-no-static-libcurl.patch
Patch1:		python-curl-fix-do_curl_reset-refcount.patch
Patch2:		pycurl-7.19.0-link.patch
BuildRequires:  python-devel
BuildRequires:  curl-devel >= 7.19.0
%py_requires -d
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	python-pycurl < %{version}-%{release}
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
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot} --optimize=2
rm -rf %{buildroot}%{_datadir}/doc/pycurl
 
%files
%defattr(-,root,root)
%doc COPYING ChangeLog README TODO examples doc tests
%{python_sitearch}/*


%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 7.19.0-7mdv2011.0
+ Revision: 667927
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 7.19.0-6mdv2011.0
+ Revision: 589994
- rebuild for python 2.7

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 7.19.0-5mdv2010.1
+ Revision: 533669
- rebuild for openssl 1.0

* Sun Oct 11 2009 Funda Wang <fwang@mandriva.org> 7.19.0-4mdv2010.0
+ Revision: 456652
- provides python-pycurl

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 7.19.0-3mdv2010.0
+ Revision: 442090
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 7.19.0-2mdv2009.1
+ Revision: 319516
- rebuild with python 2.6

* Sun Sep 14 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 7.19.0-1mdv2009.0
+ Revision: 284779
- new release

* Wed Sep 10 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 7.18.2-1mdv2009.0
+ Revision: 283580
- new release

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 7.16.4-5mdv2009.0
+ Revision: 259529
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 7.16.4-4mdv2009.0
+ Revision: 247398
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 7.16.4-2mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 7.16.4-2mdv2008.0
+ Revision: 85589
- rework spec file
  add checks
  tune up CFLAGS

  + Götz Waschk <waschk@mandriva.org>
    - fix license

* Thu Sep 06 2007 Götz Waschk <waschk@mandriva.org> 7.16.4-1mdv2008.0
+ Revision: 80680
- new version
- update license tag


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 7.15.5.1-1.20061108.1mdv2007.0
+ Revision: 88787
- Import python-curl

* Wed Nov 29 2006 G�tz Waschk <waschk@mandriva.org> 7.15.5.1-1.20061108.1mdv2007.1
- cvs snapshot

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 7.13.2-2mdk
- BuildRequires : need recent curl

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 7.13.2-1mdk
- 7.13.2

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 7.12.2-2mdk
- Rebuild for new python

* Tue Nov 23 2004 G�tz Waschk <waschk@linux-mandrake.com> 7.12.2-1mdk
- initial package

