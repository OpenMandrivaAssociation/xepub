Name:		xepub
Version:	1.0.3
Release:	1
Summary:	EPUB reader for the Linux desktop
License:        GPL-3+
URL:            https://github.com/xapp-project/xepub
Source0:	https://github.com/xapp-project/xepub/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:	gtk-update-icon-cache
BuildRequires:	lib64glib2.0-devel
BuildRequires:	lib64gio-gir2.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:       lib64gtk-gir3.0
Requires:       lib64webkit2gtk-gir4.1
Requires:       python
Requires:       python-gi
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       xapp-symbolic-icons

%description
EPUB reader for the Linux desktop

%prep
%autosetup -p1

%files
%license LICENSES/*
%doc README.md
%{_bindir}/xepub
%{_datadir}/xepub
%{_datadir}/glib-2.0/schemas/org.x.xepub.gschema.xml
%{_datadir}/applications/xepub.desktop
%{_datadir}/icons/hicolor/scalable/apps/xepub.svg
