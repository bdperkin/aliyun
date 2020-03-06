%bcond_with check

# https://github.com/aliyun/aliyun-cli
%global goipath         github.com/aliyun/aliyun-cli
Version:                3.0.36

# https://github.com/aliyun/aliyun-openapi-meta
%global gometarepo      aliyun-openapi-meta
%global gometaipath     github.com/aliyun/%{gometarepo}
%global metacommit      3e9d6a741c5029c92f6447e4137a6531f037a931
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
BuildRequires:  golang(github.com/satori/go.uuid)(commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(gopkg.in/ini.v1)
BuildRequires:  golang(gopkg.in/yaml.v2)

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

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
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
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:40:55 EST 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.36-1
- Update to aliyun-cli to version 3.0.36
- Update to aliyun-openapi-meta to commit
  3e9d6a741c5029c92f6447e4137a6531f037a931

* Fri Nov 22 15:32:08 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 3.0.30-1
- Initial package

