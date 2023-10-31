from pdfreader import PDFDocument
import os
from tqdm import tqdm 

# Specify file directory here
pdf_path = r""

# Target export file
export_file = r""

# Preprocessing
files = []
directory = r"C:\Users\Yuan Ern\Desktop\IEOL"
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
        
    page_info = f"filename: {pdf_path}  |  landscape: {landscape}  |  portrait: {portrait}"

    return page_info

# Execution
file_data = []
export_location = open(export_file, "w")
for files_tp in tqdm(files, desc="Processing PDF files"):
    data = get_pdf_page_dimensions(files_tp) + "\n"
    export_location.write(data)

export_location.close()


