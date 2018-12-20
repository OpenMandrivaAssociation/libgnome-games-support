%define major		3
%define api		1
%define libname		%mklibname gnome-games-support %{api} %{major}
%define develname	%mklibname gnome-games-support -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		libgnome-games-support
Version:	1.4.3
Release:	1
Summary:	Support library for GNOME games
Group:		Development/GNOME and GTK+
License:	LGPLv3+
URL:		https://git.gnome.org/browse/%{name}/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) >= 2.40
BuildRequires:	pkgconfig(gio-2.0) >= 2.40
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	intltool

%description
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

#------------------------------------

%package	i18n
Summary:	Support library for GNOME games - translations
Group:		System/Internationalization
BuildArch:	noarch

Obsoletes:	libgames-support-i18n < 1.0.2-2

%description	i18n
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

This package contains translations used by %{name}.

#------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries
Requires:	%{name}-i18n = %{version}-%{release}

Obsoletes:	%{_lib}games-support2 < 1.0.2-2

%description -n %{libname}
libgnome-games-support is a small library intended for internal use by GNOME Games,
but it may be used by others. The API will only break with the major version
number. The ABI is unstable.

#------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

Obsoletes:	%{_lib}games-support-devel < 1.0.2-2

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%doc README
%license COPYING.LESSER
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{develname}
%doc README
%license COPYING.LESSER
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/gnome-games-support-%{api}/
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}*.pc
