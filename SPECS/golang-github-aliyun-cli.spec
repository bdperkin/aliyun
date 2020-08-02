%bcond_without check

%global _hardened_build 1

# https://github.com/aliyun/aliyun-cli
%global goipath0        github.com/aliyun/aliyun-cli
Version:                3.0.55

# https://github.com/aliyun/aliyun-openapi-meta
%global goipath1        github.com/aliyun/aliyun-openapi-meta
%global version1        0
%global commit1         fb1de10319cf130af8945963ef6659707b5f04b7
%global gometarepo      aliyun-openapi-meta
%global gometadir       %{gometarepo}-%{commit1}

%gometa -a

%global _docdir_fmt     %{name}

%global godevelsummary0 Alibaba Cloud (Aliyun) CLI
%global godevelsummary1 Alibaba Cloud (Aliyun) OpenAPI Meta Data

%global common_description %{expand:
Alibaba Cloud (Aliyun) CLI.}

%global golicenses0     LICENSE
%global godocs0         CHANGELOG.md README-CN.md README.md README-bin.md\\\
                        README-cli.md README-CN-oss.md README-oss.md

%global golicenses1     LICENSE
%global godocs1         README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        %{godevelsummary0}

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource0}
Source1:        %{gosource1}

Patch0:         aliyun-cli-credentials-config.patch

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
%goprep -z 1
%goprep -z 0
# https://github.com/aliyun/aliyun-cli/pull/300
%patch0 -p1
mv bin/README.md README-bin.md
mv cli/README.md README-cli.md
mv oss/README.md README-oss.md
mv oss/README-CN.md README-CN-oss.md
pushd %{gobuilddir}/src/%{goipath0}
%global gometaabs       %{_builddir}/%{gometadir}
go-bindata -o resource/metas.go -pkg resource -prefix %{gometaabs} %{gometaabs}/...
popd

%build
LDFLAGS="-X '%{goipath0}/cli.Version=%{version}'" 
%gobuild -o %{gobuilddir}/bin/aliyun %{goipath0}/main
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{godevelsummary0}" -s 1 -o %{gobuilddir}/share/man/man1/aliyun.1 -N --version-string="%{version}" %{gobuilddir}/bin/aliyun

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/
%global buildsubdir %{gometadir}/_build/src/%{goipath0}

%if %{with check}
%check
%gocheck -d 'openapi' -d 'oss/lib'
%endif

%files
%license LICENSE
%doc CHANGELOG.md README-CN.md README.md README-bin.md README-cli.md
%doc README-CN-oss.md README-oss.md
%{_mandir}/man1/aliyun.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-3
- Update summary and description for clarity and consistency

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-2
- Reenable check stage
- Disable 'openapi' tests due to only being used by meta
- Disable 'oss/lib' tests due to need for credentials

* Sat Aug 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.55-1
- Update to version 3.0.55 (#1811183)
- Disable check stage temporarily
- Update to aliyun-openapi-meta to commit
  fb1de10319cf130af8945963ef6659707b5f04b7
- Add godevelsummary, golicenses, and godocs for all sources
- Reorder goprep and patch operations
- Remove goenv before gobuild
- Explicitly set man page summary
- Use standard gopkginstall and gopkgfiles
- Properly generate debugsourcefiles.list

* Fri Jul 31 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-3
- Patch to build against golang-github-aliyun-credentials-1.1.0

* Wed Jul 29 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.54-2
- Enable check stage
- Rename godocs in subdirectories
- Remove explicit gzip of man page
- Change gometaabs from define to global

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

