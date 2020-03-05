%bcond_with check

# https://github.com/droundy/goopt
%global goipath         github.com/droundy/goopt
%global commit          0b8effe182da161d81b011aba271507324ecb7ab

%gometa

%global common_description %{expand:
Getopt-like flags package for golang.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Getopt-like flags package for golang

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in test-program; do
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
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:41:20 EST 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20200304git0b8effe
- Enable check stage

* Fri Nov 22 16:48:31 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git0b8effe
- Initial package

