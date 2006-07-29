Summary:	SMB for Fuse
Summary(pl):	SMB dla Fuse
Name:		fusesmb
Version:	0.8.5
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.ricardis.tudelft.nl/~vincent/fusesmb/download/%{name}-%{version}.tar.gz
# Source0-md5:	8b9268826b544ad124e016ced17d5310
URL:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/
BuildRequires:	libfuse-devel >= 2.3
BuildRequires:	libsmbclient-devel >= 3.0
# needed by stupid configure check, anyone wants to write a patch?
BuildRequires:	samba-client
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With SMB for Fuse you can seamlessly browse your network
neighbourhood as were it on your own filesystem.

It's basically smbmount with a twist. Instead of mounting one Samba
share at a time, you mount all workgroups, hosts and shares at once.
Only when you're accessing a share a connection is made to the
remote computer.

%description -l pl
Z pomoc± SMB dla Fuse mo¿na przegl±daæ otoczenie sieciowe, tak jakby
by³o ono systemem plików.

W uproszczeniu, jest to smbmount z haczykiem. Zamiast montowaæ jeden
udzia³ Samby, montuje siê wszystykie grupy robocze, komputery
i udzia³y na raz. Po³±czenie do zdalnego komputera jest wykonywane
tylko przy próbie dostêpu do udzia³u.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO fusesmb.conf.ex
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
