spec ?= "mullvad-vpn-ostree.spec"
outdir ?= "target"

srpm:
	dnf install -y rpmdevtools
	mkdir -p ${outdir}
	spectool -g ${spec}
	rpkg srpm --spec ${spec} --outdir ${outdir}
