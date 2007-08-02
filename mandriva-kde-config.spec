%define epoch_kdelibs 30000000
%define source_date 20070802

Name: mandriva-kde-config
Summary: Mandriva KDE configuration 
Version: 2008.0
Release: %mkrel 4
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
Source0: %{name}-%{version}.%{source_date}.tar.bz2
Source2: mdv-startup.wav
Source3: buyit.desktop
Source4: subscribe.desktop
Source5: jam.desktop
License: GPL
BuildArch: noarch

%description
This package regroups all specific Mandriva config file for KDE.
(kicker config etc.)

#--------------------------------------------------------------------

%package common
Group: Graphical desktop/KDE
Summary: common configs used for Mandriva theme
Requires(pre): update-alternatives

%description common
common configs used for Mandriva theme

%post common
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/common/upstream-kde-config 9

%postun common
if ! [ -e /var/lib/mandriva/kde-profiles/common/upstream-kde-config ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/common/upstream-kde-config
fi

%files common
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/
%dir %_localstatedir/mandriva/kde-profiles/common
%_localstatedir/mandriva/kde-profiles/common/*
%_datadir/sounds/mdv-startup.wav
%_datadir/services/searchproviders/jam.desktop

#--------------------------------------------------------------------

%package -n discovery-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: mandriva-kde-icons
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(preun): mandriva-kde-config-common

%description -n discovery-kde-config
This package regroups all specific Mandriva config file for KDE.

%post -n discovery-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/discovery/kderc 10

%postun -n discovery-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/discovery/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/discovery/kderc
fi

%files -n discovery-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/discovery
%_localstatedir/mandriva/kde-profiles/discovery/*

#--------------------------------------------------------------------

%package -n powerpack-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: mandriva-kde-icons
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(preun): mandriva-kde-config-common

%post -n powerpack-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/powerpack/kderc 10

%postun -n powerpack-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/powerpack/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/powerpack/kderc
fi

%description -n powerpack-kde-config
This package regroups all specific Mandriva config file for KDE.

%files -n powerpack-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/powerpack
%_localstatedir/mandriva/kde-profiles/powerpack/*

#--------------------------------------------------------------------

%package -n powerpackplus-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: mandriva-kde-icons
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(preun): mandriva-kde-config-common

%description -n powerpackplus-kde-config
This package regroups all specific Mandriva config file for KDE.

%post -n powerpackplus-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/powerpackplus/kderc 10

%postun -n powerpackplus-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/powerpackplus/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/powerpackplus/kderc
fi

%files -n powerpackplus-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/powerpackplus
%_localstatedir/mandriva/kde-profiles/powerpackplus/*

#--------------------------------------------------------------------

%package -n one-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: mandriva-kde-icons
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(preun): mandriva-kde-config-common

%description -n one-kde-config
This package regroups all specific Mandriva config file for KDE.

%post -n one-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/one/kderc 10

%postun -n one-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/one/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/one/kderc
fi

%files -n one-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/one
%_localstatedir/mandriva/kde-profiles/one/*

%_datadir/apps/kdesktop/DesktopLinks/*.desktop

#--------------------------------------------------------------------

%package -n free-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: mandriva-kde-icons
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(preun): mandriva-kde-config-common
Obsoletes: download-kde-config-2007 <= 18mdv2007.0 
Provides:	download-kde-config-2007

%description -n free-kde-config
This package regroups all specific Mandriva config file for KDE.

%post -n free-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/free/kderc 10

%postun -n free-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/free/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/free/kderc
fi

%files -n free-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/free
%_localstatedir/mandriva/kde-profiles/free/*

%_datadir/apps/kdesktop/DesktopLinks/*.desktop

#--------------------------------------------------------------------
# KDM

%package -n mandriva-kdm-config
Summary: Mandriva KDM config file
Group: Graphical desktop/KDE
Obsoletes: kdebase-kdm-config-file
Provides: kdm-config-file = %version-%release
# For upgrade 
Provides: kdebase-kdm-config-file = 2:%version 
Conflicts: kdebase-progs <= 3.5.1-15.1.20060mdk
Obsoletes: mandriva-kde-config-file
Requires(post): perl-MDK-Common

%description -n mandriva-kdm-config
Mandriva KDM config file

%trigger -n mandriva-kdm-config -- kdebase-kdm-config-file 
perl -MMDK::Common -e 'update_gnomekderc("/etc/kde/kdm/kdmrc", "General", "ConsoleTTYs", "tty1,tty2,tty3,tty4,tty5,tty6", "ServerVTs", "-7")'

%pre -n mandriva-kdm-config
if [ ! -h "%_datadir/config" ]; then
   [ ! -d "%_sysconfdir/kde" ] && mkdir -p %_sysconfdir/kde
   cp -arf %_datadir/config/* %_sysconfdir/kde/
   rm -rf %_datadir/config
   ln -s %_sysconfdir/kde %_datadir/config   
fi

%posttrans -n mandriva-kdm-config
# Test if the rpm bug was not triggered
cd %_sysconfdir/kde/kdm
if [ ! -f kdmrc -a -f kdmrc.rpmsave ]; then
   mv kdmrc.rpmsave kdmrc
fi
if [ ! -f backgroundrc -a -f backgroundrc.rpmsave ]; then
   mv backgroundrc.rpmsave backgroundrc
fi

%files -n mandriva-kdm-config
%defattr(0644,root,root,0755)
%config(noreplace) %_sysconfdir/kde/kdm

#---------------------------------------

%prep
%setup -q

%install
rm -rf %buildroot
# Create profile dirs
mkdir -p %buildroot/%_sysconfdir/kde
mkdir -p %buildroot/%_localstatedir/mandriva

mv kde-profiles %buildroot/%_localstatedir/mandriva
mv kdm %buildroot/%_sysconfdir/kde

install -d -m 0755 %buildroot/%_datadir/sounds/
install -m 0644 %SOURCE2 %buildroot/%_datadir/sounds/

install -d -m 0755 %buildroot/%_datadir/apps/kdesktop/DesktopLinks
install -m 0644 %SOURCE3 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/
install -m 0644 %SOURCE4 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/

install -d -m 0755 %buildroot/%_datadir/services/searchproviders/
install -m 0644 %SOURCE5 %buildroot/%_datadir/services/searchproviders/


for name in discovery free one powerpack powerpackplus; do
    echo "[Directories-default]" > %buildroot%_localstatedir/mandriva/kde-profiles/$name/kderc
    echo "prefixes=/var/lib/mandriva/kde-profiles/common,%_localstatedir/mandriva/kde-profiles/$name" >> %buildroot%_localstatedir/mandriva/kde-profiles/$name/kderc
done

# Upstream
echo "[Directories-default]" > %buildroot%_localstatedir/mandriva/kde-profiles/common/upstream-kde-config
echo "prefixes=/etc/kde" >> %buildroot%_localstatedir/mandriva/kde-profiles/common/upstream-kde-config

%clean
rm -rf %buildroot



