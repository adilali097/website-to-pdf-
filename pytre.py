import pdfkit

# URL of the website to convert
url = 'https://www.geeksforgeeks.org/pattern-programs-in-c/'

# Path to save the PDF file
pdf_path = 'geeksforgeeks_patterns_in_c.pdf'

# Options for wkhtmltopdf
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

try:
    # Convert the website to PDF
    pdfkit.from_url(url, pdf_path, options=options)
    print("PDF created successfully!")
except Exception as e:
    print("An error occurred:", str(e))
