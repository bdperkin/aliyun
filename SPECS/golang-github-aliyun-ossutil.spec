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
Release:        2%{?dist}
Summary:        A user friendly command line tool to access AliCloud OSS

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/alyu/configparser)
BuildRequires:  golang(github.com/droundy/goopt)
BuildRequires:  golang(github.com/satori/go.uuid)(commit=b2ce2384e17bbe0c6d34077efa39dbab3e09123b)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  help2man
BuildRequires:  gzip

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
mkdir -p %{gobuilddir}/share/man/man1
help2man -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/ossutil.1 -N --version-string="%{version}" %{gobuilddir}/bin/ossutil
gzip %{gobuilddir}/share/man/man1/ossutil.1

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CHANGELOG.md README-CN.md README.md
%{_mandir}/man1/ossutil.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Mar 06 16:46:31 EST 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-2
- Add man page

* Wed Mar 04 16:41:18 EST 2020 Brandon Perkins <bperkins@redhat.com> - 1.6.10-1
- Update to version 1.6.10

* Fri Nov 22 15:32:40 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 1.6.9-1
- Initial package

