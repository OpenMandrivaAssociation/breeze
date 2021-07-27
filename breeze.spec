%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: breeze
Version:	5.22.4
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
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5Wayland)
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
%{_libdir}/kconf_update_bin/kde4breeze
%{_libdir}/libbreezecommon5.so*
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/fullscreenpreview.jpg
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.*
%{_datadir}/kconf_update/breezetobreezelight.upd
%{_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop
%{_datadir}/icons/breeze_cursors
%{_datadir}/icons/Breeze_Snow
%{_datadir}/wallpapers
%optional %{_datadir}/metainfo/*.xml
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/kconf_update/kde4breeze.upd
%{_libdir}/kconf_update_bin/breezetobreezelight
%{_datadir}/QtCurve
%{_datadir}/color-schemes/Breeze.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeHighContrast.colors
%{_datadir}/color-schemes/BreezeLight.colors
%{_libdir}/qt5/plugins/kstyle_breeze_config.so
%{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/*.so
%{_datadir}/kservices5/*.desktop
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz

%files devel
%{_libdir}/cmake/Breeze
