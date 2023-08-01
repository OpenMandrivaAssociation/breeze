%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: breeze
Version:	5.27.7
Release:	1
Source0: http://download.kde.org/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
Summary: The KDE 5 Breeze style
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xcb)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KDecoration2) < 5.27.50
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: plasma-lookandfeelexplorer
BuildRequires: pkgconfig(fftw3)

%description
The KDE 5 Breeze style.

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}
Provides: %{name}-devel = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%prep
%autosetup -p1

%build
%cmake_kde5 -DUSE_KDE4=OFF
%ninja

%install
%ninja_install -C build

%find_lang breeze_style_config || touch breeze_style_config.lang
%find_lang breeze_kwin_deco || touch breeze_kwin_deco.lang
cat  *.lang >all.lang

%files -f all.lang
%{_bindir}/breeze-settings5
%{_libdir}/libbreezecommon5.so*
%{_datadir}/kconf_update/breezetobreezelight.upd
%{_datadir}/icons/breeze_cursors
%{_datadir}/icons/Breeze_Snow
%{_datadir}/wallpapers/*
%{_datadir}/kstyle/themes/breeze.themerc
%{_libdir}/kconf_update_bin/breezetobreezelight
%{_datadir}/QtCurve
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeLight.colors
%{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/*.so
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%{_libdir}/kconf_update_bin/breezehighcontrasttobreezedark
%{_libdir}/kconf_update_bin/breezetobreezeclassic
%{_datadir}/color-schemes/BreezeClassic.colors
%{_datadir}/kconf_update/breezehighcontrasttobreezedark.upd
%{_datadir}/kconf_update/breezetobreezeclassic.upd
%{_libdir}/qt5/plugins/plasma/kcms/breeze/kcm_breezedecoration.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/breezestyleconfig.so
%{_datadir}/applications/breezestyleconfig.desktop
%{_datadir}/applications/kcm_breezedecoration.desktop

%files devel
%{_libdir}/cmake/Breeze
