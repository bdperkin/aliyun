%bcond_with check

# https://github.com/aliyun/credentials-go
%global goipath         github.com/aliyun/credentials-go
Version:                0.0.1

%gometa

%global common_description %{expand:
Alibaba Cloud Credentials for Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud Credentials for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(github.com/alibabacloud-go/tea/tea)
BuildRequires:  golang(gopkg.in/ini.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Mar 04 16:40:57 EST 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.1-1
- Enable check stage
- Update to version 0.0.1
- Add golang(github.com/alibabacloud-go/tea/tea) BuildRequires

* Fri Nov 22 16:07:30 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122gitc03d72d
- Initial package

