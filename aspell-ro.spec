Summary:	Romanian dictionary for aspell
Summary(pl.UTF-8):	Rumuński słownik dla aspella
Name:		aspell-ro
Version:	3.3
%define	subv	2
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ro/aspell5-ro-%{version}-%{subv}.tar.bz2
# Source0-md5:	2d708c95fd7711efc61673c77f5f9d9e
URL:		http://rospell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
BuildRequires:	which
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Romanian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Rumuński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell5-ro-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/aspell/ro-*.*
%{_libdir}/aspell/ro.*
%{_libdir}/aspell/romanian.alias
%{_libdir}/aspell/romanian-classic.alias
%{_datadir}/aspell/ro.dat
