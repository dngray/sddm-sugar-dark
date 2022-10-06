%global srcname copr-sddm-sugar-dark
%global commit ceb2c455663429be03ba62d9f898c571650ef7fe
%global commitdate 20220724
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: sddm-sugar-dark
Version: 1.2^%{commitdate}.%{shortcommit}
Release: 0%{?dist}
License: GPLv3
Summary: The sweetest dark theme around for SDDM, the Simple Desktop Display Manager.
URL: https://github.com/MarianArlt/%{name}
Source0: %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch: noarch

Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols2
Requires: qt5-qtsvg
Requires: sddm

%description
Sugar is extremely customizable and so sweet it will probably cause you
diabetes just from looking at it. Sweeten the login experience for your users,
your family and yourself. Sugar is cross platform and all about user experience
and functionality.

With those principles in mind Sugar was written completely from scratch making
it clean and simple not only by looks but by design too.

All controls use the latest Qt Quick Controls 2 for increased performance on
low end or even embedded systems.

%prep
%setup -n %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/sugar-dark
cp -ar {Assets,Components,Background.jpg,Illustration.svg,Main.qml,metadata.desktop} \
        %{buildroot}%{_datadir}/sddm/themes/sugar-dark
cp theme.conf %{buildroot}%{_datadir}/sddm/themes/sugar-dark/theme.conf

%files
%license COPYING
%doc AUTHORS
%doc CHANGELOG.md
%doc CREDITS
%doc README.md
%{_datadir}/sddm/themes/sugar-dark

%changelog
