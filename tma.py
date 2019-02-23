# TrajectoryMergeAssist v2.1
# A python based GUI tool that helps in merging two trajectories on Desmond MD

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

import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw()


class MergeMDs(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self, text='Browse Desmond "-out.cms" file', command=self.AskDesmondInputFile)
        button.grid(column=0, row=1)

        button2 = Tkinter.Button(self, text='Choose Desmond Trajectory 1', command=self.AskDesmondTrajectory1)
        button2.grid(column=0, row=2)

        button3 = Tkinter.Button(self, text='Choose Desmond Trajectory 2', command=self.AskDesmondTrajectory2)
        button3.grid(column=0, row=3)

        button4 = Tkinter.Button(self, text='Merge Desmond Trajectories', command=self.MergeDesmondTrajectories)
        button4.grid(column=0, row=4)

        button5 = Tkinter.Button(self, text='Browse GROMACS Trajectory 1 ".xtc" file', command=self.AskGROMACSTrajectory1)
        button5.grid(column=1, row=1)

        button6 = Tkinter.Button(self, text='Browse GROMACS Trajectory 2 ".xtc" file', command=self.AskGROMACSTrajectory2)
        button6.grid(column=1, row=2)

        button7 = Tkinter.Button(self, text='Merge GROMACS Trajectories', command=self.MergeGROMACSTrajectories)
        button7.grid(column=1, row=3)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.update()
        self.geometry("490x120")

    def AskDesmondInputFile(self):
        
        global cms
        cms = tkFileDialog.askopenfilename(parent=root, initialdir="pwd", title='Choose -out.cms file')
        if len(cms) > 0:
            print "%s selected" % cms

    def AskDesmondTrajectory1(self):

        global in1_trj
        in1_trj = tkFileDialog.askdirectory(parent=root, initialdir="pwd", title='Please Select Desmond Trajectory 1')
        if len(in1_trj) > 0:
            print "You chose %s" % in1_trj

    def AskDesmondTrajectory2(self):

        global in2_trj
        in2_trj = tkFileDialog.askdirectory(parent=root, initialdir="pwd", title='Please Select Desmond Trajectory 2')
        if len(in2_trj) > 0:
            print "You chose %s" % in2_trj

    def MergeDesmondTrajectories(self):

        if os.path.exists(os.path.expandvars("$SCHRODINGER")):
            print "\t"
            os.system("echo You are using Desmond MD via $SCHRODINGER")
            print "\t"
        else:
            print "Desmond MD not installed or $SCHRODINGER path not set correctly. Exiting..."
            exit()

        print "-------------------------------------------------------------"
        print "Merging both trajectories into one and generating -out.cms..."
        print "-------------------------------------------------------------"

        # For Desmond Version >= 2018.1 https://www.schrodinger.com/kb/282357

        if os.path.exists(os.path.expandvars("$SCHRODINGER/internal/bin/trj_merge.py")):
            os.system("$SCHRODINGER/run trj_merge.py %s %s %s -o NewMergedTrajectory" % (
            cms, in1_trj, in2_trj))
            os.system("mv NewMergedTrajectory.cms NewMergedTrajectory-out.cms")
            
        else:  # For Desmond Version < 2018.1 https://www.schrodinger.com/kb/90
            os.system("$SCHRODINGER/run -FROM desmond manipulate_trj.py %s NewMergedTrajectory %s %s" % (
            cms, in1_trj, in2_trj))
        
        if os.path.exists("NewMergedTrajectory-out.cms"):
            print "...Done!" 
            print "Check your current working directory for new merged trajectory and -out.cms file."
            print "Thank you for using TrajectoryMergeAssist."
            print "\t"
        else:
            print "Error! New Merged Trajectory not created! Please contact author."
            print "\t"

        exit()

    def AskGROMACSTrajectory1(self):

        global xtc1
        xtc1 = tkFileDialog.askopenfilename(parent=root, initialdir="pwd", title='Please Select GROMACS Trajectory 1 .xtc file')
        if len(xtc1) > 0:
            print "You chose %s" % xtc1

    def AskGROMACSTrajectory2(self):

        global xtc2
        xtc2 = tkFileDialog.askopenfilename(parent=root, initialdir="pwd", title='Please Select GROMACS Trajectory 2 .xtc file')
        if len(xtc2) > 0:
            print "You chose %s" % xtc2

    def MergeGROMACSTrajectories(self):

        if os.path.exists("/usr/local/gromacs"):
	    print "You are using GROMACS via /usr/local/gromacs"
	elif os.path.exists("/usr/share/gromacs"):
	    print "You are using GROMACS via /usr/share/gromacs"
	else:
	    print "Default GROMACS installation not found. Exiting."
	    exit()

        print "---------------------------------------------------------" 
        print "Merging both trajectories into one and generating .xtc..." 
        print "---------------------------------------------------------" 

	# For GROMACS 2019.1 http://manual.gromacs.org/current/onlinehelp/gmx-trjcat.html

	os.system("gmx trjcat -f %s %s -o NewMergedTrajectory.xtc" % (
            xtc1, xtc2))
            
        if os.path.exists("NewMergedTrajectory.xtc"):
            print "...Done!"
            print "Check your current working directory for new merged trajectory (.xtc) file."
            print "Thank you for using TrajectoryMergeAssist."
            print "\t"
        else:
            print "Error! New Merged Trajectory not created! Please contact author."
            print "\t"

        exit()


if __name__ == "__main__":
    app = MergeMDs(None)
    app.title('TrajectoryMergeAssist v2.1: Merge Molecular Dynamics Extended Trajectories')
    app.mainloop()
