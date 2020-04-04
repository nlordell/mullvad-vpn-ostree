[![Copr build status](https://copr.fedorainfracloud.org/coprs/nlordell/mullvad-vpn-ostree/package/mullvad-vpn-ostree/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/nlordell/mullvad-vpn-ostree/package/mullvad-vpn-ostree/)

# Mullvad VPN OSTree Compatible RPM

This repository contains a hacky RPM spec file and COPR makefile for repackaging
the official Mullvad VPN binary RPM release into something that is compatible
with OSTree-based Fedora distributions (specifically Silverblue).

**:warning: Disclaimer: this project is in no way affiliated with Mullvad VPN
and is simply the workaround that I used to get the daemon working on
Silverblue, use without warranty at your own risk! :warning:**

## Installation

The RPM is built and distributed over COPR, follow the link at the top of the
README and either download the RPM from the latest build or add the COPR
repository and install with `rpm-ostree` normally.

## How It Works?

The official RPM packages installs all the binaries to `/opt` which
unfortunately is not well supported on Silverblue. In fact, files installed to
`/opt` get installed to `/usr/lib/opt` instead. This leads to the daemon
having a SELinux file context type of `lib_t` instead of the usual `usr_t` that
is expected for things installed to the `/opt` dir, like on Fedora Workstation
installations. Executables run by `systemd` with the `lib_t` context type have
more restrictive permissions, causing access issues at runtime.

This RPM spec just repackages the Mullvad VPN app installation into `/usr/share`
so that it has has the `usr_t` file context type. This is a hacky workaround as
binaries and libraries is not what `/usr/share` is for.

## Long Term Solution

As previously mentioned, this workaround is a bit hacky, and the more correct
long-term solution would be to:
1. Write an actual SELinux policy for the daemon and supporting executables
2. Build the RPM from source
3. Try to adhere to the Linux Filesystem Hierarchy Standard as much as possible
4. :crossed_fingers: Try and incorperate this upstream, as I believe this would
   be beneficial to standard Fedora Workstation installations, specifically
   regarding the added security of having a SELinux policy as `usr_t` type
   executables run in an unrestricted context which should not be needed.

## Using the Official RPM

In order to use the official RPM, a few extra things need to be done. First,
**before the installation** is to set up an SELinux equivalency rule for `/opt`
and the Mullvad VPN installation destination:
```
sudo semanage fcontext -a -e /opt '/usr/lib/opt/Mullvad.VPN'
```

Then the official RPM can be installed normally:
```
rpm-ostree install mullvad-vpn-*.rpm
systemctl reboot
```

Then symbolic link in `/opt` to the installation can be created, this us usally
done automatically but there is a small bug because of the space in the path:
```
sudo ln -s '/usr/lib/opt/Mullvad VPN' '/opt/Mullvad VPN'
```

And finally, the `systemd` unit needs to be manually enabled and either reboot
the system so that it gets started during init, or start it manually (this only
needs to be done once):
```
systemctl enable '/opt/Mullvad VPN/resources/mullvad-daemon.service'
systemctl start mullvad-daemon.service
```

## Building Locally

In order to build the RPM locally, simply:

```
dnf install rpmdevtools
rpmdev-setuptree
spectool -g -R mullvad-vpn.spec
rpmbuild -bb mullvad-vpn.spec
```
