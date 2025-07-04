%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%bcond_without qt5

Name: breeze
Version:	6.4.2
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/breeze/-/archive/%{gitbranch}/breeze-%{gitbranchd}.tar.bz2#/breeze-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{major}/breeze-%{version}.tar.xz
%endif
Summary: The KDE 6 Breeze style
URL: https://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(xcb)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KDecoration3)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6FrameworkIntegration)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(Wayland) >= 5.90.0
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: pkgconfig(fftw3)
%if %{with qt5}
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5WindowSystem)
%endif
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_QT5:BOOL=%{?with_qt5:ON}%{!?with_qt5:OFF}
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-01
%rename plasma6-breeze

%patchlist

%description
The KDE 6 Breeze style.

%package qt5
Summary: The Plasma 6 Breeze style for Qt 5.x applications
Group: Graphical desktop/KDE

%description qt5
The Plasma 6 Breeze style for Qt 5.x applications

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}
Provides: %{name}-devel = %{EVRD}
# Renamed 2025-05-01 after 6.0
%rename plasma6-breeze-devel

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files -f %{name}.lang
%{_bindir}/breeze-settings6
%{_bindir}/kcursorgen
%{_datadir}/icons/breeze_cursors
%{_datadir}/icons/Breeze_Light
%{_datadir}/wallpapers/*
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/QtCurve
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeLight.colors
%{_qtdir}/plugins/styles/breeze6.so
%{_qtdir}/plugins/org.kde.kdecoration3/*.so
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%{_datadir}/color-schemes/BreezeClassic.colors
%{_qtdir}/plugins/kstyle_config/breezestyleconfig.so
%{_datadir}/applications/breezestyleconfig.desktop
%{_datadir}/applications/kcm_breezedecoration.desktop
%dir %{_qtdir}/plugins/org.kde.kdecoration3.kcm
%{_qtdir}/plugins/org.kde.kdecoration3.kcm/kcm_breezedecoration.so

%if %{with qt5}
%files qt5
%{_libdir}/qt5/plugins/styles/breeze5.so
%endif

%files devel
%{_libdir}/cmake/Breeze
