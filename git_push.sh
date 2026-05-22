#!/bin/sh

set -e

git_user_id=$1
git_repo_id=$2
release_note=$3
git_host=$4

if [ "$git_host" = "" ]; then
    git_host="github.com"
fi

if [ "$git_user_id" = "" ]; then
    git_user_id="cervinodata"
fi

if [ "$git_repo_id" = "" ]; then
    git_repo_id="python"
fi

if [ "$release_note" = "" ]; then
    release_note="Minor update"
fi

git init

git add .

git commit -m "$release_note"

REMOTE_URL="git@${git_host}:${git_user_id}/${git_repo_id}.git"

if git remote get-url origin >/dev/null 2>&1; then
    git remote set-url origin "$REMOTE_URL"
else
    git remote add origin "$REMOTE_URL"
fi

echo "Git pushing to $REMOTE_URL"

CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "" ]; then
    CURRENT_BRANCH="main"
    git checkout -B "$CURRENT_BRANCH"
fi

git push -u origin "$CURRENT_BRANCH"

