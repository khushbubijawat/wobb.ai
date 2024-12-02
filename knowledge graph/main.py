from extract_text import extract_text_from_pdf, extract_text_from_image, extract_text_from_url
from entity_recognition import extract_entities
from relationship_extraction import extract_relationships
from property_extraction import extract_properties
from graph_creation import create_knowledge_graph

def process_document(document_path, document_type="pdf"):
    
    if document_type == "pdf":
        text = extract_text_from_pdf(document_path)
    elif document_type == "image":
        text = extract_text_from_image(document_path)
    elif document_type == "url":
        text = extract_text_from_url(document_path)

    
    entities = extract_entities(text)
    

    relationships = extract_relationships(text)
    
  
    properties = extract_properties(text)
  
    create_knowledge_graph(entities, relationships, properties)
    print("Knowledge graph created successfully.")


process_document("question 73 rpsc.pdf", document_type="pdf")  # For PDF
process_document("withtext.jpg", document_type="image")  # For Image
#process_document("http://example.com/product_spec", document_type="url")  # For URL
