Summary:	Romanian dictionary for aspell
Summary(pl):	Rumu�ski s�ownik dla aspella
Name:		aspell-ro
Version:	0.50
%define	subv	2
Release:	1
Epoch:		1
License:	free to use, no restrictions
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Romanian dictionary (i.e. word list) for aspell.

%description -l pl
Rumu�ski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*