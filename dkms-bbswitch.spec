Name:		dkms-bbswitch
Summary:	bbswitch - Optimus GPU power switcher
Version:	v0.4
Release:	2
Source0:	%{name}-%{version}.tar.gz
URL:		https://github.com/Bumblebee-Project

Group:		System/Kernel and hardware
License:	GPLv3
BuildArch:	noarch

%description
bbswitch is a kernel module which automatically detects
the required ACPI calls for two kinds of Optimus laptops. 
It has been verified to work with "real" Optimus and 
"legacy" Optimus laptops (at least, that is how I call them).

%prep 
%setup -q

%build

%install
mkdir -p "%{buildroot}%{_usrsrc}/bbswitch-%version"
cp *.c "%{buildroot}%{_usrsrc}/bbswitch-%version"
cp Makefile "%{buildroot}%{_usrsrc}/bbswitch-%version"
sed "s/REPLACE/%{version}/" dkms/dkms.conf > "%{buildroot}%{_usrsrc}/bbswitch-%version/dkms.conf"

%files 
%defattr(0755,root,root)
%{_usrsrc}/bbswitch-%version/*

%post
set -x
dkms --rpm_safe_upgrade add -m bbswitch -v %{version}
dkms --rpm_safe_upgrade build -m bbswitch -v %{version} &&
dkms --rpm_safe_upgrade install -m bbswitch -v %{version}
depmod -a

%preun
dkms remove --binary -m bbswitch -v %{version} --rpm_safe_upgrade --all

%changelog
* Tue Jan 17 2012 Александр Казанцев <kazancas@mandriva.org> v0.4-1
+ Revision: 762030
- imported package dkms-bbswitch


* Mon Jan 16 2012 Jaron Viëtor <thulinma@thulinma.com> v0.4-1mdk
- Initial package
