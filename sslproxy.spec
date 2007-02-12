Summary:	sslproxy - convert a TCP Service to its SSL Variant
Summary(pl.UTF-8):	sslproxy - konwersja usług TCP na wersje SSL
Name:		sslproxy
Version:	2000_Jan_29
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.obdev.at/ftp/pub/Products/sslproxy/%{name}.%{version}.tar.gz
# Source0-md5:	784b9f24bd58af9a6de29fbb867f8f53
Patch0:		%{name}-Makefile.patch
URL:		http://www.obdev.at/products/ssl-proxy/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sslproxy is a transparent proxy that can translate between encrypted
and unencrypted data transport on socket connections. It also has a
non-transparent mode for automatic encryption-detection on NetBIOS.
sslproxy has been developed to have more secure servers available for
the secure mode of Sharity (a CIFS/SMB client for Unix). However, the
program can also be used for a multitude of other security related
applications.

%description -l pl.UTF-8
sslproxy to przezroczyste proxy potrafiące tłumaczyć między
przesyłaniem zaszyfrowanych i odszyfrowanych danych poprzez połączenia
gniazdami. Ma także tryb nieprzezroczysty do automatycznego wykrywania
szyfrowania w NetBIOS. sslproxy jest tworzone aby udostępnić bardziej
bezpieczne serwery dla bezpiecznego trybu Sharity (klienta CIFS/SMB
dla Uniksa). Jednak program ten może być używany z wieloma innymi
aplikacjami związanymi z bezpieczeństwem.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install sslproxy $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dummyCert.pem README.txt
%attr(755,root,root) %{_sbindir}/*
