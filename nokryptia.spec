Summary:	Nokia 5510 tool
Summary(pl):	Narzêdzia dla Nokii 5510
Name:		nokryptia
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://tuxmobil.org/software/nokryptia/%{name}-%{version}.tar.bz2
# Source0-md5:	10c9509d7a78df9677aa4e92f753668a
URL:		http://www.tuxmobil.org/nokryptia.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	id3lib-devel >= 3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Nokia 5510 tool.

%description -l pl
Narzêdzie do zarz±dzania telefonem Nokia 5510 pod³±czonym do portu
USB.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
