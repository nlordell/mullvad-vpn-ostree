srpm:
	dnf install -y rpmdevtools
	spectool -g -R ${spec_path}
	rpmbuild -bs ${spec_path}
	cp ~/rpmbuild/SRPMS/* ${outdir}
