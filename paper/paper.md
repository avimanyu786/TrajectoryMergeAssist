---
title: 'TrajectoryMergeAssist: A Python based tool to simplify extended molecular dynamics simulations on Desmond'
tags:
  - Python
  - Desmond
  - Bioinformatics
  - Trajectories
  - Molecular Dynamics
  - Extended Simulations
authors:
  - name: Avimanyu Bandyopadhyay
    orcid: 0000-0003-4806-2238
    affiliation: 1
affiliations:
 - name: Department of Biotechnology, Heritage Institute of Technology
   index: 1
 - name: Institution 1
   index: 1

 - name: Maulana Abul Kalam Azad University of Technology (formerly West Bengal University of Technology)
   index: 2
 - name: Institution 2
   index: 2   
date: 03 May 2018
---

# Summary

Working with trajectories generated with the Desmond molecular dynamics software
can be quite inconvenient when simulations are extended multiple number of times 
with the same. Extended simulations allow Bioinformaticians to observe and interpret 
plots upto greater lengths of time and also do it at their own time of convenience 
when with lesser resources.

To make this process simpler and easier, ``TrajectoryMergeAssist`` was created. 
It is a very handy and user-friendly GUI tool for Bioinformaticians to manage extended 
trajectories and finally merge all of them into a single trajectory with a series of 
steps and observations:

With every gradual extended simulation, the user would like to view the resultant plots
starting from the first trajectory until the end of the second. The user would be eager
to view the resultant RMSD/RMSF plot of the same on Desmond (Maestro) after the end of 
each extended simulation and that is when this tool becomes very useful. With further 
extended simulations, the user can use the combined trajectory obtained previously and 
merge it with the third and so on.

The tool has been written in Python and makes use of *Tkinter*, one of Python's own GUI 
programming toolkits.

## Key Features

Starting with Desmond 2018.1, a new Desmond script has been introduced and the earlier
one has been deprecated for merging trajectories. ``TrajectoryMergeAssist`` works with 
both the latest and earlier versions of Desmond. 

Unlike versions prior to 2018.1, Desmond creates "merged.cms" files instead of "merged-out.cms",
making it a requirement to manually rename it to the latter to make it ready for viewing on
Maestro. ``TrajectoryMergeAssist`` also takes care of this by generating an "-out.cms" file
instead of ".cms".

## Usage

To be able to use the tool, the ``python-tk`` or ``tkinter`` package would be required in addition to Python on Linux.

For systems like Ubuntu, it can be installed with a Linux terminal with the following command: 

``sudo apt-get install python-tk``  

For Python3 on Ubuntu, the terminal command would be: 

``sudo apt-get install python3-tk``.

For CentOS type systems, the installation can be done via: 

``sudo yum install tkinter``. 

For Python3 on CentOS, the preferable command would be: 

``sudo yum install python34-tkinter``

or

``sudo yum install python36u-tkinter``.

### Steps to use TrajectoryMergeAssist

1. The "TMA.py" file has to be present in a directory containing the following required input files and trajectories:

    a. The "-out.cms" file

    b. The first trajectory directory(ends with "_trj")

    c. The second trajectory directory from an extended Desmond MD simulation.

2.  It is strongly recommended to work with the above files from a location like ``/home/username/directory``

3.  Navigate to the directory on a terminal window and run:

    ``python TMA.py``

4.  Select the "-out.cms" file

5.  Navigate to the two "_trj" directories

6.  The 3 choices will be visible in the background terminal so that the selections can be confirmed.

7.  Click on "Merge Trajectories"

8.  Wait until the "...Done!" message

9.  The new merged trajectory along-with the new "-out.cms" file can be found in the same working directory.


# References

