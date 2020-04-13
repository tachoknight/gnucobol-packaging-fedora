Name:           gnucobol
Version:        2.2
Release:        1%{?dist}
Summary:        GnuCOBOL is a free implementation of the COBOL programming language.
License:        GPL
URL:            https://sourceforge.net/projects/open-cobol/
Source0:        http://ftp.gnu.org/gnu/gnucobol/gnucobol-%{version}.tar.gz

Patch0:         stackprotector.patch

BuildRequires:  make
BuildRequires:  gmp-devel
BuildRequires:  libdb-devel
BuildRequires:  gcc

Requires:       gcc
Requires:       gmp-devel
Requires:       libdb-devel


%description
GnuCOBOL is a free software COBOL compiler. 
cobc translates COBOL source code to native executable using intermediate C, 
designated C compiler and linker.


%package devel
Summary:    Headers and library files for GnuCOBOL


%description devel
Headers and libraries for building GnuCOBOL programs


%prep
%setup -q -n gnucobol-%{version}
%patch0 -p0

%build
%configure --enable-debug
make

%install
%make_install

%files
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_datadir}/gnucobol/*                                                                                                                                     
%{_datadir}/locale/**/LC_MESSAGES/gnucobol.mo 
%{_infodir}/gnucobol.info.gz
%{_infodir}/dir    
%{_mandir}/man1/cobc.1*
%{_mandir}/man1/cobcrun.1*
%license COPYING


%files devel
%{_includedir}/libcob.h
%{_includedir}/libcob
%{_libdir}/libcob.so.4.0.0
%{_libdir}/libcob.la
%{_libdir}/libcob.so.4
%{_libdir}/libcob.so
%{_libdir}/libcob.a
%{_libdir}/gnucobol


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Sat Apr 11 2020 Ron Olson <tachoknight@fedoraproject.org> 2.2-1
- Intitial version
