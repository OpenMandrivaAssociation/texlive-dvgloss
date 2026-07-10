%global tl_name dvgloss
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Facilities for setting interlinear glossed text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dvgloss
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvgloss.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides extensible macros for setting interlinear glossed
text -- useful, for instance, for typing linguistics papers. The
operative word here is "extensible": few features are built in, but some
flexible and powerful facilities are included for adding your own.

