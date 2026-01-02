#!/bin/bash

echo "📁 Adding files to git..."
git add .

echo "💾 Creating commit..."
git commit -m "DSA Practice - Added solutions on $(date +'%Y-%m-%d %H:%M')"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Done! Repository updated successfully!"
echo "🌐 View at: https://github.com/ankit1350/dsa-practice"
