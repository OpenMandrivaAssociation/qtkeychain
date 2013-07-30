%define lib_major 0
%define lib_name %mklibname %name %{lib_major}
%define lib_dev %mklibname %name -d

Name: qtkeychain
Summary: Platform-independent Qt API for storing passwords securely
Version: 0.1.0
Release: 1
Url: https://github.com/frankosterfeld/qtkeychain
License: LGPLv2+
Group: Graphical desktop/KDE
Source0: %name-%version.tar.gz
BuildRequires: qt4-devel
BuildRequires: cmake

%description
Platform-independent Qt API for storing passwords securely

#------------------------------------------------------------------

%package -n %{lib_name}
Summary:  Platform-independent Qt API for storing passwords securely
Group: System/Libraries

%description -n %{lib_name}
Platform-independent Qt API for storing passwords securely

%files -n %{lib_name}
%{_libdir}/libqtkeychain.so.%{lib_major}*

#------------------------------------------------------------------

%package -n %{lib_dev}
Summary: Development tools for programs which will use the %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}

%description -n %{lib_dev}
This package contains the header files and .so libraries 
for developing %{name}.

%files -n %{lib_dev}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/QtKeychain

#------------------------------------------------------------------

%prep
%setup -q -n %name-0.1

%build
%cmake_qt4 

%make

%install
%makeinstall_std -C build



%changelog

* Mon Apr 01 2013 neoclust <neoclust> 0.1.0-2.mga3
+ Revision: 407076
- Do not requires qtkeychain package as it does not exist
