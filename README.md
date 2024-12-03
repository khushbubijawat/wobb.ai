# wobb.ai

Extracting Text and Creating a Knowledge Graph
1. Prerequisites
Before running the project, ensure that you have the following installed on your machine:

Neo4j Database: You can either use a local Neo4j installation or a cloud instance like Neo4j Aura.
To install Neo4j locally, follow Neo4j installation guide.
Or, use Neo4j Aura (free tier available) at Neo4j Aura.
Required Python Libraries: Install all required libraries by running the following command in your terminal or command prompt:
bash

pip install -r requirements.txt
The requirements.txt should contain the following dependencies:


py2neo
pytesseract
pdfminer.six
beautifulsoup4
requests
streamlit
2. Setting up Neo4j

Local Setup: If you're using a local Neo4j instance, ensure Neo4j is running and accessible on bolt://localhost:7687 (default).
The default credentials are: username: neo4j, password: password.
Cloud Setup: If you're using Neo4j Aura, replace the connection URL in your code with your Neo4j Aura connection details:
python
Copy code
graph = Graph("bolt://<your-neo4j-uri>:7687", auth=("neo4j", "<your-password>"))
3. Running the Document Processing Pipeline
Step 1: Extract Text

The text extraction functions handle three types of input sources:
PDF: Use the extract_text_from_pdf() function (uses pdfminer.six).
Image: Use the extract_text_from_image() function (uses pytesseract).
URL: Use the extract_text_from_url() function (uses requests and BeautifulSoup).
Step 2: Entity Recognition

The extract_entities() function processes the extracted text and identifies key entities (e.g., people, places, organizations).
Step 3: Relationship Extraction

The extract_relationships() function analyzes the text to identify relationships between the entities.
Step 4: Property Extraction

The extract_properties() function detects key properties related to the entities, such as dates, locations, or values.
Step 5: Knowledge Graph Creation

The create_knowledge_graph() function takes the entities, relationships, and properties, and adds them to the Neo4j graph.
