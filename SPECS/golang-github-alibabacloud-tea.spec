%bcond_with check

# https://github.com/alibabacloud-go/tea
%global goipath         github.com/alibabacloud-go/tea
Version:                0.0.7

%gometa

%global common_description %{expand:
Support for TEA OpenAPI DSL.}

%global golicenses      LICENSE
%global godocs          README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Support for TEA OpenAPI DSL

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(golang.org/x/net/proxy)

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
* Thu Mar 05 11:09:50 EST 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.7-1
- Initial package

