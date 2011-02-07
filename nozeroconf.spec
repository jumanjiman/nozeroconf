%global network_global_config /etc/sysconfig/network

Name:		nozeroconf
Version:	0.1
Release:	1%{?dist}
Summary:	Disables Zeroconf networking

Group:		System Environment/Base
License:	GPLv3+
URL:		https://github.com/jumanjiman/nozeroconf
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	%{network_global_config}
Requires:	sed

%description
Install this package to disable zeroconf networking.

For more information about zeroconf, see:
http://www.zeroconf.org/


%prep
%setup -q


%build


%install
%{__rm} -rf %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPLv3


%preun
if [ $1 -eq 0 ]; then
  sed -i '/^NOZEROCONF.*/d' %{network_global_config}
fi


%post
if [ $1 -gt 0 ]; then
  . %{network_global_config} || exit 1
  if [[ -z ${NOZEROCONF} ]]; then
    echo 'NOZEROCONF=disabled' >> %{network_global_config}
  fi
fi


%changelog
* Mon Feb 07 2011 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- new package built with tito


