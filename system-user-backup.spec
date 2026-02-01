Name: system-user-backup
Version: 0.1
Release: 1%{?dist}
Summary: Service templates for systemd that backup and restore system user state
License: MIT
URL: https://github.com/jdmarble/%{name}

Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: rclone

%description
Service templates for systemd that backup and restore system user state.

%prep
%setup -q

%install
install -DZ --target-directory=%{buildroot}%{_libdir}/systemd/system \
  --mode u=rw,go=r \
  backup@.service \
  backup@.timer \
  restore@.service

%files
%{_libdir}/systemd/system/backup@.service
%{_libdir}/systemd/system/backup@.timer
%{_libdir}/systemd/system/restore@.service

%post
systemctl daemon-reload

%changelog
* Fri Nov 21 2025 James D. Marble <jdmarble@jdmarble.com> 0.1-1
- new package built with tito
