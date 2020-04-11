%global debug_package %{nil}
%global compdir gnucobol-2.2

Name:           GnuCOBOL
Version:        2.2
Release:        1%{?dist}
Summary:        GnuCOBOL is a free implementation of the COBOL programming language.
License:        GPL
URL:            https://sourceforge.net/projects/open-cobol/
Source0:        http://ftp.gnu.org/gnu/gnucobol/gnucobol-2.2.tar.gz

BuildRequires:  make
BuildRequires:  gmp-devel
BuildRequires:  libdb-devel
BuildRequires:  gcc

Requires:       gcc


%description
GnuCOBOL is a free software COBOL compiler. 
cobc translates COBOL source code to native executable using intermediate C, 
designated C compiler and linker.


%prep
%setup -q -n %{compdir}


%build
./configure --prefix=/usr --libdir=%{_libdir}
make

%install
%make_install

%files
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_includedir}/libcob.h
%{_includedir}/libcob
%{_libdir}/libcob.so.4.0.0
%{_libdir}/libcob.la
%{_libdir}/libcob.so.4
%{_libdir}/libcob.so
%{_libdir}/libcob.a
%{_libdir}/gnucobol
%{_datadir}/gnucobol/*                                                                                                                                     
%{_datadir}/locale/de/LC_MESSAGES/gnucobol.mo                                                                                                                
%{_datadir}/locale/en@boldquot/LC_MESSAGES/gnucobol.mo                                                                                                       
%{_datadir}/locale/en@quot/LC_MESSAGES/gnucobol.mo                                                                                                           
%{_datadir}/locale/es/LC_MESSAGES/gnucobol.mo                                                                                                                
%{_datadir}/locale/it/LC_MESSAGES/gnucobol.mo                                                                                                                
%{_datadir}/locale/ja/LC_MESSAGES/gnucobol.mo
%{_datadir}/locale/nl/LC_MESSAGES/gnucobol.mo
%{_datadir}/locale/pt/LC_MESSAGES/gnucobol.mo
%{_infodir}/gnucobol.info.gz
%{_infodir}/dir    
%{_mandir}/man1/cobc.1.gz
%{_mandir}/man1/cobcrun.1.gz
%license COPYING

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Sat Apr 11 2020 Ron Olson <tachoknight@fedoraproject.org> 2.2-1
- Intitial version
