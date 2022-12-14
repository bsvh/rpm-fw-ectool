%global reponame    framework-ec
%global commit      54c140399bbc3e6a3dce6c9f842727c4128367be
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20221204
%global gitrel      .%{commit_date}.git%{shortcommit}

Name:           fw-ectool
Version:        v0.3.3
Release:        1%{gitrel}%{?dist}
Summary:        A tool for interacting with the embedded controller on a Framework laptop.

License:        BSD
URL:            https://github.com/DHowett/framework-ec
Source0:        https://github.com/DHowett/framework-ec/archive/%{commit}/%{reponame}-%{shortcommit}.tar.gz
Source1:        fw-ectool.sh
Source2:		framework-caps-swap-escape.service

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  arm-none-eabi-gcc-cs
BuildRequires:  libftdi-devel
Requires:       libftdi

%description

Read and write values to the embedded controller on a Framework laptop.


%prep
%autosetup -n %{reponame}-%{commit}


%build
make utils


%install
install -Dm755 build/bds/util/ectool %{buildroot}%{_bindir}/ectool
install -m755 %SOURCE1 %{buildroot}%{_bindir}/fw-ectool
install -Dm644 %SOURCE2 %{buildroot}%{_libdir}/systemd/system/framework-caps-swap-escape.service


%clean
rm -rf %{buildroot}


%files
%license LICENSE
%{_bindir}/ectool
%{_bindir}/fw-ectool



%changelog
* Tue Dec 13 2022 Brendan Van Hook <brendan@vastactive.com>
- Add systemd unit file for swapping caps lock with escape
* Wed Oct 05 2022 Brendan Van Hook <brendan@vastactive.com>
- Initial spec file
- Add alias fw-ectool to ectool --interface=fwk
