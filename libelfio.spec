#
# TODO:
# - make dynamic/static library

Summary:	elfio
Summary(pl.UTF-8):	elfio
Name:		libelfio
Version:	1.0.3
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dl.sourceforge.net/elfio/ELFIO-%{version}.tar.gz
# Source0-md5:	fd6fca12c7b43f6c01d30b23d22aaefe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package subpackage
Summary:	-
Summary(pl.UTF-8):	-
Group:		-

%description subpackage

%description subpackage -l pl.UTF-8

%package libs
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries

%description libs

%description libs -l pl.UTF-8

%package devel
Summary:	Header files for ... library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ...
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ... library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl.UTF-8):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl.UTF-8
Statyczna biblioteka ....

%prep
%setup -q -n ELFIO-%{version}

%build
##%{__libtoolize}
##%{__aclocal}
#3%{__autoconf}
##%{__autoheader}
##%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
