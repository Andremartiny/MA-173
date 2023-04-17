import os
import pypandoc
import datetime


args = ["--css=styling.css",
        "--mathjax",
        "--toc",
        "--toc-depth=3",
        "--template=template.html",
        #  "-s", "-o"
        ]

for file in os.listdir("./Splitting"):
    if file.endswith(".md"):
        if file == "geo.md" or file == "tallteori.md":
            continue
        # if file != "tallteori copy.md":
        #     continue
        file = f"./Splitting/{file}"
        print(file)
        date = datetime.date.today().strftime("%Y-%m-%d")
        print(os.path.splitext(file)[0])
        fileout_pdf = f"{os.path.splitext(file)[0]}_{date}.pdf"
        fileout_html = os.path.splitext(file)[0] + ".html"
        # pypandoc.convert_file(file, to="html", outputfile=fileout_html, extra_args=[
        #     "--css=styling.css",
        #     "--mathjax",
        #     "--toc",
        #     "--toc-depth=3",
        #     "--template=template.html",
        #     "-s",
        #     "--include-in-header=styling.css"])
        pypandoc.convert_file(file,
                            "pdf",
                            outputfile=fileout_pdf,
                            extra_args=["--pdf-engine=xelatex",
                                        "--variable=block-headings",
                                        ],)
