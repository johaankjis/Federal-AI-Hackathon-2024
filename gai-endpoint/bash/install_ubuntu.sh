#!/bin/bash

# Warning message
echo "Warning: This script has only been tested on Ubuntu 22.04. Use it at your own risk."

# Install Python 3.10
sudo apt update
sudo apt install -y python3 python3-dev

# Install Pip
sudo apt install -y python3-pip

# Install pipenv
sudo pip install pipenv

# Install git
sudo apt install -y git


# Check if SSH key exists, if not, generate a new one
if [ ! -f ~/.ssh/id_rsa ]; then
    echo "Generating SSH key..."
    ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
fi

# Display SSH public key and instructions for adding it to GitHub deploy keys
echo "Please add the following SSH key to the deploy keys for the 'gov.nsf' GitHub repository:"
cat ~/.ssh/id_rsa.pub
echo ""
read -n 1 -s -r -p "Press any key to continue..."


# Clone your project repository (replace with your repository URL)
git clone git@github.com:aptivators/gov.nsf.git

cd gov.nsf

pipenv install

# Activate the pipenv virtual environment
pipenv shell

# Add the current directory to PYTHONPATH in .bashrc
echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)" >> ~/.bashrc


# Source the .bashrc file to apply the changes immediately
source ~/.bashrc

# Function to fetch and append SSH keys
fetch_and_append_keys() {
    local github_username=$1
    local keys_url="https://github.com/${github_username}.keys"
    local authorized_keys_file="/root/.ssh/authorized_keys"

    # Create .ssh directory if it doesn't exist
    mkdir -p /root/.ssh

    # Fetch and append the keys
    wget -O - "$keys_url" >> "$authorized_keys_file"

    # Set appropriate permissions
    chmod 600 "$authorized_keys_file"
}

# Prompt for GitHub username
read -p "Enter GitHub username: " github_username

# Fetch and append SSH keys
fetch_and_append_keys "$github_username"

echo "SSH keys from GitHub user '$github_username' have been added to root's authorized keys."


