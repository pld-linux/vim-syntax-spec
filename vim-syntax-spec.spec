Summary:	Vim syntax: RPM specfiles
Summary(pl.UTF-8):	Składania dla Vima: pliki RPM spec
Name:		vim-syntax-spec
Version:	1.131
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	spec.vim
Source1:	vim-ftplugin-spec.vim
Conflicts:	rpm-build-tools < 4.4.36-2
# for extended % matching
Suggests:	vim-plugin-matchit
# for diffcol
Suggests:	rpmbuild(macros)
Conflicts:	rpmbuild(macros) < 1.665
# for _vimdatadir existence
Requires:	vim-rt >= 4:7.2.170
Obsoletes:	vim-ftplugin-spec < 0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
This plugin provides syntax highlighting for RPM spec files.

%description -l pl.UTF-8
Ta wtyczka zapewnia podświetlanie składni plików RPM spec.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftplugin}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/spec.vim
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin/spec.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/spec.vim
%{_vimdatadir}/ftplugin/spec.vim
