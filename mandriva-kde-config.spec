%define epoch_kdelibs 30000000
%define source_date 20080201

Name: mandriva-kde-config
Summary: Mandriva KDE configuration 
Version: 2008.1
Release: %mkrel 7
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
Source0: %{name}-%{version}.%{source_date}.tar.bz2
License: GPL
BuildArch: noarch

%description
This package regroups all specific Mandriva config file for KDE.
(kicker config etc.)

#--------------------------------------------------------------------

%package common
Group: Graphical desktop/KDE
Summary: Common configs used for Mandriva theme
Requires(pre): update-alternatives
Requires: urw-fonts

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

#--------------------------------------------------------------------

%package -n powerpack-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Obsoletes: powerpackplus-kde-config < 2008.0 
Provides: powerpackplus-kde-config = %version-%release
Requires(preun): mandriva-kde-config-common

%pre -n powerpack-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop
fi

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

%package -n one-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common

%description -n one-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n one-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop
fi

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


#--------------------------------------------------------------------

%package -n flash-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common

%description -n flash-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n flash-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop
fi

%post -n flash-kde-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/mandriva/kde-profiles/flash/kderc 10

%postun -n flash-kde-config
if ! [ -e /var/lib/mandriva/kde-profiles/flash/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/flash/kderc
fi

%files -n flash-kde-config
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/kde-profiles/flash
%_localstatedir/mandriva/kde-profiles/flash/*


#--------------------------------------------------------------------

%package -n free-kde-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde-config-common
Obsoletes: download-kde-config-2007 < 2008.0 
Provides:	download-kde-config-2007
Obsoletes: discovery-kde-config < 2008.0
Provides: discovery-kde-config = %version-%release

%description -n free-kde-config
This package regroups all specific Mandriva config file for KDE.

%pre -n free-kde-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop
fi

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


#--------------------------------------------------------------------
# KDM

%package -n mandriva-kdm-config
Summary: Mandriva KDM config file
Group: Graphical desktop/KDE
Obsoletes: kdebase-kdm-config-file < 2008.0
Provides: kdm-config-file = %version-%release
# For upgrade 
Provides: kdebase-kdm-config-file = 2:%version 
Conflicts: kdebase-progs <= 3.5.1-15.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
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
%config(noreplace) %_sysconfdir/kde/kdm/backgroundrc
%config(noreplace) %_sysconfdir/kde/kdm/kdmrc
%_sysconfdir/kde/kdm/themes

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

for name in flash free one powerpack; do
    echo "[Directories-default]" > %buildroot%_localstatedir/mandriva/kde-profiles/$name/kderc
    echo "prefixes=/var/lib/mandriva/kde-profiles/common,%_localstatedir/mandriva/kde-profiles/$name" >> %buildroot%_localstatedir/mandriva/kde-profiles/$name/kderc
	# create the symlink to the desktop data
    mkdir -p %buildroot%_localstatedir/mandriva/kde-profiles/$name/share/apps/kdesktop
    ln -s %_datadir/mdk/desktop/$name %buildroot%_localstatedir/mandriva/kde-profiles/$name/share/apps/kdesktop/DesktopLinks
done

# Upstream
echo "[Directories-default]" > %buildroot%_localstatedir/mandriva/kde-profiles/common/upstream-kde-config
echo "prefixes=/etc/kde" >> %buildroot%_localstatedir/mandriva/kde-profiles/common/upstream-kde-config


%clean
rm -rf %buildroot
