%define	module	Spiffy
%define	name	perl-%{module}
%define	version	0.30
%define	release	%mkrel 6

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Spiffy Perl Interface Framework For You
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/Spiffy.pm

