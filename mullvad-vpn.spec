Name:           mullvad-vpn
Version:        2020.3.0
Release:        1%{?dist}_ostree
Summary:        Mullvad VPN client

License:        GPL-3.0
URL:            https://github.com/mullvad/mullvadvpn-app#readme
Source0:        https://github.com/mullvad/mullvadvpn-app/releases/download/2020.3/MullvadVPN-2020.3_x86_64.rpm

BuildArch:      x86_64
BuildRequires:  
Requires:       libXScrnSaver libnotify libnsl

%description
Mullvad VPN clinet. This is repackaged from the official Mullvad RPM release to
be compatible with OSTree based Fedora distributions.


%prep
rpm2archive < %{SOURCE0} | tar -xzvvf -


%build


%install
mv 'usr' %{buildroot}/%{_prefix}
mv 'opt/Mullvad VPN' %{buildroot}/%{_datarootdir}/mullvad-vpn
mkdir -p %{buildroot}/var/log/mullvad-vpn
mkdir -p %{buildroot}/var/cache/mullvad-vpn


%files
exit 1


%changelog
* Sun Mar 29 2020 Initial version
