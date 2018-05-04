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
- name: Department of Biotechnology, Heritage Institute of Technology, Kolkata, India
  index: 1
- name: Maulana Abul Kalam Azad University of Technology (formerly West Bengal University of Technology), India
  index: 2
  
date: 03 May 2018
bibliography: paper.bib
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
programming toolkits. Another version has also been written in Python3.

## Key Features

### Works with both the latest and older versions of Desmond

Starting with Desmond 2018.1, a new Desmond script has been introduced and the earlier
one has been deprecated for merging trajectories. ``TrajectoryMergeAssist`` checks for the same
and proceeds accordingly, in order to support both the latest and earlier versions. 

### Generates "-out.cms" file ready for use in Maestro

Unlike versions prior to 2018.1, Desmond creates "merged.cms" files instead of "merged-out.cms",
making it a requirement to manually rename it to the latter to make it ready for viewing on
Maestro. ``TrajectoryMergeAssist`` also takes care of this by generating an "-out.cms" file
instead of ".cms".

## Usage Links

1. [Repository](https://github.com/avimanyu786/TrajectoryMergeAssist)

2. [Releases](https://github.com/avimanyu786/TrajectoryMergeAssist/releases)

3. [Documentation](https://github.com/avimanyu786/TrajectoryMergeAssist/wiki)

# References
