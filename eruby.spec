Summary:	Embedded Ruby
Name:		eruby
Version:	1.0.5
Release:	%mkrel 6
# eruby is GPLv2+, liberuby is LGPLv2
License:	GPLv2+ and LGPLv2+
Group:		Development/Other
URL:		https://www.modruby.net/en/index.rbx/eruby/whatis.html
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}
BuildRequires:	ruby-devel
Requires:	ruby

%define ruby_libdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")

%description
eRuby (embedded Ruby) interprets a Ruby code embedded text file. For example,
eRuby enables you to embed a Ruby code to a HTML file.

%prep
%setup -q -n %{name}-%{version}

%build
./configure.rb \
    --prefix=%{_prefix} \
    --datadir=%{_datadir} \
    --mandir=%{buildroot}%{_mandir} 
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} site-install
chmod 755 %{buildroot}/%{ruby_archdir}/eruby.so
strip %{buildroot}/%{ruby_archdir}/eruby.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/eruby
%{_includedir}/eruby.h
%{_libdir}/liberuby.*
%{ruby_archdir}/eruby.*
%{_mandir}/*/*
%doc ChangeLog COPYING README.* examples

