import re

def extract_properties(text):
    properties = {}

    # Example: Extract price (e.g., "$999")
    price_match = re.search(r'\$([\d,]+(?:\.\d{1,2})?)', text)
    if price_match:
        properties['price'] = price_match.group(0)

    # Example: Extract size (e.g., "6.5 inches")
    size_match = re.search(r'(\d+(\.\d+)?)\s*(inches|cm|mm)', text)
    if size_match:
        properties['size'] = size_match.group(0)

    return properties
