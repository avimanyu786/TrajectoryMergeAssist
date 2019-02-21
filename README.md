# TrajectoryMergeAssist

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1243715.svg)](https://doi.org/10.5281/zenodo.1243715)

A python based GUI tool that helps in merging two sequential trajectories on [Desmond MD (molecular dynamics)](http://www.deshawresearch.com/resources_desmond.html) and [GROMACS](http://www.gromacs.org). This is a very useful tool for Bioinformaticians that makes it easier to work with different trajectories generated via extended molecular dynamics simulations on Desmond.

Key features:

1. Works with both the latest and older versions of Desmond.

2. Generates new "-out.cms" file, ready for use in Maestro if Desmond version is 2018.1 or later.

3. Works with GROMACS ".xtc" files.

## Easy Installation:

Download the **[installer](https://github.com/avimanyu786/TrajectoryMergeAssist/releases/download/v2.1/tma_v2.1-setup.sh)**.

To install, just use a terminal and run:

1. `chmod +x tma_v2.1-setup.sh`

2. `./tma_v2.1-setup.sh`

The installer will also set the path for you.

Run _TrajectoryMergeAssist_ GUI with the following simple command:

`tma`

Contributions are most welcome for further improvements and including other molecular dynamics formats to make it universal.

Bandyopadhyay A. (2018) Improving productivity while managing extensive molecular dynamics simulation data. PeerJ Preprints 6:e26920v1 https://doi.org/10.7287/peerj.preprints.26920v1
