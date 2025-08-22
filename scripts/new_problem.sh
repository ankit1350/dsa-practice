#!/bin/bash
set -e

topic="$1"
slug="$2"
title="$3"
link="$4"

if [ -z "$topic" ] || [ -z "$slug" ] || [ -z "$title" ] || [ -z "$link" ]; then
  echo "Usage: $0 <topic> <slug> \"<Title>\" \"<Link>\""
  exit 1
fi

# Validate topic exists
if [ ! -d "$topic" ]; then
  echo "Topic folder '$topic' does not exist."
  echo "Create it or use one of: arrays, strings, linked_list, trees, graphs"
  exit 1
fi

fname="$topic/${slug}.py"
if [ -f "$fname" ]; then
  echo "File already exists: $fname"
  exit 1
fi

cat > "$fname" << EOF2
"""
Problem: $title
Link: $link

Approach:
- <Describe your approach here>
- Time: O(?), Space: O(?)

Notes:
- <Edge cases / pitfalls / patterns>
"""

def solve():
    # TODO: implement
    pass


if __name__ == "__main__":
    # quick test harness
    print("Running: $title")
    # print(solve())
EOF2

# Update the topic README index row
if [ -f "$topic/README.md" ]; then
  echo "| ${slug}.py | $title | <approach> |" >> "$topic/README.md"
fi

echo "Created: $fname"
