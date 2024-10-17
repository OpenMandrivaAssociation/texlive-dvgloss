Name:		texlive-dvgloss
Version:	29103
Release:	2
Summary:	Facilities for setting interlinear glossed text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dvgloss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides extensible macros for setting interlinear
glossed text -- useful, for instance, for typing linguistics
papers. The operative word here is "extensible": few features
are built in, but some flexible and powerful facilities are
included for adding your own.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dvgloss/dvgloss.sty
%doc %{_texmfdistdir}/doc/latex/dvgloss/README
%doc %{_texmfdistdir}/doc/latex/dvgloss/dvgloss.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dvgloss/dvgloss.dtx
%doc %{_texmfdistdir}/source/latex/dvgloss/dvgloss.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
