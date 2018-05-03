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

Starting with Desmond 2018.1, a new Desmond script has been introduced and the earlier
one has been deprecated for merging trajectories. ``TrajectoryMergeAssist`` works with 
both the latest and earlier versions of Desmond. 

Unlike versions prior to 2018.1, Desmond creates "merged.cms" files instead of "merged-out.cms",
making it a requirement to manually rename it to the latter to make it ready for viewing on
Maestro. ``TrajectoryMergeAssist`` also takes care of this by generating an "-out.cms" file
instead of ".cms".

# References

