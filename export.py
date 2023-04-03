import os
import pypandoc


files = []
args = ["--css=styling.css",
        "--mathjax",
        "--toc",
        "--toc-depth=3",
        "--template=template.html",
        #  "-s", "-o"
        ]

for file in os.listdir("./"):
    if file.endswith(".md"):
        print(file)
        print(os.path.splitext(file)[0])
        fileoutpdf = os.path.splitext(file)[0] + ".pdf"
        fileouthtml = os.path.splitext(file)[0] + ".html"
        pypandoc.convert_file(file, to="html", outputfile=fileouthtml, extra_args=[
            "--css=styling.css",
            "--mathjax",
            "--toc",
            "--toc-depth=3",
            "--template=template.html",
            "-s",
            "--include-in-header=styling.css"])
        pypandoc.convert_file(file,
                            "pdf",
                            outputfile=fileoutpdf,
                            extra_args=["--pdf-engine=xelatex",
                                        "--variable=block-headings"
                                        ],)
