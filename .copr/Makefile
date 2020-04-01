spec ?= "mullvad-vpn-ostree.spec"
outdir ?= "target"

srpm:
	dnf install -y rpmdevtools
	spectool -g -R ${spec}
	rpmbuild -bs ${spec}
	mkdir -p ${outdir}
	cp ~/*build/SRPMS/* ${outdir}
