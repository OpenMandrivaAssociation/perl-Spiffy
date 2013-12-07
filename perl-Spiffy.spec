%define	module	Spiffy

Version:	0.30
Name:		perl-%{module}
Release:	15
Summary:	Spiffy Perl Interface Framework For You
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It
attempts to fix all the nits and warts of traditional Perl OO, in a clean,
straightforward and (perhaps someday) standard way.

Spiffy borrows ideas from other OO languages like Python, Ruby, Java and
Perl 6. It also adds a few tricks of its own.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Spiffy.pm
%{_mandir}/man3/*

