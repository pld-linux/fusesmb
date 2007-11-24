Summary:	SMB for Fuse
Summary(pl.UTF-8):	SMB dla Fuse
Name:		fusesmb
Version:	0.8.7
Release:	1.1
License:	GPL
Group:		Applications/System
Source0:	http://www.ricardis.tudelft.nl/~vincent/fusesmb/download/%{name}-%{version}.tar.gz
# Source0-md5:	ff5adc291b18fd452fe4694cbe45dabd
Patch0:		%{name}-no_clientchk.patch
Patch1:		%{name}-free_vg.patch
Patch2:		%{name}-more_debug.patch
Patch3:		%{name}-rewindir.patch
Patch4:		%{name}-sv.patch
Patch5:		%{name}-debug_write.patch
URL:		http://www.ricardis.tudelft.nl/~vincent/fusesmb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.3
BuildRequires:	libsmbclient-devel >= 3.0
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With SMB for Fuse you can seamlessly browse your network
neighbourhood as were it on your own filesystem.

It's basically smbmount with a twist. Instead of mounting one Samba
share at a time, you mount all workgroups, hosts and shares at once.
Only when you're accessing a share a connection is made to the
remote computer.

%description -l pl.UTF-8
Z pomocą SMB dla Fuse można przeglądać otoczenie sieciowe, tak jakby
było ono systemem plików.

W uproszczeniu, jest to smbmount z haczykiem. Zamiast montować jeden
udział Samby, montuje się wszystykie grupy robocze, komputery
i udziały na raz. Połączenie do zdalnego komputera jest wykonywane
tylko przy próbie dostępu do udziału.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO fusesmb.conf.ex
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
