#!/bin/bash
# Deploy script for Kunstgeschiedenis website
# Usage: ./deploy.sh "commit message"

set -e

WORKDIR="/root/.openclaw/workspace/kunstgeschiedenis/website"
REMOTE_USER="matthiasr.com"
REMOTE_HOST="ssh.matthiasr.com"
REMOTE_PASS="y41*^&XJlS!BaM"
REMOTE_PATH="/www/art"

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

echo "📤 Uploading to One.com server..."

# First, ensure directories exist on server
lftp -c "open -u $REMOTE_USER,'$REMOTE_PASS' sftp://$REMOTE_HOST; mkdir -p $REMOTE_PATH/images/postmodern $REMOTE_PATH/images/postmodernisme $REMOTE_PATH/images/hedendaags; exit 0"

# Then upload all files
lftp -c "open -u $REMOTE_USER,'$REMOTE_PASS' sftp://$REMOTE_HOST; mirror -R --parallel=6 --no-perms . $REMOTE_PATH"

echo "✅ Deploy complete!"
echo "   GitHub: https://github.com/suzyassist/artproject"
echo "   Live:   https://matthiasr.com/art/"
