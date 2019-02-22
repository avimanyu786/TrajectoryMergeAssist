#!/bin/sh
# TrajectoryMergeAssist Setup v1.1
# A setup tool to easily install TrajectoryMergeAssist v2.1

# Copyright (C) 2019 Avimanyu Bandyopadhyay

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

DISTRO=$( cat /etc/*-release | tr [:upper:] [:lower:] | grep -Poi '(debian|centos|fedora|rhel)' | uniq )

if [ $DISTRO = 'centos' ] || [ $DISTRO = 'fedora' ] || [ $DISTRO = 'rhel' ]; 
then
	su -c 'yum update'
	su -c 'yum install tkinter'
elif [ $DISTRO = 'debian' ];
then
	sudo apt update
	sudo apt install python-tk
else
	echo $DISTRO 'Linux Distribution not supported'
fi
	
cd ~
echo 'Downloading TrajectoryMergeAssist...'
wget https://github.com/avimanyu786/TrajectoryMergeAssist/releases/download/v2.1/tma_v2.1.tar.gz
tar xvzf tma_v2.1.tar.gz
echo 'Setting Paths...'
echo '----------------'
echo 'export TMAPATH=$HOME/tma_v2.1/bin' >> ~/.bashrc
echo 'export PATH=$PATH:$TMAPATH' >> ~/.bashrc
echo 'Reloading BASH...'
. ~/.bashrc
echo '----------------------'
echo 'Installation Complete!'
echo '----------------------'
echo 'You can now run TrajectoryMergeAssist v2.1 with command "tma".'

