# TrajectoryMergeAssist v1.2
# A python3 based GUI tool that helps in merging two trajectories on Desmond MD

# Copyright (C) 2018 Avimanyu Bandyopadhyay

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

import tkinter
import os
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()


class MergeMDs(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        button = tkinter.Button(self, text='Browse "-out.cms" file', command=self.AskInputFile)
        button.grid(column=0, row=1)

        button2 = tkinter.Button(self, text='Choose Trajectory 1', command=self.AskTrajectory1)
        button2.grid(column=0, row=2)

        button3 = tkinter.Button(self, text='Choose Trajectory 2', command=self.AskTrajectory2)
        button3.grid(column=0, row=3)

        button3 = tkinter.Button(self, text='Merge Trajectories', command=self.MergeTrajectories)
        button3.grid(column=0, row=4)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry("400x120")

    def AskInputFile(self):
        filename = tkinter.filedialog.askopenfilename(parent=root, title='Choose -out.cms file')
        global cms
        cms = os.path.basename(filename)
        if len(cms) > 0:
            print("%s selected" % cms)

    def AskTrajectory1(self):
        global in1_trj
        in1_trj = tkinter.filedialog.askdirectory(parent=root, initialdir="pwd", title='Please Select Trajectory 1')
        if len(in1_trj) > 0:
            print("You chose %s" % in1_trj)

    def AskTrajectory2(self):
        global in2_trj
        in2_trj = tkinter.filedialog.askdirectory(parent=root, initialdir="pwd", title='Please Select Trajectory 2')
        if len(in2_trj) > 0:
            print("You chose %s" % in2_trj)

    def MergeTrajectories(self):
        print("-------------------------------------------------------------")
        print("Merging both trajectories into one and generating -out.cms...")
        print("-------------------------------------------------------------")

        # For Desmond Version >= 2018.1 https://www.schrodinger.com/kb/282357

        if os.path.isfile("/opt/schrodinger2018-3/internal/bin/trj_merge.py"):
            os.system("/opt/schrodinger2018-3/run trj_merge.py %s %s %s -o NewMergedTrajectory" % (
            cms, in1_trj, in2_trj))
            os.system("mv NewMergedTrajectory.cms NewMergedTrajectory-out.cms")

        if os.path.isfile("/opt/schrodinger2018-2/internal/bin/trj_merge.py"):
            os.system("/opt/schrodinger2018-2/run trj_merge.py %s %s %s -o NewMergedTrajectory" % (
            cms, in1_trj, in2_trj))
            os.system("mv NewMergedTrajectory.cms NewMergedTrajectory-out.cms")

        if os.path.isfile("/opt/schrodinger2018-1/internal/bin/trj_merge.py"):
            os.system("/opt/schrodinger2018-1/run trj_merge.py %s %s %s -o NewMergedTrajectory" % (
            cms, in1_trj, in2_trj))
            os.system("mv NewMergedTrajectory.cms NewMergedTrajectory-out.cms")

        else:  # For Desmond Version < 2018.1 https://www.schrodinger.com/kb/90
            if os.path.isfile("/opt/schrodinger2017-4/desmond-v5.2/bin/Linux-x86_64/manipulate_trj.py"):
                os.system("/opt/schrodinger2017-4/run -FROM desmond manipulate_trj.py %s NewMergedTrajectory %s %s" % (
                cms, in1_trj, in2_trj))

            if os.path.isfile("/opt/schrodinger2017-3/desmond-v5.2/bin/Linux-x86_64/manipulate_trj.py"):
                os.system("/opt/schrodinger2017-3/run -FROM desmond manipulate_trj.py %s NewMergedTrajectory %s %s" % (
                cms, in1_trj, in2_trj))

        print("...Done!")
        exit()


if __name__ == "__main__":
    app = MergeMDs(None)
    app.title('TrajectoryMergeAssist: Merge Desmond MD Trajectories')
    app.mainloop()
