#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Subtext
Summary:	HTML::Subtext Perl module - performs text substitutions on an HTML template
Summary(pl.UTF-8):	Moduł Perla HTML::Subtext - podmiana tekstu w szablonie HTML
Name:		perl-HTML-Subtext
Version:	1.03
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94f653b74dee5799efd40f10740ade88
URL:		http://search.cpan.org/dist/HTML-Subtext/
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Subtext is a package for performing text substitutions on a
specially formatted HTML template. The template uses normal HTML
markup, but includes special links.

%description -l pl.UTF-8
HTML::Subtext to pakiet dokonujący podmiany tekstu w specjalnie
sformatowanym szablonie HTML. Szablon używa normalnych znaczników
HTML, ale zawiera specjalne odnośniki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/Subtext.pm
%{_mandir}/man3/*
