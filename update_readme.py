import requests
import feedparser
import json

RSS_URL = "https://siv2r.substack.com/feed"

feed = feedparser.parse(RSS_URL)
# Get the latest 5 posts
posts = feed.entries[:5]
# Generate markdown list for posts
blog_md = ""
for i, post in enumerate(posts):
    blog_md += f"{i+1}. [{post.title}]({post.link})\n"

# Read the current README.md content
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

# Define your insertion markers
start_marker = "<!-- BLOG-POSTS:START -->"
end_marker = "<!-- BLOG-POSTS:END -->"

# Find positions of markers in the README
start_index = readme.find(start_marker)
end_index = readme.find(end_marker)

if start_index != -1 and end_index != -1:
    # Insert the blog markdown between the markers
    updated_readme = (
        readme[:start_index + len(start_marker)] +
        "\n" + blog_md + "\n" +
        readme[end_index:]
    )
else:
    # If markers don't exist, raise ValueError
    raise ValueError("Markers for blog posts doesn't exist")

# Write the updated README back to file
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("Added the following blogs to README:")
print(f"{blog_md}")

# Dump RSS feed to JSON file
with open("rss_feed.json", "w", encoding="utf-8") as file:
    json.dump(feed.entries, file, ensure_ascii=False, indent=4)
print("Dumped RSS feed entries to rss_feed.json")