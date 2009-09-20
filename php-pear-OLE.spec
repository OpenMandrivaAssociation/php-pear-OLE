%define		_class		OLE
%define		_status		beta
%define		_pearname	%{_class}
%define		pre       RC1

Summary:	%{_pearname} - package for reading and writing OLE containers
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	%mkrel 0.%{pre}.1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{pre}.tgz
URL:		http://pear.php.net/package/OLE/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package allows reading and writing of OLE (Object Linking and
Embedding) files, the format used as container for Excel, Word and
other MS file formats. Documentation for the OLE format can be found
at: http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html .

In PEAR status of this package is: %{_status}.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/
install -m 644 %{_pearname}-%{version}%{pre}/%{_class}.php \
    %{buildroot}%{_datadir}/pear

install -d %{buildroot}%{_datadir}/pear/%{_class}
install -m 644 %{_pearname}-%{version}%{pre}/PPS.php \
    %{buildroot}%{_datadir}/pear/%{_class}
install -m 644 %{_pearname}-%{version}%{pre}/ChainedBlockStream.php \
    %{buildroot}%{_datadir}/pear/%{_class}

install -d %{buildroot}%{_datadir}/pear/%{_class}/PPS
install -m 644 %{_pearname}-%{version}%{pre}/PPS/*.php \
    %{buildroot}%{_datadir}/pear/%{_class}/PPS

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{_pearname}.xml


