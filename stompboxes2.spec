%define name	stompboxes2
%define version 0.3
%define release 2mdk

Summary:	This is Stompboxes2, a real-time audio effects processor.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://mrbook.org/stompboxes/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}16.png
Source2:	%{name}32.png
Source3:	%{name}48.png
Patch0:		stompboxes2-0.3-misc_fixes.patch.bz2
Requires:	libgtk+1.2
BuildRequires:	libgtk+1.2-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
StompBoxes is a real-time audio effects processor designed
for guitar under Linux. It is written in C using gtk+ for the
graphical user interface. The sound is processed in 16 bit
at a rate of 44100Hz.

So you want to try stompboxes2 ?? Ok, but be warned the immature
stage of the project might turn your speakers into the most
annoying noise making maCHine that ever existed.

%prep

%setup -q
%patch0 -p1

%build

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}
install -d %{buildroot}%{_menudir}

# Icons
install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

# Menu
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}): needs="x11" \\
section="Multimedia/Sound" \\
title="StompBoxes" \\
longtitle="%{summary}" \\
command="%{name}" \\
icon="%{name}.png"
?package(%{name}): needs="x11" \\
section="Documentation" \\
title="StompBoxes" \\
longtitle="StompBoxes" \\
command="if ps U \$USER | grep -q \$BROWSER; then \$BROWSER -remote \'openURL(%{url})\'; else \$BROWSER \'%{url}\'; fi" \\
icon="%{name}.png"
EOF

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,755)
%doc ChangeLog LOG README doc/QUICKSTART
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

