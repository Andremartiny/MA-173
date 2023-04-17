import os
import glob
from bs4 import BeautifulSoup
import re
import subprocess


################## DEL 1: ###########################################
def restructure(pathin, pathout):
    dictionary = {}
    # 1. Open the Markdown document and read it line by line
    with open(pathin, 'r') as file:
        lines = file.readlines()

    # 2. Create an empty list called "subsubheaders"
    subsubheaders = []

    # 3. Loop through lines
    for line in lines:
        # 4. Check if the line starts with "### "
        if line.startswith("### "):
            # 5. Remove the identifier (if it exists) and any trailing whitespace
            newline = re.sub(r'\s*{#.*?}\s*$', '', line).rstrip()

            # 6. If newline is not in subsubheaders, append it
            if newline not in subsubheaders:
                subsubheaders.append(newline)
                dictionary[newline] = {"grunnleggende" : [], "middels" : [], "avansert" : []}

    # Print the unique subsubheaders
    # for header in subsubheaders:
    #     print(header)
    # print(dictionary)

    current_subheader = ''
    current_subsubheader = ''
    current_nivå = ''
    nivå = ["grunnleggende", "middels", "avansert"]

    for line in lines:
        # Check if the line is a subheader
        if line.startswith('## '):
            current_subheader = line[2:]
            continue
        if line.startswith('### '):
            current_subsubheader = re.sub(r'\s*{#.*?}\s*$', '', line).rstrip()
            continue
        if line.startswith('#### ') or line.startswith('##### '):
            added = False
            for niv in nivå:
                if re.search(niv, line, re.IGNORECASE):
                    added = True
                    current_nivå = niv
                    if re.search("vurderingskriterier", line, re.IGNORECASE):
                        dictionary[current_subsubheader][niv].append("#### Vurderingskriterier " + niv + ": " + current_subheader)    
                    else:
                        dictionary[current_subsubheader][niv].append("#### " + niv.capitalize() + ": " + re.sub(r"^###\s*", "",current_subsubheader) + ", " + current_subheader)
            if added == False:
                dictionary[current_subsubheader][current_nivå].append(line)
            continue
        if current_subsubheader == '' or current_nivå == '':
            continue
        else:
            dictionary[current_subsubheader][current_nivå].append(line)


    counter = 1
    for header in subsubheaders:
        
        # file.write(header + "\n")
        for niv in nivå:
            with open(pathout + str(counter)+niv[0] + ".md", "w") as file:
                for line in dictionary[header][niv]:
                    file.write(line)
        counter += 1

restructure('Splitting\\tallteori.md', 'converted\\tallteo')
restructure('Splitting\\funk.md', 'converted\\funk')
restructure('Splitting\\tall.md', 'converted\\tall')
restructure('Splitting\\geo.md', 'converted\\geo')
restructure('Splitting\\likninger.md', 'converted\\likn')
restructure('Splitting\\sannsyn.md', 'converted\\sannsyn')


################## DEL 2: ######################################
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






################## DEL 3: ######################################
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