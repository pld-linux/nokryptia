Summary:	Nokia 5510 tool
Summary(pl):	Narzêdzia dla Nokii 5510
Name:		nokryptia
Version:	1.2
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://mobilix.org/software/nokryptia/%{name}-%{version}.tgz
URL:		http://mobilix.org/nokryptia.html
BuildRequires:	id3lib-devel >= 3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Nokia 5510 tool.

%description -l pl
Narzêdzie do zarz±dzania telefonem Nokia 5510 pod³±czonym do poru USB.

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
