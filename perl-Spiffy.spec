%define	module	Spiffy

Version:	0.30
Name:		perl-%{module}
Release:	12
Summary:	Spiffy Perl Interface Framework For You
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
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
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/Spiffy.pm


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30-9mdv2012.0
+ Revision: 765652
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30-8
+ Revision: 764164
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.30-7
+ Revision: 763098
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.30-6
+ Revision: 667310
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.30-5mdv2011.0
+ Revision: 426589
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.30-4mdv2009.0
+ Revision: 224055
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.30-3mdv2008.1
+ Revision: 180566
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 0.30-2mdv2008.0
+ Revision: 18035
- rebuild


* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-1mdk
- 0.30

* Tue Jan 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.29-1mdk
- 0.29

* Thu Jan 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.27-1mdk
- 0.27

* Wed Jan 18 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.26-1mdk
- 0.26

* Tue Jan 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.25-1mdk
- 0.25

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.24-1mdk
- 0.24

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdk 
- 0.23
- spec cleanup

* Wed Jan 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.22-1mdk
- 0.22

* Thu Dec 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.21-1mdk
- First MDK release

