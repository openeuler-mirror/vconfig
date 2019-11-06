Name:       	vconfig
Version:    	1.9
Release:    	26
Summary:    	802.1Q VLAN implementation for Linux
License:    	GPLv2+

URL:        	https://www.candelatech.com/~greear/vlan.html
Source0:     	https://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz

Patch0:     	%{name}-1.9-Pass-compilation-with-Werror-format-security.patch
BuildRequires:  coreutils gcc make

%description 
The %{name} program allows you to create and remove vlan-devices on a vlan
enabled kernel. Vlan-devices are virtual ethernet devices which represents
the virtual lans on the physical lan.

%package_help

%prep
%autosetup -n vlan -p1

%build
make clean
rm -f %{name}
make CCFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" STRIP=/bin/true %{name}

%install
install -D -m755 %{name} %{buildroot}%{_sbindir}/%{name}
install -D -m644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%defattr(-,root,root)
%{_sbindir}/%{name}

%files help
%defattr(-,root,root)
%doc CHANGELOG README vlan.html vlan_test.pl
%{_mandir}/man8/%{name}.8.gz

%changelog
* Fri Oct 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.9-26
- Package init
