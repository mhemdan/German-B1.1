#!/bin/bash
# Setup script for GitHub Pages
# This script prepares the repository for GitHub Pages by:
# 1. Installing required Python packages
# 2. Converting all Markdown files to HTML
# 3. Providing instructions for pushing to GitHub

echo "===== German Learning Hub - GitHub Pages Setup ====="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Install required Python packages
echo "Installing required Python packages..."
pip install markdown || { echo "Failed to install packages. Please install manually: pip install markdown"; exit 1; }

# Convert Markdown files to HTML
echo ""
echo "Converting Markdown files to HTML..."
python3 convert_md_to_html.py

# Check if git is installed
if command -v git &> /dev/null; then
    # Check if this is a git repository
    if git rev-parse --is-inside-work-tree &> /dev/null; then
        echo ""
        echo "This directory is already a git repository."
        
        # Check if there are changes to commit
        if ! git diff-index --quiet HEAD --; then
            echo "There are uncommitted changes. Would you like to commit them? (y/n)"
            read -r response
            if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
                echo "Enter a commit message:"
                read -r commit_message
                git add .
                git commit -m "$commit_message"
                echo "Changes committed."
            fi
        fi
        
        # Ask if user wants to push to GitHub
        echo "Would you like to push to GitHub now? (y/n)"
        read -r response
        if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
            git push
            echo "Changes pushed to GitHub."
        fi
    else
        echo ""
        echo "This directory is not a git repository."
        echo "Would you like to initialize a git repository? (y/n)"
        read -r response
        if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
            git init
            git add .
            git commit -m "Initial commit"
            
            echo "Enter your GitHub username:"
            read -r username
            echo "Enter your repository name:"
            read -r repo_name
            
            git remote add origin "https://github.com/$username/$repo_name.git"
            echo "Remote repository added. You can now push with: git push -u origin main"
        fi
    fi
else
    echo ""
    echo "Git is not installed. You'll need to manually push to GitHub."
    echo "Please install git and follow the instructions in GITHUB_README.md"
fi

echo ""
echo "===== Setup Complete ====="
echo ""
echo "Next steps:"
echo "1. Push your repository to GitHub (if not done already)"
echo "2. Go to your repository settings on GitHub"
echo "3. Scroll down to the 'GitHub Pages' section"
echo "4. Select the branch you want to use (usually 'main')"
echo "5. Click 'Save'"
echo ""
echo "Your site will be published at: https://yourusername.github.io/repository-name/"
echo ""
echo "For more details, see GITHUB_README.md"
