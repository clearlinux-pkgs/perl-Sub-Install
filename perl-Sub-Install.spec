#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Install
Version  : 0.928
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-0.928.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-0.928.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-handle-util-perl/libio-handle-util-perl_0.01-2.debian.tar.xz
Summary  : 'install subroutines into packages easily'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Install-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Sub-Install,
version 0.928:
install subroutines into packages easily

%package dev
Summary: dev components for the perl-Sub-Install package.
Group: Development
Provides: perl-Sub-Install-devel = %{version}-%{release}

%description dev
dev components for the perl-Sub-Install package.


%package license
Summary: license components for the perl-Sub-Install package.
Group: Default

%description license
license components for the perl-Sub-Install package.


%prep
%setup -q -n Sub-Install-0.928
cd ..
%setup -q -T -D -n Sub-Install-0.928 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Sub-Install-0.928/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Install
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Install/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Sub-Install/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.26.1/Sub/Install.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Install.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Install/LICENSE
/usr/share/package-licenses/perl-Sub-Install/deblicense_copyright
