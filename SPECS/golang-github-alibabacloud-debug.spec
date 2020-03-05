%bcond_with check

# https://github.com/alibabacloud-go/debug
%global goipath         github.com/alibabacloud-go/debug
%global commit          9472017b5c6804c66e5d873fabd2a2a937b31e0b

%gometa

%global common_description %{expand:
Alibaba Cloud Debug function for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Alibaba Cloud Debug function for Golang

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/debug %{goipath}

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
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:40:37 EST 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20200304git9472017
- Enable check stage
- Add common_description and Summary

* Fri Nov 22 16:08:39 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git9472017
- Initial package

