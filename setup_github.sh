#!/bin/bash

# This script helps set up GitHub connection and push the Snake Game repository

# Set git user configuration
echo "Setting up Git user configuration..."
read -p "Enter your GitHub username: " username
read -p "Enter your GitHub email: " email

git config --global user.name "$username"
git config --global user.email "$email"

echo "Git user configured as:"
git config --global user.name
git config --global user.email

# Create a new repository on GitHub
echo -e "\nTo create a new repository on GitHub:"
echo "1. Go to https://github.com/new"
echo "2. Name your repository 'snake_game'"
echo "3. Add a description (optional)"
echo "4. Choose public or private"
echo "5. Do NOT initialize with README, .gitignore, or license"
echo "6. Click 'Create repository'"

read -p "Have you created the repository? (y/n): " created

if [ "$created" != "y" ]; then
  echo "Please create the repository first and then run this script again."
  exit 1
fi

# Get the repository URL
read -p "Enter your GitHub repository URL (e.g., https://github.com/username/snake_game.git): " repo_url

# Authentication options
echo -e "\nGitHub no longer supports password authentication since June 13, 2023."
echo "You have two options for authentication:"
echo "1. Use a Personal Access Token (PAT)"
echo "2. Set up SSH key authentication"
read -p "Choose authentication method (1 for PAT, 2 for SSH): " auth_method

if [ "$auth_method" == "1" ]; then
  echo -e "\nTo create a Personal Access Token:"
  echo "1. Go to https://github.com/settings/tokens"
  echo "2. Click 'Generate new token'"
  echo "3. Give it a name (e.g., 'Snake Game Access')"
  echo "4. Select scopes: at minimum, check 'repo'"
  echo "5. Click 'Generate token'"
  echo "6. Copy the token (you won't be able to see it again!)"
  
  read -p "Have you created your Personal Access Token? (y/n): " token_created
  
  if [ "$token_created" == "y" ]; then
    echo -e "\nWhen prompted for password during git operations, use your Personal Access Token instead."
    
    # Configure credential helper to store the token
    git config --global credential.helper store
    echo "Credential helper configured to store your token."
    
    # If using HTTPS, keep the URL as is
    if [[ $repo_url != https://github.com/* ]]; then
      https_url=$(echo $repo_url | sed 's|git@github.com:|https://github.com/|' | sed 's|\.git$|.git|')
      echo "Converting to HTTPS URL: $https_url"
      repo_url=$https_url
    fi
  else
    echo "Please create a Personal Access Token before continuing."
    exit 1
  fi
elif [ "$auth_method" == "2" ]; then
  # Generate SSH key
  ssh-keygen -t ed25519 -C "$email"
  
  # Start ssh-agent
  eval "$(ssh-agent -s)"
  
  # Add SSH key to ssh-agent
  ssh-add ~/.ssh/id_ed25519
  
  # Display the public key
  echo -e "\nCopy the following SSH key to GitHub (https://github.com/settings/keys):"
  cat ~/.ssh/id_ed25519.pub
  
  echo -e "\nAfter adding the SSH key to GitHub, press Enter to continue..."
  read
  
  # Convert HTTPS URL to SSH URL if needed
  if [[ $repo_url == https://github.com/* ]]; then
    ssh_url=$(echo $repo_url | sed 's|https://github.com/|git@github.com:|' | sed 's|\.git$|.git|')
    echo "Converting to SSH URL: $ssh_url"
    repo_url=$ssh_url
  fi
else
  echo "Invalid option. Exiting."
  exit 1
fi

# Add remote and push
echo -e "\nAdding remote repository..."
cd /home/ec2-user/q/snake_game
git remote add origin $repo_url

echo -e "\nPushing to GitHub..."
git push -u origin master

echo -e "\nRepository successfully pushed to GitHub!"
echo "You can now clone it to your local machine with:"
echo "git clone $repo_url"
# Add remote and push
echo -e "\nAdding remote repository..."
cd /home/ec2-user/q/snake_game
git remote add origin $repo_url

echo -e "\nPushing to GitHub..."
git push -u origin master

echo -e "\nRepository successfully pushed to GitHub!"
echo "You can now clone it to your local machine with:"
echo "git clone $repo_url"
