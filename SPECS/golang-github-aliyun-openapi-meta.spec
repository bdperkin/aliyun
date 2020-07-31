%bcond_without check

# https://github.com/aliyun/aliyun-openapi-meta
%global goipath         github.com/aliyun/aliyun-openapi-meta
%global commit          fb1de10319cf130af8945963ef6659707b5f04b7

%gometa

%global common_description %{expand:
Aliyun OpenAPI Meta Data.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Aliyun OpenAPI Meta Data

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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
* Fri Jul 31 19:06:44 EDT 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20200731gitfb1de10
- Initial package

