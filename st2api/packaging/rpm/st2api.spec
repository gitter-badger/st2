Summary: Stanley API
Name: st2api
Version: 0.4.0
Release: 1
License: license
Group: Applications/Engineering
BuildArch: noarch
Source: /opt/git/stanley/st2api.tar.gz
URL: https://github.com/StackStorm/stanley
Vendor: StackStorm
Packager: Stormin Stanley <stanley@stackstorm.com>
Requires:       st2common

%description
An automation plaform that needs a much better description than this.

%prep
%setup

%build
sed -i -r "s~logs~/var/log/stanley~g" conf/logging.conf

%install

mkdir -p %{buildroot}/etc/st2api
mkdir -p %{buildroot}%{python2_sitelib}
mkdir -p %{buildroot}/usr/bin
cp -R st2api %{buildroot}%{python2_sitelib}/
cp -R conf/* %{buildroot}/etc/st2api
install -m755 bin/st2api %{buildroot}/usr/bin/st2api

%files

/usr/lib/python2.7/site-packages/st2api*
/usr/bin/st2api
/etc/st2api*