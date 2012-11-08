Summary:	Vim syntax: RPM specfiles
Summary(pl.UTF-8):	Składania dla Vima: pliki RPM spec
Name:		vim-syntax-spec
Version:	1.122
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	spec.vim
Source1:	vim-ftplugin-spec.vim
# 4.4.35 is broken
Conflicts:	rpm-build-tools < 4.4.36-2
# for diffcol
Suggests:	rpmbuild(macros)
Conflicts:	rpmbuild(macros) < 1.322
# for _vimdatadir existence
Requires:	vim-rt >= 4:7.2.170
Obsoletes:	vim-ftplugin-spec
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
This plugin provides syntax highlighting for RPM spec files.

%description -l pl.UTF-8
Ta wtyczka zapewnia podświetlanie składni plików RPM spec.

%prep
%setup -qcT
rev=$(awk '/^".*Version:.*/{print $3}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

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
