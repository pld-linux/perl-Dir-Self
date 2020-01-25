#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Dir
%define		pnam	Self
Summary:	Dir::Self - a __DIR__ constant for the directory your source file is in
Summary(pl.UTF-8):	Dir::Self - stała __DIR__ dla katalogu, w którym znajduje się plik źródłowy
Name:		perl-Dir-Self
Version:	0.11
Release:	1
# same as perl 5.8.8+
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Dir/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e484446c3aa042737c0b7cbd0fb2f904
URL:		http://search.cpan.org/dist/Dir-Self/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.48
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl has two pseudo-constants describing the current location in your
source code, __FILE__ and __LINE__. This module adds __DIR__, which
expands to the directory your source file is in, as an absolute
pathname.

%description -l pl.UTF-8
Perl ma dwie pseudo-stałe opisujące aktualne położenie kodu
źródłowego: __FILE__ i __LINE__. Ten moduł dodaje __DIR__, rozwijającą
się do katalogu, w którym znajduje się plik źródłowy, w postaci
ścieżki bezwzględnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Dir/Self.pm
%{_mandir}/man3/Dir::Self.3pm*
