#!/bin/bash
# Deploy script for Kunstgeschiedenis website
# Usage: ./deploy.sh "commit message"

set -e

WORKDIR="/root/.openclaw/workspace/kunstgeschiedenis/website"

cd "$WORKDIR"

# Check for changes
if git diff-index --quiet HEAD --; then
    echo "ℹ️  No changes to commit"
else
    # Commit message
    MSG="${1:-auto: website update $(date +%Y-%m-%d\ %H:%M)}"
    
    echo "📦 Committing changes..."
    git add -A
    git commit -m "$MSG"
    
    echo "🚀 Pushing to GitHub..."
    git push origin master
fi

# Upload via Python SFTP script
python3 "$WORKDIR/sftp_upload.py"

echo "   GitHub: https://github.com/suzyassist/artproject"
