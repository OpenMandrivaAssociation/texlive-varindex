Name:		texlive-varindex
Version:	32262
Release:	1
Summary:	Luxury frontend to the \index command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/varindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/varindex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a convenient front-end for the \index command. For
example, with it you can generate multiple index entries in
almost any form by a single command. The package is highly
customizable, and works with all versions of LaTeX and probably
most other TeX formats.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/varindex/varindex.sty
%doc %{_texmfdistdir}/doc/latex/varindex/README
%doc %{_texmfdistdir}/doc/latex/varindex/varindex.pdf
%doc %{_texmfdistdir}/doc/latex/varindex/varindex.tex
%doc %{_texmfdistdir}/doc/latex/varindex/varindex.txt
#- source
%doc %{_texmfdistdir}/source/latex/varindex/varindex.dtx
%doc %{_texmfdistdir}/source/latex/varindex/varindex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
