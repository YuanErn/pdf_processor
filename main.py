from pdfreader import PDFDocument
import os

# File Directory here
directory = r""
files = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.abspath(directory) + "\\" + filename
        files.append(filepath)

# Magic here
def get_pdf_page_dimensions(pdf_path):
    pdf = PDFDocument(open(pdf_path, 'rb'))
    portrait, landscape = 0, 0 

    all_pages = [p for p in pdf.pages()]

    for page in all_pages:
        page_width = page.MediaBox[2]
        page_height = page.MediaBox[3]

        if page_width > page_height:
            landscape += 1
        else:
            portrait += 1
        
    page_info = {
        'filename': pdf_path,
        'landscape': landscape,
        'portrait': portrait
    }

    return page_info

# The loop for processing
file_data = []
for files_tp in files:
    data = get_pdf_page_dimensions(files_tp)
    file_data.append(data)

print(file_data)
