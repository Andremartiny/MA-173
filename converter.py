import os
import glob
import subprocess

# Set the path to the "converted" subfolder
folder_path = "./converted"

# Use glob to get all the Markdown files in the folder
markdown_files = glob.glob(os.path.join(folder_path, "*.md"))

# Loop through each Markdown file
for md_file in markdown_files:
    # Create the output file path by replacing the .md extension with .html
    html_file = os.path.splitext(md_file)[0] + ".html"

    # Run the pandoc command to convert the Markdown file to an HTML file
    subprocess.run(["pandoc", md_file, "-f", "markdown", "-t", "html", "--mathjax", "-o", html_file])