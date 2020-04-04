spec ?= "mullvad-vpn-ostree.spec"

srpm:
	dnf install -y rpkg rpmdevtools
	mkdir -p target/ $(outdir)
	spectool -g --directory target/ $(spec)
	rpkg srpm --outdir target/ --spec $(spec)
	[ -z "$(outdir)" ] || mv target/*.src.rpm $(outdir)
