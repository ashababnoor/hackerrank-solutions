function git_add_commit_push() {
    local commit_msg="$1"

    # Check if a commit message is provided
    if [ -z "$commit_msg" ]; then
        echo "Error: Please provide a commit message."
        return 1
    fi

    # Add changes to staging area
    git add .

    # Commit changes with the provided message
    git commit -m "$commit_msg"

    # Push changes to the current branch
    branch=$(git rev-parse --abbrev-ref HEAD)
    git push origin $branch

    # Print success message
    echo ""

    remote_url=$(git remote get-url origin)

    # Extract server and repo
    server=$(echo $remote_url | awk -F: '{print $1}' | awk -F@ '{print $2}')
    repo=$(echo $remote_url | awk -F: '{print $2}' | sed 's/.git$//')

    echo "Successfully, pushed to remote server: $server"
    echo "                        remote repo:   $repo"
    echo "                        remote branch: $branch"    
}

alias gitit=git_add_commit_push 