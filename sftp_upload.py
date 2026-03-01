#!/usr/bin/env python3
"""
Deploy script for Kunstgeschiedenis website - SFTP upload via expect
"""

import subprocess
import os
import sys

WORKDIR = "/root/.openclaw/workspace/kunstgeschiedenis/website"
REMOTE_USER = "matthiasr.com"
REMOTE_HOST = "ssh.matthiasr.com"
REMOTE_PASS = "y41*^&XJlS!BaM"
REMOTE_PATH = "/www/art"

def run_expect_sftp(commands):
    """Run SFTP commands via expect"""
    expect_script = f"""
set timeout 300
spawn sftp {REMOTE_USER}@{REMOTE_HOST}
expect "password:"
send "{REMOTE_PASS}\\r"
"""
    for cmd in commands:
        expect_script += f'expect "sftp>"\nsend "{cmd}\\r"\n'
    expect_script += 'expect "sftp>"\nsend "exit\\r"\nexpect eof\n'
    
    result = subprocess.run(['expect'], input=expect_script, capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def upload_all():
    """Upload all website files"""
    print("📤 Uploading to One.com server...")
    
    # Build list of files to upload
    files_to_upload = []
    for root, dirs, files in os.walk(WORKDIR):
        # Skip .git directory
        if '.git' in root:
            continue
        for f in files:
            local_path = os.path.join(root, f)
            rel_path = os.path.relpath(local_path, WORKDIR)
            remote_path = f"{REMOTE_PATH}/{rel_path}"
            files_to_upload.append((local_path, remote_path))
    
    print(f"   Found {len(files_to_upload)} files to upload")
    
    # Build SFTP commands
    commands = []
    
    # Create directories first
    dirs_created = set()
    for local_path, remote_path in files_to_upload:
        remote_dir = os.path.dirname(remote_path)
        if remote_dir not in dirs_created:
            commands.append(f"mkdir -p {remote_dir}")
            dirs_created.add(remote_dir)
    
    # Upload files
    for local_path, remote_path in files_to_upload:
        commands.append(f"put {local_path} {remote_path}")
    
    success, output = run_expect_sftp(commands)
    
    if success:
        print("✅ Deploy complete!")
        print(f"   Live: https://matthiasr.com/art/")
        return 0
    else:
        print(f"❌ Upload failed:\n{output}")
        return 1

if __name__ == '__main__':
    sys.exit(upload_all())
