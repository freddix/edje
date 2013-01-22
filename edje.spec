Summary:	Enlightenment Foundation Library
Name:		edje
Version:	1.7.4
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	f09010b74a1e19056666f2ccc9af219c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	eio-devel
BuildRequires:	embryo-devel
BuildRequires:	libtool
BuildRequires:	lua-devel
BuildRequires:	pkg-config
Requires(post,postun):	shared-mime-info
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evas-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edje is a complex graphical design & layout library.

%package libs
Summary:	Edje library
Group:		Libraries

%description libs
Edje library.

%package devel
Summary:	Header files for edje library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for edje library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/edje/modules

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/edje*
%attr(755,root,root) %{_bindir}/inkscape2edc
%dir %{_libdir}/edje
%dir %{_libdir}/edje/utils
%dir %{_libdir}/edje/modules
%attr(755,root,root) %dir %{_libdir}/edje/utils/epp
%dir %{_datadir}/edje
%{_datadir}/edje/include
%{_datadir}/mime/packages/edje.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libedje.so.1
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so
%{_includedir}/edje-1
%{_pkgconfigdir}/edje.pc

