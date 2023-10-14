# Define Unicode code points 
party_popper_emoji="\U0001F389"   # 🎉
confetti_ball_emoji="\U0001F38A"  # 🎊

# Define ANSI escape codes
bold='\033[1m'
reset='\033[0m'

# Define color codes (non-bold)
blue='\033[0;34m'       # Blue
light_blue='\033[0;36m' # Light Blue
green='\033[0;32m'      # Green
red='\033[0;31m'        # Red
yellow='\033[0;33m'     # Yellow
purple='\033[0;35m'     # Purple

# Define bold color codes
blue_bold='\033[1;34m'       # Bold Blue
light_blue_bold='\033[1;36m' # Bold Light Blue
green_bold='\033[1;32m'      # Bold Green
red_bold='\033[1;31m'        # Bold Red
yellow_bold='\033[1;33m'     # Bold Yellow
purple_bold='\033[1;35m'     # Bold Purple

# Reset color and formatting
nc='\033[0m' # No Color


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

    echo "${green_bold}Hurray!${nc} ${party_popper_emoji}${confetti_ball_emoji}"
    echo "Successfully, pushed to remote server: ${yellow}$server${nc}"
    echo "                        remote repo:   ${yellow}$repo${nc}"
    echo "                        remote branch: ${yellow}$branch${nc}"
}

alias gitit=git_add_commit_push 