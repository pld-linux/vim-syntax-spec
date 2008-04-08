Summary:	Vim syntax: RPM specfiles
Name:		vim-syntax-spec
Version:	1.80
Release:	2
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	spec.vim
Source1:	vim-ftplugin-spec.vim
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
Obsoletes:	vim-ftplugin-spec
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define		syntax spec

%description
This plugin provides syntax highlighting for RPM spec files.

%prep
%setup -qcT
rev=$(awk '/^".*Version:.*Revision:/{print $4}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftplugin}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/spec.vim
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin/spec.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/spec.vim
%{_vimdatadir}/ftplugin/spec.vim
