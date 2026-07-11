%global tl_name titlesec
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.17
Release:	%{tl_revision}.1
Summary:	Select alternative section titles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/titlesec
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlesec.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package providing an interface to sectioning commands for selection
from various title styles. E.g., marginal titles and to change the font
of all headings with a single command, also providing simple one-step
page styles. Also includes a package to change the page styles when
there are floats in a page. You may assign headers/footers to individual
floats, too.

