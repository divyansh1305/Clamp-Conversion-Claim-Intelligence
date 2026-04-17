#!/bin/bash

# Auto Git Sync Script
echo "Starting Auto Git Sync every 10 minutes..."

while true; do
  # Wait for 10 minutes (600 seconds)
  sleep 600

  # Check if there are any changes
  if [[ -n $(git status -s) ]]; then
    # Add all changes
    git add .
    
    # Get current timestamp for the commit message
    timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    
    # Commit changes
    git commit -m "Auto-sync at $timestamp"
    
    # Push to origin main
    git push origin main
    
    echo "Changes synced to GitHub at $timestamp"
  else
    echo "No changes detected at $(date '+%Y-%m-%d %H:%M:%S')."
  fi
done
