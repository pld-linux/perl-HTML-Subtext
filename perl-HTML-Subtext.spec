%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	HTML-Subtext perl module
Summary(pl):	Modu³ perla HTML-Subtext
Name:		perl-HTML-Subtext
Version:	1.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Subtext-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-HTML-Parser
Requires:	perl-URI
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-Subtext perl module

%description -l pl
Modu³ perla HTML-Subtext

%prep
%setup -q -n HTML-Subtext-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/Subtext
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/HTML/Subtext.pm
%{perl_sitearch}/auto/HTML/Subtext

%{_mandir}/man3/*
