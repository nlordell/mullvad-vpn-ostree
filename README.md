## Build Process

```
dnf install rpmdevtools

rpmdev-setuptree
spectool -g -R mullvad-vpn.spec
rpmbuild -bb mullvad-vpn.spec
```
