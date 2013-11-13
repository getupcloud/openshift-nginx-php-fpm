%global cartridgedir %{_libexecdir}/openshift/cartridges/nginx-php-fpm
%global frameworkdir %{_libexecdir}/openshift/cartridges/nginx-php-fpm

Name:          openshift-cartridge-nginx-php-fpm
Version:       0.0.0.3
Release:       1%{?dist}
Summary:       Php-fpm cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://getupcloud.com
Source0:       https://github.com/getupcloud/origin-server/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      php >= 5.3.2
Requires:      php < 5.4
Requires:      httpd < 2.4
Requires:      php
Requires:      php-devel
Requires:      php-pdo
Requires:      php-gd
Requires:      php-xml
Requires:      php-mysql
Requires:      php-pecl-mongo
Requires:      php-pgsql
Requires:      php-mbstring
Requires:      php-pear
Requires:      php-imap
Requires:      php-pecl-apc
Requires:      php-mcrypt
Requires:      php-soap
Requires:      php-bcmath
Requires:      php-process
Requires:      php-pecl-imagick
Requires:      php-pecl-xdebug
BuildArch:     noarch
# php-5.4 scl
Requires:      php54-php-pdo
Requires:      php54-php-pecl-amqp
Requires:      php54-php-enchant
Requires:      php54-php-pecl-igbinary-devel
Requires:      php54-php
Requires:      php54-php-dba
Requires:      php54-php-twig-CTwig
Requires:      php54-php-xml
Requires:      php54-php-pspell
Requires:      php54-php-interbase
Requires:      php54-php-pecl-ssh2
Requires:      php54-php-pecl-xdebug
Requires:      php54-php-pear
Requires:      php54-php-gd
Requires:      php54-php-snmp
Requires:      php54-php-imap
Requires:      php54-php-pecl-geoip
Requires:      php54-php-ldap
Requires:      php54-php-pecl-zendopcache
Requires:      php54-php-cli
Requires:      php54-php-devel
Requires:      php54-php-pecl-apcu >= 4.0
Requires:      php54-php-tidy
Requires:      php54-php-pecl-sphinx
Requires:      php54-php-pecl-rrd
Requires:      php54-php-recode
Requires:      php54-php-pecl-redis
Requires:      php54-php-odbc
Requires:      php54-php-pecl-xhprof
Requires:      php54-php-intl
Requires:      php54-php-fpm
Requires:      php54-php-pecl-mongo
Requires:      php54-php-xmlrpc
Requires:      php54-php-soap
Requires:      php54-php-process
Requires:      php54-php-pecl-igbinary
Requires:      php54-php-pecl-msgpack
Requires:      php54-php-pecl-mailparse
Requires:      php54-php-pecl-gearman
Requires:      php54-php-pecl-radius
Requires:      php54-php-mbstring
Requires:      php54-php-pecl-msgpack-devel
Requires:      php54-php-pecl-apcu-devel >= 4.0
Requires:      php54-php-mysqlnd
Requires:      php54-php-mcrypt
Requires:      php54-php-pecl-imagick
Requires:      php54-php-common
Requires:      php54-php-pecl-http1
Requires:      php54-php-mssql
Requires:      php54-php-pecl-http1-devel
Requires:      php54-php-pgsql
Requires:      php54-php-pecl-memcache
Requires:      php54-php-bcmath
# php-5.5 scl
Requires:      php55-php-pdo
Requires:      php55-php-pecl-mailparse
Requires:      php55-php-mssql
Requires:      php55-php-pecl-imagick
Requires:      php55-php-mcrypt
Requires:      php55-php-intl
Requires:      php55-php-tidy
Requires:      php55-php-common
Requires:      php55-php-pecl-http1
Requires:      php55-php-pecl-redis
Requires:      php55-php-pecl-ssh2
Requires:      php55-php-pecl-xhprof
Requires:      php55-php-dba
Requires:      php55-php-fpm
Requires:      php55-php-pear
Requires:      php55-php-pecl-msgpack
Requires:      php55-php-pgsql
Requires:      php55-php-pecl-rrd
Requires:      php55-php-pecl-sphinx
Requires:      php55-php-gmp
Requires:      php55-php-bcmath
Requires:      php55-php-cli
Requires:      php55-php-pecl-jsonc
Requires:      php55-php-devel
Requires:      php55-php-mbstring
Requires:      php55-php-pecl-apcu-devel >= 4.0
Requires:      php55-php-odbc
Requires:      php55-php-pecl-mongo
Requires:      php55-php-pecl-xdebug
Requires:      php55-php-pecl-amqp
Requires:      php55-php-pecl-gearman
Requires:      php55-php-recode
Requires:      php55-php-opcache
Requires:      php55-php-enchant
Requires:      php55-php-snmp
Requires:      php55-php-xml
Requires:      php55-php-pecl-apcu >= 4.0
Requires:      php55-php-pecl-igbinary-devel
Requires:      php55-php-pecl-geoip
Requires:      php55-php-pecl-memcache
Requires:      php55-php
Requires:      php55-php-gd
Requires:      php55-php-pecl-igbinary
Requires:      php55-php-pecl-msgpack-devel
Requires:      php55-php-mysqlnd
Requires:      php55-php-pecl-radius
Requires:      php55-php-xmlrpc
Requires:      php55-php-ldap
Requires:      php55-php-pspell
Requires:      php55-php-process
Requires:      php55-php-pecl-jsonc-devel
Requires:      php55-php-pecl-http1-devel
Requires:      php55-php-interbase
Requires:      php55-php-twig-CTwig
Requires:      php55-php-imap
Requires:      php55-php-soap

#Obsoletes: openshift-origin-cartridge-php-5.3

%description
PHP-FPM cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{cartridgedir}/versions/shared/configuration/etc/conf/

%files
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md


%changelog
* Wed Nov 13 2013 Getup Builder <getup@getupcloud.com> 0.0.0.3-1
- new package built with tito

* Wed Nov 13 2013 Getup Builder <getup@getupcloud.com> 0.0.0.2-1
- new package built with tito

