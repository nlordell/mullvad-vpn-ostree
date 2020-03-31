%define mullvad_ver 2020.3

Name:           mullvad-vpn
Version:        %{mullvad_ver}.0
Release:        1%{?dist}_ostree
Summary:        Mullvad VPN client

License:        GPL-3.0
URL:            https://github.com/mullvad/mullvadvpn-app#readme
Source0:        https://github.com/mullvad/mullvadvpn-app/releases/download/%{mullvad_ver}/MullvadVPN-%{mullvad_ver}_x86_64.rpm
Source1:        https://raw.githubusercontent.com/mullvad/mullvadvpn-app/master/LICENSE.md

BuildArch:      x86_64

AutoReqProv:    no
Requires:       dbus-libs libXScrnSaver libnotify libnsl


%description
Mullvad VPN client. This is repackaged from the official Mullvad RPM release to
be compatible with OSTree based Fedora distributions.


%prep
rpm2archive < %{SOURCE0} | tar -xzvvf -
cp %{SOURCE1} LICENSE.md


%build
mv 'opt/Mullvad VPN' usr/share/mullvad-vpn
mv usr/share/mullvad-vpn/resources/mullvad-daemon.service mullvad-daemon.service
rm usr/bin/mullvad-problem-report
rm usr/share/mullvad-vpn/resources/mullvad-daemon.conf
sed -Ei 's/\/opt\/Mullvad.*?VPN/\/usr\/share\/mullvad-vpn/' mullvad-daemon.service
sed -Ei 's/\/opt\/Mullvad.*?VPN/\/usr\/share\/mullvad-vpn/' usr/share/applications/mullvad-vpn.desktop


%install
mv 'usr' %{buildroot}/%{_prefix}
install -m 0644 -D -t %{buildroot}/%{_unitdir} mullvad-daemon.service
ln -sr %{buildroot}/%{_datadir}/mullvad-vpn/resources/mullvad-problem-report %{buildroot}/%{_bindir}/mullvad-problem-report
ln -sr %{buildroot}/%{_datadir}/mullvad-vpn/mullvad-vpn %{buildroot}/%{_bindir}/mullvad-vpn
mkdir -p %{buildroot}/var/cache/mullvad-vpn
mkdir -p %{buildroot}/var/log/mullvad-vpn


%post
%systemd_post mullvad-daemon.service

%preun
%systemd_preun mullvad-daemon.service

%postun
%systemd_postun mullvad-daemon.service


%files
%license LICENSE.md
%dir /var/cache/mullvad-vpn
%dir /var/log/mullvad-vpn
%{_bindir}/mullvad
%{_bindir}/mullvad-problem-report
%{_bindir}/mullvad-vpn
%{_datadir}/applications/mullvad-vpn.desktop
%{_datadir}/icons/hicolor/16x16/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/32x32/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/48x48/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/64x64/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/128x128/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/256x256/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/512x512/apps/mullvad-vpn.png
%{_datadir}/icons/hicolor/1024x1024/apps/mullvad-vpn.png
%{_datadir}/mullvad-vpn/*
%{_unitdir}/mullvad-daemon.service


%changelog
* Sun Mar 29 2020 Initial version
-
