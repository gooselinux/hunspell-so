Name: hunspell-so
Summary: Somali hunspell dictionaries
Version: 0.1.2
Release: 2.1%{?dist}
Group: Applications/Text
Source: http://www.opensourcesomalia.org/uploads/so-SO@dictionaries.addons.mozilla.org3.xpi
URL: http://www.opensourcesomalia.org/index.php?page=hingaad-saxe
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
Requires: hunspell

%description
Somali hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/so-SO.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/so_SO.aff
cp -p dictionaries/so-SO.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/so_SO.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
so_SO_aliases="so_DJ so_ET so_KE"
for lang in $so_SO_aliases; do
        ln -s so_SO.aff $lang.aff
        ln -s so_SO.dic $lang.dic
done
popd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc xuquuqda/*
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1.2-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.1.2-1
- initial version
