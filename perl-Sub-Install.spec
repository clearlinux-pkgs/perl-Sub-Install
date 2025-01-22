#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Sub-Install
Version  : 0.929
Release  : 43
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-0.929.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-0.929.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-handle-util-perl/libio-handle-util-perl_0.01-2.debian.tar.xz
Summary  : 'install subroutines into packages easily'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Install-license = %{version}-%{release}
Requires: perl-Sub-Install-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Sub-Install,
version 0.929:
install subroutines into packages easily

%package dev
Summary: dev components for the perl-Sub-Install package.
Group: Development
Provides: perl-Sub-Install-devel = %{version}-%{release}
Requires: perl-Sub-Install = %{version}-%{release}

%description dev
dev components for the perl-Sub-Install package.


%package license
Summary: license components for the perl-Sub-Install package.
Group: Default

%description license
license components for the perl-Sub-Install package.


%package perl
Summary: perl components for the perl-Sub-Install package.
Group: Default
Requires: perl-Sub-Install = %{version}-%{release}

%description perl
perl components for the perl-Sub-Install package.


%prep
%setup -q -n Sub-Install-0.929
cd %{_builddir}
tar xf %{_sourcedir}/libio-handle-util-perl_0.01-2.debian.tar.xz
cd %{_builddir}/Sub-Install-0.929
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sub-Install-0.929/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Install
cp %{_builddir}/Sub-Install-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Install/b3081ec3c2924490fae7d408f798f3c2f45777d3 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sub-Install/c7cbead4fc445ef2748335e1d1a81a21d992aad2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Install.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Install/b3081ec3c2924490fae7d408f798f3c2f45777d3
/usr/share/package-licenses/perl-Sub-Install/c7cbead4fc445ef2748335e1d1a81a21d992aad2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
