import os
import pypandoc

args = ["--css=styling.css",
             "--mathjax",
             "--toc",
             "--toc-depth=3",
             "--template=template.html",
            #  "-s", "-o"
             ]

for file in os.listdir("./quizzer/"):
    if file.endswith(".md"):
        fileout = os.path.splitext(file)[0] + ".pdf"
        print(file)
        # pypandoc.convert_file(file, to = "html", outputfile= fileout, extra_args=[
        #     "--css=styling.css",
        #      "--mathjax",
        #      "--toc",
        #      "--toc-depth=3",
        #      "--template=template.html",
        #      "-s"])
        fil = "./quizzer/" + file
        pypandoc.convert_file(  fil, 
                                "pdf",
                                outputfile= fileout,
                                 extra_args=
                                 ["--pdf-engine=xelatex",
                                 "--variable=block-headings"
                                 ],)
