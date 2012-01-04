# revision 24852
# category Package
# catalog-ctan /macros/latex/contrib/titlesec
# catalog-date 2011-12-15 15:36:45 +0100
# catalog-license lppl
# catalog-version 2.10.0
Name:		texlive-titlesec
Version:	2.10.0
Release:	2
Summary:	Select alternative section titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlesec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package providing an interface to sectioning commands for
selection from various title styles. E.g., marginal titles and
to change the font of all headings with a single command, also
providing simple one-step page styles. Also includes a package
to change the page styles when there are floats in a page. You
may assign headers/footers to individual floats, too.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titlesec/block.tss
%{_texmfdistdir}/tex/latex/titlesec/drop.tss
%{_texmfdistdir}/tex/latex/titlesec/frame.tss
%{_texmfdistdir}/tex/latex/titlesec/leftmargin.tss
%{_texmfdistdir}/tex/latex/titlesec/margin.tss
%{_texmfdistdir}/tex/latex/titlesec/rightmargin.tss
%{_texmfdistdir}/tex/latex/titlesec/titleps.sty
%{_texmfdistdir}/tex/latex/titlesec/titlesec.sty
%{_texmfdistdir}/tex/latex/titlesec/titletoc.sty
%{_texmfdistdir}/tex/latex/titlesec/ttlkeys.def
%{_texmfdistdir}/tex/latex/titlesec/ttlps.def
%{_texmfdistdir}/tex/latex/titlesec/wrap.tss
%doc %{_texmfdistdir}/doc/latex/titlesec/CHANGES
%doc %{_texmfdistdir}/doc/latex/titlesec/README
%doc %{_texmfdistdir}/doc/latex/titlesec/titleps.pdf
%doc %{_texmfdistdir}/doc/latex/titlesec/titleps.tex
%doc %{_texmfdistdir}/doc/latex/titlesec/titlesec.pdf
%doc %{_texmfdistdir}/doc/latex/titlesec/titlesec.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
