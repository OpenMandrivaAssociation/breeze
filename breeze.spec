%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%bcond_without kde4

Name: breeze
Version: 5.6.1
Release: 1
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

%description
The KDE 5 Breeze style.

%if %{with kde4}
%package kde4
Summary:	The KDE 4 Breeze style
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	kdelibs-devel
Requires:	kdelibs4-core

%description kde4
The KDE 4 Breeze style.
%endif

%prep
%setup -q

%build
%cmake_kde5 -DUSE_KDE4=OFF
%ninja


%if %{with kde4}
cd ..
mkdir build-kde4
pushd build-kde4
%cmake_kde4 ../.. \
    -DUSE_KDE4=ON \
    -DBUILD_TESTING:BOOL=OFF

%make

%endif

%install
%if %{with kde4}
pushd build-kde4
%makeinstall_std -C build
mkdir -p %{buildroot}%{_qt_plugindir}/styles/
ln -s %{_kde_libdir}/kde4/plugins/styles/breeze.so %{buildroot}%{_qt_plugindir}/styles/breeze.so
popd
%endif

%ninja_install -C build

%find_lang breeze_style_config
%find_lang breeze_kwin_deco
cat  *.lang >all.lang

%files -f all.lang
%{_bindir}/breeze-settings5
%{_libdir}/kconf_update_bin/kde4breeze
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Breeze
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/contents/previews/preview.png
%{_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/metadata.desktop
%{_datadir}/icons/breeze_cursors
%{_datadir}/icons/Breeze_Snow
%{_datadir}/wallpapers
%{_datadir}/kstyle/themes/breeze.themerc
%{_datadir}/kconf_update/kde4breeze.upd
%{_datadir}/QtCurve
%{_datadir}/color-schemes/Breeze.colors
%{_datadir}/color-schemes/BreezeDark.colors
%{_datadir}/color-schemes/BreezeHighContrast.colors
%{_libdir}/qt5/plugins/kstyle_breeze_config.so
%{_libdir}/qt5/plugins/styles/breeze.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/*.so
%{_datadir}/kservices5/*.desktop
%{_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz

%if %{with kde4}
%files kde4
%{_libdir}/kde4/plugins/styles/breeze.so
%{_libdir}/kde4/kstyle_breeze_config.so
%{_datadir}/apps/kstyle/themes/breeze.themerc
%{_qt_plugindir}/styles/breeze.so
%endif
