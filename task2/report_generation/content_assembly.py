from utils.text_extraction import extract_text_from_pdf, extract_text_from_image

def assemble_report_content(checklist, documents):
    """Assembles content for the report sections from the documents."""
    for section in checklist:
        if 'content' not in section:
            section_keywords = section['name'].split()  # Split the section name into keywords
            content = ""
            for doc in documents:
                doc_text = ""
                if doc['type'] == 'pdf':
                    doc_text = extract_text_from_pdf(doc['path'])
                elif doc['type'] == 'image':
                    doc_text = extract_text_from_image(doc['path'])
                # Extract relevant content for the section
                content += extract_content_from_document(doc_text, section_keywords)
            
            section['content'] = content if content else "No relevant content found."
    
    return checklist

def extract_content_from_document(document, section_keywords):
    """Extracts content based on the section keywords."""
    content = ""
    for keyword in section_keywords:
        if keyword.lower() in document.lower():
            content += f"Found information related to {keyword}: {document[:300]}\n"
    return content
