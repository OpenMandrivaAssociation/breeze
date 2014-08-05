%define debug_package %{nil}

Name: breeze
Version: 5.0.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE 5 Breeze style
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KDecorations)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(Qt5)
BuildRequires: ninja

%description
The KDE 5 Breeze style

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_libdir}/kconf_update_bin/kde4breeze
%{_libdir}/qml/QtQuick/Controls/Styles/Breeze
%{_datadir}/icons/breeze
%{_datadir}/icons/breeze_cursors
%{_datadir}/kwin/decorations/kwin4_decoration_qml_breeze
%{_datadir}/wallpapers
%{_datadir}/kservices5/kwin/kwin4_decoration_qml_breeze.desktop
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/QtCurve
%{_datadir}/color-schemes/Breeze.colors
