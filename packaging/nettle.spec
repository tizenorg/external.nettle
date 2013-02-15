%define nettlemajor 4
%define hogweedmajor 2
%define develname nettle-devel

Name:		nettle
Summary:	Nettle cryptographic library
Version:	2.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.lysator.liu.se/~nisse/nettle/
Source:		http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	openssl-devel
BuildRequires:	gmp-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more or less any context:
In crypto toolkits for object-oriented languages (C++, Python, Pike, ...),
in applications like LSH or GNUPG, or even in kernel space.

%package -n %develname
Group:		Development/C++
Summary:	Header files for compiling against Nettle library
Provides:	%name-devel = %{version}-%{release}

%description -n %develname
This is the development package of nettle.

%prep
%setup -q

%build
%configure --disable-openssl --enable-shared
make

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%manifest nettle.manifest
%{_bindir}/*
%{_infodir}/*
%{_libdir}/libnettle.so.%{nettlemajor}*
%{_libdir}/libhogweed.so.%{hogweedmajor}*

%files -n %develname
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_includedir}/nettle

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
