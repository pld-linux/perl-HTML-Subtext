%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Subtext
Summary:	HTML::Subtext module - performs text substitutions on an HTML template
Summary(pl):	Modu³ HTML::Subtext - dokonuj±cy podmiany tekstu w szablonie HTML
Name:		perl-HTML-Subtext
Version:	1.03
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Subtext is a package for performing text substitutions on a
specially formatted HTML template. The template uses normal HTML
markup, but includes special links.

%description -l pl
HTML::Subtext to pakiet dokonuj±cy podmiany tekstu w specjalnie
sformatowanym szablonie HTML. Szablon u¿ywa normalnych znaczników
HTML, ale zawiera specjalne odno¶niki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/Subtext.pm
%{_mandir}/man3/*
