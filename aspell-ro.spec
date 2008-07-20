Summary:	Romanian dictionary for aspell
Summary(pl.UTF-8):	Rumuński słownik dla aspella
Name:		aspell-ro
Version:	3.1
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ro/aspell5-ro-%{version}.tar.bz2
# Source0-md5:	9be13b83c2eb441db38932933ae2a9c8
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Romanian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Rumuński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell5-ro-%{version}

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
%{_libdir}/aspell/*
%{_datadir}/aspell/*
