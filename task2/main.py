# from report_generation.report_structure import generate_report_structure
# from report_generation.content_assembly import assemble_report_content
# from report_generation.summary_generation import generate_summary
# from report_generation.post_processing import add_bookmarks_to_pdf
# from dynamic_checklist.checklist_parser import parse_checklist
# from utils.text_extraction import extract_text_from_pdf, extract_text_from_image
# import pytesseract

# # Ensure Tesseract is in the PATH or explicitly set the path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust if necessary


# def main():
#     # 1. Load checklist
#     checklist = parse_checklist("checklist.json")
    
   
#     documents = [
#         {"type": "pdf", "path": "C:\\Users\\HP\\OneDrive\\Desktop\\wobb.ai\\task2\\documents\\market.pdf"},
#         {"type": "image", "path": "C:\\Users\\HP\\OneDrive\\Desktop\\wobb.ai\\task2\\documents\\withtext.jpg"}
#     ]
    
#     # 3. Generate report structure based on the checklist
#     generate_report_structure(checklist, base_path="C:\\Users\\HP\\OneDrive\\Desktop\\wobb.ai\\task2\\generated_report\\final_report.pdf")
    
#     # 4. Assemble content for the report
#     populated_report = assemble_report_content(checklist, documents)
    
#     # 5. Generate summary section
#     summary = generate_summary(populated_report)
#     print(summary)
    
#     # 6. Post-process the report (e.g., adding bookmarks to the PDF)
#     add_bookmarks_to_pdf("generated_report/final_report.pdf", "generated_report/final_report_with_bookmarks.pdf")

# if __name__ == "__main__":
#     main()

import os
from report_generation.report_structure import generate_report_structure
from report_generation.content_assembly import assemble_report_content
from report_generation.summary_generation import generate_summary
from report_generation.post_processing import add_bookmarks_to_pdf
from dynamic_checklist.checklist_parser import parse_checklist
from utils.text_extraction import extract_text_from_pdf, extract_text_from_image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust if necessary

def main():
    
    try:
        checklist = parse_checklist("checklist.json")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    
    documents = [
        {"type": "pdf", "path": r"C:\Users\HP\OneDrive\Desktop\wobb.ai\task2\documents\market.pdf"},
        {"type": "image", "path": r"C:\Users\HP\OneDrive\Desktop\wobb.ai\task2\documents\withtext.jpg"}
    ]
    
    if not os.path.exists("generated_report"):
        os.makedirs("generated_report")
    
    try:
        generate_report_structure(checklist, base_path=r"C:\Users\HP\OneDrive\Desktop\wobb.ai\task2\generated_report\final_report.pdf")
    except Exception as e:
        print(f"Error generating report structure: {e}")
        return
    
    try:
        populated_report = assemble_report_content(checklist, documents)
    except Exception as e:
        print(f"Error assembling report content: {e}")
        return
    
    try:
        summary = generate_summary(populated_report)
        print(summary)
    except Exception as e:
        print(f"Error generating summary: {e}")
        return
    
    
    add_bookmarks_with_permission_check("generated_report/final_report.pdf", "generated_report/final_report_with_bookmarks.pdf")


def add_bookmarks_with_permission_check(input_pdf_path, output_pdf_path):
    
    if not os.path.exists(input_pdf_path):
        print(f"Error: The file '{input_pdf_path}' does not exist.")
        return
    
    try:
        
        with open(input_pdf_path, 'rb') as f:
            pass  

        
        add_bookmarks(input_pdf_path, output_pdf_path)
    except PermissionError as e:
        print(f"Permission Error: {e}")
        print("Ensure that the file is not open in any other program and you have the necessary permissions.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
