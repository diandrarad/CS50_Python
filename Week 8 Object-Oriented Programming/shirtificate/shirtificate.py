from fpdf import FPDF


class Shirtificate():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(20)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font(style="B")
        text_width = self._pdf.get_string_width(f"{name} took CS50")
        x = (self._pdf.epw - text_width) / 1.7
        self._pdf.text(x=x, y=140, txt=f"{name} took CS50")

    def generate(self, filename):
        # Output the PDF to a file
        self._pdf.output(filename)

# Prompt the user for their name
name = input("Enter your name: ")

# Generate the shirtificate PDF
shirtificate = Shirtificate(name)
shirtificate.generate("shirtificate.pdf")