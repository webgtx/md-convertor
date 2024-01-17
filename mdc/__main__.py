from weasyprint import HTML
from fire import Fire
from markdown2 import markdown

class MDC:
    def __init__(self):
        self.html_buffer = str()
        self.work_dir = path.dirname(__file__)

    def pdf(self, inputfile: str, outputfile: str):
        with open(inputfile, "r") as f:
            self.html_buffer = markdown(f.read())
            HTML(string=self.html_buffer).write_pdf(outputfile)

Fire(MDC)
