%global tl_name varindex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Luxury frontend to the \index command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/varindex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a convenient front-end for the \index command. For example,
with it you can generate multiple index entries in almost any form by a
single command. The package is highly customizable, and works with all
versions of LaTeX and probably most other TeX formats.

