Summary: Kernel dropped packet monitor 
Name: dropwatch 
Version: 1.4
Release: 16%{?dist} 
Source0: https://fedorahosted.org/releases/d/r/dropwatch/dropwatch-%{version}.tbz2
URL: http://fedorahosted.org/dropwatch
License: GPLv2+ 
Group: Applications/System 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: kernel-devel, readline-devel
BuildRequires: binutils-devel, binutils-static libnl3-devel pkgconfig
Requires: libnl3, readline

Patch0: convert-a-to-m-in-scanf-line.patch
Patch1: printf-format-fix.patch

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
cd src
export CFLAGS=$RPM_OPT_FLAGS
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0755 src/dropwatch $RPM_BUILD_ROOT%{_bindir}
install -m0644 doc/dropwatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc README
%doc COPYING

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Neil Horman <nhorman@redhat.com> - 1.4-15
- fix build error (bz 1412926)

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4-14
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Neil Horman <nhorman@redhat.com> - 1.4-12
- Fixed FTBFS issue (bz 1239436)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 29 2013 Neil Horman <nhorman@redhat.com> - 1.4-8
- Updating spec file

* Fri Nov 29 2013 Neil Horman <nhorman@redhat.com> - 1.4-7
- Drop libnl-devel BuildRequire (bz 1035791)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Dan Horák <dan@danny.cz> - 1.4-4
- rebuilt again for fixed soname in libnl3

* Fri Jan 18 2013 Neil Horman <nhorman@redhat.com> - 1.4-3
- rebuilt to pull in new libnl3 dependencies

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Neil Horman <nhorman@redhat.com> - 1.4-1
- Update to latest upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Neil Horman <nhorman@redhat.com> - 1.2
- Update to latest upstream

* Thu Apr 08 2010 Neil Horman <nhorman@redhat.com> - 1.1-2
- Adding more missing buildrequires

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 1.1-1
- Add missing buildrequires

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 1.1-0
- Move to latest upstream sources

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 20 2009 Neil Horman <nhorman@redhat.com> 1.0-2
- Fixed up Errors found in package review (bz 491240)

* Tue Mar 17 2009 Neil Horman <nhorman@redhat.com> 1.0-1
- Initial build

