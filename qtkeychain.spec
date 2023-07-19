%bcond_without qt5
%bcond_without qt6

%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define libqt6name Qt6 %mklibname
%define devqt6name Qt6 %mklibname -d

Summary:	Platform-independent Qt API for storing passwords securely
Name:		qtkeychain
Version:	0.13.2
Release:	2
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://github.com/frankosterfeld/qtkeychain
Source0:	https://github.com/frankosterfeld/qtkeychain/archive/v%{version}/%{name}-%{version}.tar.gz
	
# Fix qt6 detection broken by including ECMGeneratePriFile
Patch0:         qtkeychain-qt6.patch

BuildRequires:	cmake
%if %{with qt5}
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
%endif
BuildRequires:	pkgconfig(libsecret-1)
%if %{with qt6}
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6DBus)
%endif
%description
Platform-independent Qt API for storing passwords securely.


#----------------------------------------------------------------------------
%if %{with qt5}
%package common
Summary:	Common files for %{name} (translations etc)
Group:		System/Libraries

%description common
Common files for %{name} (translations etc).

%files common -f %{name}.lang

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Platform-independent Qt API for storing passwords securely
Group:		System/Libraries
Requires:	%{name}-common

%description -n %{libname}
Platform-independent Qt API for storing passwords securely.

%files -n %{libname}
%{_libdir}/libqt5keychain.so.%{major}*
%{_libdir}/libqt5keychain.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development tools for programs which will use the %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the header files and .so libraries for developing
%{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Qt5Keychain
%{_prefix}/mkspecs/modules/*
%endif
#----------------------------------------------------------------------------

%if %{with qt6}
%package %{libqt6name}
Summary:        %{summary}
Requires:	%{name}-common

%description %{libqt6name}
The qt6keychain library allows you to store passwords easily and securely.
 
 
%package %{devqt6name}
Summary:        Development files for %{name}-qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
Requires:       %{libqt6name} = %{EVRD}
Requires:       cmake(Qt6Core)
# deps referenced in Qt6KeychainLibraryDepends-relwithdebinfo.cmake:  IMPORTED_LINK_INTERFACE_LIBRARIES_RELWITHDEBINFO "Qt6::Core;secret-1;gio-2.0;gobject-2.0;glib-2.0;Qt6::DBus"
# *probably* overlinking and can be pruned, but requires closer inspection
Requires:       pkgconfig(libsecret-1)
 
%description %{devqt6name}
This package contains development files for qt6keychain.
%endif

%if %{with qt6}
%files %{libqt6name}
%license COPYING
%{_libdir}/libqt6keychain.so.1
%{_libdir}/libqt6keychain.so.0*
 
%files %{devqt6name}
%{_includedir}/qt6keychain/
%{_libdir}/cmake/Qt6Keychain/
%{_libdir}/libqt6keychain.so
%endif
#---------------------------------------------------------------------------- 

%prep
%autosetup -p1

%build	
%if %{with qt5}
export CMAKE_BUILD_DIR=build-qt5
%cmake_qt5
%make_build
cd ..
%endif
	
%if %{with qt6}
export CMAKE_BUILD_DIR=build-qt6
%cmake \
  -DBUILD_WITH_QT6:BOOL=ON
%make_build
cd ..
%endif

%install
%make_install -C build

%make_install -C build-qt6


%find_lang %{name} --with-qt
