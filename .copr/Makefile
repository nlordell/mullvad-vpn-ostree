spec ?= "mullvad-vpn-ostree.spec"
outdir ?= "target"

srpm:
	dnf install -y rpkg rpmdevtools
	mkdir -p ${outdir}
	spectool -g --directory ${outdir} ${spec}
	rpkg srpm --outdir ${outdir} --spec ${spec}
