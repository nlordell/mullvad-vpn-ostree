srpm:
	dnf install -y rpmdevtools
	spectool -g -R ${spec}
	rpmbuild -bs ${spec}
	cp ~/rpmbuild/SRPMS/* ${outdir}
