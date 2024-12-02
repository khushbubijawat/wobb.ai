from PyPDF2 import PdfReader, PdfWriter

def add_bookmarks(input_pdf_path, output_pdf_path):
    """Adds bookmarks to a PDF."""
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])
    

    writer.add_bookmark("Introduction", 0)
    writer.add_bookmark("Summary", 1)
    
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)
    print("Bookmarks added successfully.")
