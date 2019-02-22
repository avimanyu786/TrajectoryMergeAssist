# TrajectoryMergeAssist v2.1

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2574623.svg)](https://doi.org/10.5281/zenodo.2574623)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/avimanyu786/TrajectoryMergeAssist/wiki)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/avimanyu786/TrajectoryMergeAssist/graphs/contributors)

A python based GUI tool that helps in merging two sequential trajectories on [Desmond](http://www.deshawresearch.com/resources_desmond.html) or [GROMACS](http://www.gromacs.org). This is a very useful tool for Bioinformaticians that makes it easier to work with different trajectories generated via extended molecular dynamics simulations on Desmond and GROMACS.

Key features:

1. Works with both the latest and older versions of Desmond.

2. Generates new "-out.cms" file, ready for use in Maestro if Desmond version is 2018.1 or later.

3. Works with GROMACS ".xtc" files.

## Easy Installation

1. Download the [installer](https://github.com/avimanyu786/TrajectoryMergeAssist/releases/download/v2.1/tma_v2.1-setup.sh).

2. To install, just use a terminal and run:

    a. `chmod +x tma_v2.1-setup.sh`

    b. `./tma_v2.1-setup.sh`

    The installer will also set the path for you.

3. Run _TrajectoryMergeAssist_ GUI with the following simple command:

   `tma`

## Steps to use TrajectoryMergeAssist

### i. Merging Desmond MD trajectories

1. Make sure you have the following required input files and trajectories:

    a. The "-out.cms" file

    b. The first trajectory directory (name ends with "_trj")

    c. The second trajectory directory from an extended Desmond MD simulation

2.  It is recommended to work with the above files from a location like:
    
    /home/username/directory/

3.  Navigate to the directory on a terminal window and run:    

    `tma`

      or  

    `tma-py3`      -- For Python3 Only

4.  Select the "-out.cms" file

5.  Navigate to the two trajectory directories ending with "_trj"

6.  The 3 choices will be visible in the background terminal so that the selections can be confirmed.

7.  Click on "Merge Desmond Trajectories"

8.  Wait until the "...Done!" message

9.  The new merged trajectory along-with the new "-out.cms" file can be found in the same working directory

### ii. Merging GROMACS MD trajectories

1. Make sure you have the following required input trajectory files:

    a. The first trajectory file (name ends with ".xtc")

    b. The second trajectory file from an extended GROMACS MD simulation

2.  It is recommended to work with the above files from a location like:
    
    /home/username/directory/

3.  Navigate to the directory on a terminal window and run:    

    `tma`

     or  

    `tma-py3`      -- For Python3 Only

4.  Choose the two trajectory files ending with ".xtc"

5.  The 2 choices will be visible in the background terminal so that the selections can be confirmed.

6.  Click on "Merge GROMACS Trajectories"

7.  Wait until the "...Done!" message

8.  The new merged trajectory (".xtc" file) can be found in the same working directory.

Contributions are most welcome for further improvements and including other molecular dynamics formats to make it universal.

### Citation [![DOI](https://zenodo.org/badge/DOI/10.7287/peerj.preprints.26920.svg)](https://doi.org/10.7287/peerj.preprints.26920)

If *TrajectoryMergeAssist* helped you during your research while managing extended molecular dynamics data, please cite it as:

**Bandyopadhyay A. (2018) Improving productivity while managing extensive molecular dynamics simulation data. PeerJ Preprints 6:e26920 https://doi.org/10.7287/peerj.preprints.26920**

*BibTex*:

```
@article{10.7287/peerj.preprints.26920,
 title = {Improving productivity while managing extensive molecular dynamics simulation data},
 author = {Bandyopadhyay, Avimanyu},
 year = 2018,
 month = may,
 keywords = {molecular dynamics, extended simulations, managing data, python, gui},
 abstract = {
        This paper discusses the difficulties experienced by bioinformaticians while working with extensive data generated from extended molecular dynamics simulations. For better experimental analysis, it often becomes crucial to conduct simulations up to extended periods of time. When with limited resources, running a complete simulation up to a desired length of time can become quite difficult to be performed at one go. So, a new approach is proposed to simplify handling such data for better productivity.
      },
 volume = 6,
 pages = {e26920},
 journal = {PeerJ Preprints},
 issn = {2167-9843},
 url = {https://doi.org/10.7287/peerj.preprints.26920},
 doi = {10.7287/peerj.preprints.26920}
}
```
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-200x33.png)](https://opensource.org/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://facebook.com/iAvimanyu)
> *© [Avimanyu Bandyopadhyay](https://raw.githubusercontent.com/avimanyu786/TrajectoryMergeAssist/master/AUTHORS) 2018-19*
