import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_markdown(content):
    subsubheaders = re.findall(r'### (.+)', content)
    unique_subsubheaders = list(set(subsubheaders))

    result = ""
    for ush in unique_subsubheaders:
        result += f"### {ush}\n"
        for keyword in ['grunnleggende', 'middels', 'avansert']:
            result += f"#### {ush} {keyword}\n"
            regex = re.compile(rf'#### {ush} {keyword}\n(.*?)\n(?!#)', re.DOTALL)
            matches = regex.findall(content)
            for match in matches:
                result += match
            result += "\n"
    return result

markdown_content = read_file('likninger.md')
processed_content = process_markdown(markdown_content)
write_file('likningertest.md', processed_content)
