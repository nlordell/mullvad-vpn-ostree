%define mullvad_ver 2020.5

Name:           mullvad-vpn-ostree
Version:        %{mullvad_ver}.0
Release:        1%{?dist}
Summary:        Mullvad VPN client

License:        GPL-3.0
URL:            https://github.com/mullvad/mullvadvpn-app#readme
Source0:        https://github.com/mullvad/mullvadvpn-app/releases/download/%{mullvad_ver}/MullvadVPN-%{mullvad_ver}_x86_64.rpm
Source1:        https://raw.githubusercontent.com/mullvad/mullvadvpn-app/master/LICENSE.md
Patch0:         mullvad-vpn.patch

AutoReqProv:    no
BuildRequires:  systemd systemd-rpm-macros
Requires:       dbus-libs libXScrnSaver libnotify libnsl
Recommends:     libappindicator-gtk3
Provides:       mullvad-vpn = %{mullvad_ver}.0-1 mullvad-vpn(x86_64) = %{mullvad_ver}.0-1


%description
Mullvad VPN client. This is repackaged from the official Mullvad RPM release to
be compatible with OSTree based Fedora distributions.


%prep
rpm2archive < %{SOURCE0} | tar -xzvvf -
mv 'opt/Mullvad VPN' usr/share/mullvad-vpn
%patch -p1
cp %{SOURCE1} LICENSE.md
mv usr/share/mullvad-vpn/resources/mullvad-daemon.service .
mv usr/local/share/zsh usr/share/zsh
rmdir usr/local/share usr/local


%build


%install
mv 'usr' %{buildroot}/%{_prefix}
install -m 0644 -D -t %{buildroot}/%{_unitdir} mullvad-daemon.service
mkdir -p %{buildroot}/var/cache/mullvad-vpn
mkdir -p %{buildroot}/var/log/mullvad-vpn


%post
%systemd_post mullvad-daemon.service

%preun
%systemd_preun mullvad-daemon.service

%postun
%systemd_postun mullvad-daemon.service


%files
%attr(0444,root,root) %license LICENSE.md
%attr(-,root,root) %dir /var/cache/mullvad-vpn
%attr(-,root,root) %dir /var/log/mullvad-vpn
%attr(-,root,root) %{_bindir}/mullvad
%attr(-,root,root) %{_bindir}/mullvad-exclude
%attr(-,root,root) %{_bindir}/mullvad-problem-report
%attr(-,root,root) %{_bindir}/mullvad-vpn
%attr(-,root,root) %{_datadir}/applications/mullvad-vpn.desktop
%attr(-,root,root) %{_datadir}/bash-completion/completions/mullvad
%attr(-,root,root) %{_datadir}/icons/hicolor/16x16/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/32x32/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/48x48/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/64x64/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/128x128/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/256x256/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/512x512/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/icons/hicolor/1024x1024/apps/mullvad-vpn.png
%attr(-,root,root) %{_datadir}/mullvad-vpn/*
%attr(-,root,root) %{_datadir}/zsh/site-functions/_mullvad
%attr(-,root,root) %{_unitdir}/mullvad-daemon.service


%changelog
* Mon Jun 29 2020 Nicholas Rodrigues Lordello <nlordell@gmail.com> 2020.5.0-1
- Bump to version `2020.5`

* Tue May 12 2020 Nicholas Rodrigues Lordello <nlordell@gmail.com> 2020.4.0-1
- Bump to version `2020.4`

* Sat Apr 04 2020 Nicholas Rodrigues Lordello <nlordell@gmail.com> 2020.3.0-3
- Use a `.patch` file for all modifications to the official release
- Fix `mullvad-vpn` wrapper script not working

* Fri Apr 03 2020 Nicholas Rodrigues Lordello <nlordell@gmail.com> 2020.3.0-2
- Added weak dependency to `libappindicator-gtk3`

* Wed Apr 01 2020 Nicholas Rodrigues Lordello <nlordell@gmail.com> 2020.3.0-1
- Initial repackaging of `mullvad-vpn` RPM pacakge
