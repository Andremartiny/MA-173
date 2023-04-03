import os
import glob
from bs4 import BeautifulSoup

# Read the content of the template file
template_file = 'index.html'
with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Use Beautiful Soup to parse the template
soup = BeautifulSoup(template_content, 'html.parser')

# Set the path to the subfolder containing the HTML files
subfolder_path = '.\\converted'

# Use glob to get all the HTML files in the subfolder
html_files = glob.glob(os.path.join(subfolder_path, '*.html'))

# Loop through each HTML file
for html_file in html_files:
    # Read the content of the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        file_content = f.read()

    # Use Beautiful Soup to parse the HTML file content
    file_soup = BeautifulSoup(file_content, 'html.parser')

    # Extract the id from the file name (assuming the id is the file name without the extension)
    file_id = os.path.splitext(os.path.basename(html_file))[0]

    # Find the corresponding div in the template using its id
    target_div = soup.find('div', {'id': file_id})

    # If the target div is found, append the content of the HTML file to the div
    if target_div:
        for element in file_soup.contents:
            target_div.append(element)


# Save the modified template to a new file
output_file = 'output.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))