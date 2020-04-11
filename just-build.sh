#!/bin/bash

MYDIR=$PWD

START_TS=`date`

rm -rf /home/rolson/rpmbuild
mkdir -p /home/rolson/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/cobol-lang.spec /home/rolson/rpmbuild/SPECS

pushd /home/rolson/rpmbuild/SPECS
spectool -g -R ./cobol-lang.spec
# Get the dependencies
dnf builddep -y ./cobol-lang.spec
# Now do the actual build
rpmbuild -ba ./cobol-lang.spec 2>&1 | tee $MYDIR/build-output.txt
popd

echo Started:_____$START_TS
echo Ended:_______`date`
