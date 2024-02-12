from weasyprint import HTML

# URL of the website to convert
url = 'https://www.geeksforgeeks.org/pattern-programs-in-c/'

# Path to save the PDF file
pdf_path = 'geeksforgeeks_patterns_in_c.pdf'

try:
    # Generate PDF from the website
    HTML(url).write_pdf(pdf_path)
    print("PDF created successfully!")
except Exception as e:
    print("An error occurred:", str(e))
