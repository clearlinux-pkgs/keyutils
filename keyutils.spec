#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyutils
Version  : 1.5.9
Release  : 9
URL      : http://people.redhat.com/~dhowells/keyutils/keyutils-1.5.9.tar.bz2
Source0  : http://people.redhat.com/~dhowells/keyutils/keyutils-1.5.9.tar.bz2
Summary  : Linux Key Management Utilities
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.0+ LGPL-2.1+
Requires: keyutils-bin
Requires: keyutils-lib
Requires: keyutils-data
Requires: keyutils-doc
BuildRequires : libc-bin
Patch1: stateless.patch

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to user space to get a key
instantiated.

%package bin
Summary: bin components for the keyutils package.
Group: Binaries
Requires: keyutils-data

%description bin
bin components for the keyutils package.


%package data
Summary: data components for the keyutils package.
Group: Data

%description data
data components for the keyutils package.


%package dev
Summary: dev components for the keyutils package.
Group: Development
Requires: keyutils-lib
Requires: keyutils-bin
Requires: keyutils-data

%description dev
dev components for the keyutils package.


%package doc
Summary: doc components for the keyutils package.
Group: Documentation

%description doc
doc components for the keyutils package.


%package lib
Summary: lib components for the keyutils package.
Group: Libraries
Requires: keyutils-data

%description lib
lib components for the keyutils package.


%prep
%setup -q -n keyutils-1.5.9
%patch1 -p1

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install LIBDIR=%{_libdir} USRLIBDIR=%{_libdir}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/key.dns_resolver
/usr/bin/keyctl
/usr/bin/request-key

%files data
%defattr(-,root,root,-)
/usr/share/keyutils/request-key-debug.sh
/usr/share/keyutils/request-key.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
