Summary:	Tool to gather NetBIOS info from Windows networks
Name:		nbtscan
Version:	1.5.1
Release:	%mkrel 3
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
