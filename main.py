from pypdf import PdfReader
import os
from tqdm import tqdm 

# Specify file directory here
directory = r""

# Target export file
export_file = r""

# Preprocessing
files = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.abspath(directory) + "\\" + filename
        files.append(filepath)

# Magic here
def get_pdf_page_dimensions(pdf_path):
    reader = PdfReader(pdf_path)
    portrait, landscape = 0, 0 

    for page_num in range(len(reader.pages)):
        page_width = reader.pages[page_num].mediabox[2]
        page_height = reader.pages[page_num].mediabox[3]

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


