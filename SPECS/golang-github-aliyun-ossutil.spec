%bcond_with check

# https://github.com/aliyun/ossutil
%global goipath         github.com/aliyun/ossutil
Version:                1.6.10

%gometa

%global common_description %{expand:
A user friendly command line tool to access AliCloud OSS.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A user friendly command line tool to access AliCloud OSS

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/satori/go.uuid)(commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/ossutil %{goipath}

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
%doc CHANGELOG.md README-CN.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:41:18 EST 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-1
- Update to version 1.6.10

* Fri Nov 22 15:32:40 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 1.6.9-1
- Initial package

