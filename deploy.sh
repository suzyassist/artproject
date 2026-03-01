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

# Create lftp command file (avoids password in process list)
cat > /tmp/lftp_commands.txt << EOF
open -u matthiasr.com,y41*^&XJlS!BaM sftp://ssh.matthiasr.com
mirror -R --parallel=6 --no-perms . /www/art
exit
EOF

lftp -f /tmp/lftp_commands.txt
rm /tmp/lftp_commands.txt

echo "✅ Deploy complete!"
echo "   GitHub: https://github.com/suzyassist/artproject"
echo "   Live:   https://matthiasr.com/art/"
