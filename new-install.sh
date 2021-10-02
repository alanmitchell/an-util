#!/bin/bash
# List of software needed for a new Linux install for me.

# Use ssh-keygen to generate an SSH key pair for the new machine.
# Copy the Public key to Github and to commonly accessed Linux servers: DigitalOcean
# and AHFC Rackspace server.

# Clone this Repo, an-util, to the machine.

# Need to get Python installed before running pip commands below.
# Anaconda:  https://www.anaconda.com/products/individual


# Share Downloads directory with Linux
# Share Admin/Invoices, Admin/TimeTracking
# Share AHFC/BMON_FY21_onward

sudo apt install -y nano

pip install --no-input visidata
pip install --no-input bmondata

# Install VS Code:  https://code.visualstudio.com/download

sudo apt install -y pdftk pandoc texlive texlive-plain-generic
sudo apt install -y picocom

# Picoscope Oscilloscope:  https://www.picotech.com/downloads/linux

# See the useful-aliases file in this repo and add to the end of .bashrc
