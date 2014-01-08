%define gitdate 20120614
%define oname bbswitch

Name:		dkms-bbswitch
Summary:	bbswitch - Optimus GPU power switcher
Version:	0.4.2
Release:	6
#Source0:	%{name}-%{version}.tar.gz
# source from git repo git://github.com/Bumblebee-Project/bbswitch.git
Source0:	%{oname}_%{gitdate}.tar.xz
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
%setup -qn %{oname}

%build
sed -i 's/#MODULE_VERSION#/%{version}-%{release}/g' dkms/dkms.conf

%install
mkdir -p %{buildroot}%{_usrsrc}/%{oname}-%{version}-%{release}
cp *.c %{buildroot}%{_usrsrc}/%{oname}-%{version}-%{release}
cp Makefile %{buildroot}%{_usrsrc}/%{oname}-%{version}-%{release}
cp dkms/dkms.conf %{buildroot}%{_usrsrc}/%{oname}-%{version}-%{release}/dkms.conf

%files 
%{_usrsrc}/%{oname}-%{version}-%{release}/*

%post
dkms add -m %{oname} -v %{version}-%{release} --rpm_safe_upgrade &&
dkms build -m %{oname} -v %{version}-%{release} --rpm_safe_upgrade &&
dkms install -m %{oname} -v %{version}-%{release} --rpm_safe_upgrade --force
true
/sbin/modprobe %{oname}

%preun
dkms remove --binary -m bbswitch -v %{version}-%{release} --rpm_safe_upgrade --all
