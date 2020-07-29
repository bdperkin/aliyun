%bcond_with check

%global _hardened_build 1

# https://github.com/aliyun/aliyun-cli
%global goipath         github.com/aliyun/aliyun-cli
Version:                3.0.54

# https://github.com/aliyun/aliyun-openapi-meta
%global gometarepo      aliyun-openapi-meta
%global gometaipath     github.com/aliyun/%{gometarepo}
%global metacommit      73a3ade39a109bda00ae3a80585fac98b3f3dd70
%global gometaname      golang-github-%{gometarepo}
%global gometaversion   0
%global gometarelease   0.1%{?dist}
%global gometasummary   Aliyun OpenAPI Meta Data
%global gometaurl       https://%{gometaipath}
%global gometadir       %{gometarepo}-%{metacommit}
%global gometasource    %{gometadir}.tar.gz

%gometa

%global common_description %{expand:
Alibaba Cloud CLI.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md bin/README.md\\\
                        cli/README.md oss/README-CN.md oss/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud CLI

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gometasource}

BuildRequires:  go-bindata
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/endpoints)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/ecs)
BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/aliyun/credentials-go/credentials)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/jmespath/go-jmespath)
BuildRequires:  golang(github.com/posener/complete)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  help2man
BuildRequires:  gzip

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%setup -D -T -b 1 -n %{gometadir} -q
%goprep
cd %{gobuilddir}/src/%{goipath}
%define gometaabs       %{_builddir}/%{gometadir}
go-bindata -o resource/metas.go -pkg resource -prefix %{gometaabs} %{gometaabs}/...

%build
LDFLAGS="-X '%{goipath}/cli.Version=%{version}'" 
%gobuild -o %{gobuilddir}/bin/aliyun %{goipath}/main
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/aliyun.1 -N --version-string="%{version}" %{gobuilddir}/bin/aliyun
gzip %{gobuilddir}/share/man/man1/aliyun.1

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/
for dir in bin cli oss; do
  install -m 0755 -vd                   %{buildroot}%{_pkgdocdir}/$dir
done
for doc in %{godocs}; do
  install -m 0644 -vp %{gobuilddir}/src/%{goipath}/$doc %{buildroot}%{_pkgdocdir}/$doc
done

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc %{_pkgdocdir}/*
%{_mandir}/man1/aliyun.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-1
- Update to version 3.0.54 (#1811183)
- Explicitly harden package
- Update to aliyun-openapi-meta to commit
  73a3ade39a109bda00ae3a80585fac98b3f3dd70
- Remove golang(github.com/satori/go.uuid)
  (commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b) BuildRequires
- Fix man page generation
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-2
- Add man page

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-1
- Update to aliyun-cli to version 3.0.36
- Update to aliyun-openapi-meta to commit
  3e9d6a741c5029c92f6447e4137a6531f037a931

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 3.0.30-1
- Initial package

