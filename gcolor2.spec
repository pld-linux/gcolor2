# TODO:
# - check x86_64 arch, and when needed, please apply this patch:
#	http://repos.archlinux.org/wsvn/community/gcolor2/trunk/gcolor2-0.4-amd64.patch
Summary:	gcolor2 is a simple color selector
Name:		gcolor2
Version:	0.4
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/project/gcolor2/gcolor2/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	223a126b8a87234d1552be4be4140789
Source1:	%{name}.desktop
Patch0:		%{name}-missing-includes.patch
URL:		http://gcolor2.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcolor2 is a simple color selector that was originally based on
gcolor, ported to use GTK+2, and now has a completely new UI.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/%{name}
%{_desktopdir}/%{name}.desktop
