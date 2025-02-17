%define	module	Spiffy
%define upstream_version 0.46

Version:	%perl_convert_version %{upstream_version}
Name:		perl-%{module}
Release:	13
Summary:	Spiffy Perl Interface Framework For You
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/pod/Spiffy
Source0:	https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-%{upstream_version}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It
attempts to fix all the nits and warts of traditional Perl OO, in a clean,
straightforward and (perhaps someday) standard way.

Spiffy borrows ideas from other OO languages like Python, Ruby, Java and
Perl 6. It also adds a few tricks of its own.

%prep
%autosetup -p1 -n %{module}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/Spiffy*
