%define epoch_kdelibs 30000000
%define source_date 20070405

Name: mandriva-kde-config
Summary: Mandriva KDE configuration 
Version:	2007.1
Release:	%mkrel 25
URL: http://www.mandriva.com
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-buildroot
Source0: %{name}-%{version}.%{source_date}.tar.bz2
Source1: updatekdeprofile
Source2:	mdv-startup.wav
Source3:	buyit.desktop
Source4:	subscribe.desktop
Source5:	jam.desktop
License:	GPL
BuildArch: noarch

%description
This package regroups all specific Mandriva config file for KDE.
(kicker config etc.)

#--------------------------------------------------------------------

%package common
Group: Graphical desktop/KDE
Summary: common configs used for Mandriva theme

%description common
common configs used for Mandriva theme

%files common
%defattr(0644,root,root,755)
%dir %_localstatedir/mandriva/
%dir %_localstatedir/mandriva/kde-profiles/common
%_localstatedir/mandriva/kde-profiles/common/*
%attr(0755,root,root) %_bindir/updatekdeprofile
%config(noreplace ) %_sysconfdir/kderc
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

%posttrans -n discovery-kde-config
updatekdeprofile --add %_localstatedir/mandriva/kde-profiles/discovery

%preun -n discovery-kde-config
if [ -x /usr/bin/updatekdeprofile ]; then
	updatekdeprofile --remove %_localstatedir/mandriva/kde-profiles/discovery
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

%description -n powerpack-kde-config
This package regroups all specific Mandriva config file for KDE.

%posttrans -n powerpack-kde-config
updatekdeprofile --add %_localstatedir/mandriva/kde-profiles/powerpack

%preun -n powerpack-kde-config
if [ -x /usr/bin/updatekdeprofile ]; then
	updatekdeprofile --remove %_localstatedir/mandriva/kde-profiles/powerpack
fi

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

%posttrans -n powerpackplus-kde-config
updatekdeprofile --add %_localstatedir/mandriva/kde-profiles/powerpackplus

%preun -n powerpackplus-kde-config
if [ -x /usr/bin/updatekdeprofile ]; then
	updatekdeprofile --remove %_localstatedir/mandriva/kde-profiles/powerpackplus
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

%posttrans -n one-kde-config
updatekdeprofile --add %_localstatedir/mandriva/kde-profiles/one

%preun -n one-kde-config
if [ -x /usr/bin/updatekdeprofile ]; then
	updatekdeprofile --remove %_localstatedir/mandriva/kde-profiles/one
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

%posttrans -n free-kde-config
updatekdeprofile --add %_localstatedir/mandriva/kde-profiles/free

%preun -n free-kde-config
if [ -x /usr/bin/updatekdeprofile ]; then
	updatekdeprofile --remove %_localstatedir/mandriva/kde-profiles/free
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

# kdm migration
install -d -m 0755 %buildroot/%_bindir

# updatekdeprofiles
install -m 0755 %SOURCE1 %buildroot/%_bindir/updatekdeprofile

install -d -m 0755 %buildroot/%_datadir/sounds/
install -m 0644 %SOURCE2 %buildroot/%_datadir/sounds/

install -d -m 0755 %buildroot/%_datadir/apps/kdesktop/DesktopLinks
install -m 0644 %SOURCE3 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/
install -m 0644 %SOURCE4 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/

install -d -m 0755 %buildroot/%_datadir/services/searchproviders/
install -m 0644 %SOURCE5 %buildroot/%_datadir/services/searchproviders/

# We symlink all not specific configs from common
CFGDIR="%_localstatedir/mandriva/kde-profiles"
pushd %buildroot/${CFGDIR}
for config in discovery powerpack powerpackplus one free; do
   pushd common
      find . -type d -exec mkdir -p ../${config}/{} \;
   popd
   find common -type f | while read common; do
      dest=`echo ${common} | sed "s,common,${config},g"`
      [ ! -f "$dest" ] && ln -sf "$CFGDIR/$common" "$dest"
   done
done

# Create empty kderc
install -d 0755 %buildroot/%_sysconfdir/
cat << EOF > %buildroot/%_sysconfdir/kderc
[Directories-default]
prefixes=
EOF
chmod 0644 %buildroot/%_sysconfdir/kderc


%clean
rm -rf %buildroot



