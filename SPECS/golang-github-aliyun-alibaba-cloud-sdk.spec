%bcond_with check

# https://github.com/aliyun/alibaba-cloud-sdk-go
%global goipath         github.com/aliyun/alibaba-cloud-sdk-go
Version:                1.61.31

%gometa

%global common_description %{expand:
Alibaba Cloud SDK for Go.}

%global golicenses      LICENSE
%global godocs          docs CONTRIBUTING.md ChangeLog.txt README-CN.md\\\
                        README.md tools/document.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud SDK for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jmespath/go-jmespath)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(gopkg.in/ini.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/goji/httpauth)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in tools; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs CONTRIBUTING.md ChangeLog.txt README-CN.md README.md tools/document.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:40:50 EST 2020 Brandon Perkins <bperkins@redhat.com> - 1.61.31-1
- Update to version 1.61.31

* Fri Nov 22 15:35:08 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 1.60.259-1
- Initial package

