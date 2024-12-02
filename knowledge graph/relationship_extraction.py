import spacy

# Load the SpaCy model for dependency parsing
nlp = spacy.load("en_core_web_sm")

def extract_relationships(text):
    doc = nlp(text)
    relationships = []
    
    # Extract subject-verb-object relationships
    for token in doc:
        if token.dep_ == 'ROOT':
            subject = None
            verb = token
            obj = None
            
            # Get subject and object related to the verb
            for child in verb.lefts:
                if child.dep_ == 'nsubj':
                    subject = child
            for child in verb.rights:
                if child.dep_ in ['dobj', 'prep']:
                    obj = child
            
            if subject and obj:
                relationships.append({
                    'subject': subject.text,
                    'relationship': verb.text,
                    'object': obj.text
                })
    
    return relationships
