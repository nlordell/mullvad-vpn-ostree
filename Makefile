.PHONY: submodules
submodules:
	git submodule update --init
	git -C mullvadvpn-app submodule update --init dist-assets/binaries
