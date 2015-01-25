%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: breeze
Version: 5.1.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
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
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Service)
#BuildRequires: cmake(KDecorations)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(Qt5)
BuildRequires: ninja

%description
The KDE 5 Breeze style

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install
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
%{_datadir}/kconf_update/gtkbreeze.upd
%{_libdir}/kconf_update_bin/gtkbreeze
%{_libdir}/qt5/plugins/kstyle_breeze_config.so
%{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/*.so
