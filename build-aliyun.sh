#! /bin/bash

export http_proxy=http://localhost:3128

MOCKR="fedora-rawhide-x86_64"

PACKAGES="
alibabacloud-debug
alibabacloud-tea
aliyun-alibaba-cloud-sdk
aliyun-credentials
alyu-configparser
droundy-goopt
aliyun-oss-sdk
aliyun-ossutil
aliyun-cli
"

mock -r ${MOCKR} --clean
if [ $? -ne 0 ]; then
    exit 1
fi

mock -r ${MOCKR} --init
if [ $? -ne 0 ]; then
    exit 1
fi

mkdir -p SRPMS RPMS
if [ $? -ne 0 ]; then
    exit 1
fi

rm -f SRPMS/golang-github-*.src.rpm
if [ $? -ne 0 ]; then
    exit 1
fi

rm -f RPMS/golang-github-*.rpm
if [ $? -ne 0 ]; then
    exit 1
fi

for PKG in ${PACKAGES}; do
    SPEC="SPECS/golang-github-${PKG}.spec"

    mock -r ${MOCKR} --buildsrpm --spec ${SPEC} --sources SOURCES --symlink-dereference
    if [ $? -ne 0 ]; then
        exit 1
    fi

    mv -v /var/lib/mock/*/result/golang-github-${PKG}-*.src.rpm SRPMS
    if [ $? -ne 0 ]; then
        exit 1
    fi
done

mock -r ${MOCKR} --chain --recurse $(ls -trd SRPMS/golang-github-*.src.rpm)
if [ $? -ne 0 ]; then
    exit 1
fi

ls -trd /var/tmp/mock-chain-bperkins-* | tail -1 | xargs -i find {} -type f -name '*.src.rpm' -print | xargs -i mv -v -f {} SRPMS
if [ $? -ne 0 ]; then
    exit 1
fi

ls -trd /var/tmp/mock-chain-bperkins-* | tail -1 | xargs -i find {} -type f -name '*.rpm' -print | xargs -i mv -v -f {} RPMS
if [ $? -ne 0 ]; then
    exit 1
fi
