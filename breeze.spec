%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: breeze
Version: 5.4.0
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
Summary: The KDE 5 Breeze style
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xcb)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(KF5KCMUtils)

%description
The KDE 5 Breeze style.

%prep
%setup -q
%cmake_kde5 -DUSE_KDE4=false

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang breeze_style_config
%find_lang breeze_kwin_deco
cat  *.lang >all.lang

%files -f all.lang
%{_bindir}/breeze-settings5
%{_libdir}/kconf_update_bin/kde4breeze
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Breeze
%{_datadir}/icons/breeze
%{_datadir}/icons/breeze_cursors
%{_datadir}/icons/breeze-dark
%{_datadir}/icons/Breeze_Snow
%{_datadir}/wallpapers
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/QtCurve
%{_datadir}/color-schemes/Breeze.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeHighContrast.colors
%{_datadir}/kconf_update/gtkbreeze.upd
%{_libdir}/kconf_update_bin/gtkbreeze
%{_libdir}/qt5/plugins/kstyle_breeze_config.so
%{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/*.so
%{_datadir}/kservices5/*.desktop
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
