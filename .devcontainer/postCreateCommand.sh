#!/bin/sh
pip3 install -U pytest
pip3 install -U pytest-dependency
pip3 install -U requests
sudo pip3 install 'argcomplete>=0.5.7'
sudo activate-global-python-argcomplete
register-python-argcomplete pytest >> /home/vscode/.bashrc
