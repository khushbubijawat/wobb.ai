import streamlit as st
from extract_text import extract_text_from_pdf, extract_text_from_image, extract_text_from_url
from entity_recognition import extract_entities
from relationship_extraction import extract_relationships
from property_extraction import extract_properties
from graph_creation import create_knowledge_graph

def process_document(document_path, document_type="pdf"):
    # Step 1: Extract text from the document
    if document_type == "pdf":
        text = extract_text_from_pdf(document_path)
    elif document_type == "image":
        text = extract_text_from_image(document_path)
    elif document_type == "url":
        text = extract_text_from_url(document_path)

    # Step 2: Extract entities, relationships, and properties
    entities = extract_entities(text)
    relationships = extract_relationships(text)
    properties = extract_properties(text)

    # Step 3: Create Knowledge Graph
    create_knowledge_graph(entities, relationships, properties)

    # Step 4: Display Success Message
    st.success("Knowledge graph created successfully.")
    
    # Optional: Display the extracted entities, relationships, and properties
    st.subheader("Entities")
    st.write(entities)
    
    st.subheader("Relationships")
    st.write(relationships)
    
    st.subheader("Properties")
    st.write(properties)

# Streamlit App UI
st.title("Knowledge Graph Creation from Documents")
st.write("Upload a document (PDF/Image) to create a knowledge graph.")

# File uploader for PDF or Image
uploaded_file = st.file_uploader("Choose a PDF or Image file", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Get the file type (PDF or Image)
    file_type = uploaded_file.type.split("/")[0]  # 'application' for pdf or 'image' for image files
    
    if file_type == "application":
        # Process the PDF file
        process_document(uploaded_file, document_type="pdf")
    elif file_type == "image":
        # Process the image file
        process_document(uploaded_file, document_type="image")
