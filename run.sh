#!/bin/bash

# Debian/Ubuntu
# Rudimentary setup script to be run in 
# AWS EC2 Ubuntu instance

# Go to your home directory
cd ~

# Define project directory name
dir="discord-bot"
repo="https://github.com/nigeltroy/discord-bot.git"

# If project directory exists in the current directory,
# go to the project directory
if [[ -d $dir ]]; then
    cd ./$dir
# else if you're in the project directory,
# do nothing
elif [[ ${PWD##*/} == $dir ]]; then
    :
# else if not found, clone the repo
else
    git clone $repo
    cd ./$dir
fi

# Pull all recent changes from master
git pull

# Install Python 3 and Pip
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip

# Install all requirements for the project
pip3 install -r requirements.txt

# If .env doesn't exist, write into the stub env file and
# copy to .env
if [[ -f .env ]]; then
    :
else
    # Open up the given stub .env file and
    # copy the stub .env file to the actual .env file
    vim stub.env
    cp stub.env .env
fi

# Kill all old main.py processes
pkill -f main.py

# Run the project (as a daemon as specced in main.py)
python3 main.py
