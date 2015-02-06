Summary:	Tool to gather NetBIOS info from Windows networks
Name:		nbtscan
Version:	1.5.1
Release:	6
Group:		Networking/Other
License:	GPL
URL:		http://www.inetcat.net/software/nbtscan.html
Source0:	http://www.inetcat.net/software/%{name}-%{version}.tar.gz
#add $DESTDIR to make install
Patch0:		nbtscan-1.5.1-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
NBTscan is a program for scanning IP networks for NetBIOS name information.
It sends a NetBIOS status query to each address in supplied range and lists
received information in human readable form.

%prep

%setup -qn %{name}-%{version}a
%patch0 -p1

%build

%configure2_5x

%make


%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_bindir}/*


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-5mdv2011.0
+ Revision: 620479
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5.1-4mdv2010.0
+ Revision: 430157
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.5.1-3mdv2009.0
+ Revision: 253651
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.5.1-1mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdv2008.0
+ Revision: 81497
- Import nbtscan



* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-1mdv2008.0
- initial Mandriva package (fedora import)
