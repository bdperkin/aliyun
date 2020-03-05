%bcond_with check

# https://github.com/alyu/configparser
%global goipath         github.com/alyu/configparser
%global commit          744e9a66e7bcb83ea09084b979ddd1efc1f2f418

%gometa

%global common_description %{expand:
Config ini file parser in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Config ini file parser in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Wed Mar 04 16:41:19 EST 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20200304git744e9a6
- Enable check stage
- Remove perl-Digest-SHA BuildRequires for tests

* Fri Nov 22 16:20:17 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git744e9a6
- Initial package

