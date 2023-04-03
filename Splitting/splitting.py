import re
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
        if line.startswith('#### '):
            for niv in nivå:
                if re.search(niv, line, re.IGNORECASE):
                    current_nivå = niv
                    if re.search("vurderingskriterier", line, re.IGNORECASE):
                        dictionary[current_subsubheader][niv].append("#### Vurderingskriterier " + niv + ": " + current_subheader)    
                    else:
                        dictionary[current_subsubheader][niv].append("#### " + niv.capitalize() + ": " + current_subheader)
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