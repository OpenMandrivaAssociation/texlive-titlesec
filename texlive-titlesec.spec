Name:		texlive-titlesec
Version:	59845
Release:	2
Summary:	Select alternative section titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlesec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/titlesec
%doc %{_texmfdistdir}/doc/latex/titlesec

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
