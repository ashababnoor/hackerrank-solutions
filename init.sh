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
    echo "Successfully, pushed changes to branch $branch"
}