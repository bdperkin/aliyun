%bcond_with check

# https://github.com/aliyun/aliyun-oss-go-sdk
%global goipath         github.com/aliyun/aliyun-oss-go-sdk
Version:                2.0.6

%gometa

%global common_description %{expand:
Aliyun OSS SDK for Go.}

%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Aliyun OSS SDK for Go

License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/time/rate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/baiyubin/aliyun-sts-go-sdk/sts)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/aliyun-oss-go-sdk %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc CHANGELOG.md README-CN.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Mar 04 16:41:05 EST 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.6-1
- Update to version 2.0.6
- Added ASL 2.0 License

* Fri Nov 22 18:02:03 UTC 2019 Brandon Perkins <bperkins@redhat.com> - 2.0.4-1
- Initial package

