%define major 0
%define libname %mklibname %name %{major}
%define devname %mklibname %name -d

Summary:	Platform-independent Qt API for storing passwords securely
Name:		qtkeychain
Version:	0.3.0
Release:	2
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://github.com/frankosterfeld/qtkeychain
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt4-devel

%description
Platform-independent Qt API for storing passwords securely.

#----------------------------------------------------------------------------

%package common
Summary:	Common files for %{name} (translations etc)
Group:		System/Libraries
Requires:	%{name}-common

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
%{_libdir}/libqtkeychain.so.%{major}*

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
%{_libdir}/cmake/QtKeychain

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4 -DBUILD_WITH_QT4:BOOL=ON
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-qt
