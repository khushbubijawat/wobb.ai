import json

def parse_checklist(checklist_path):
    """Parses the checklist from a JSON file."""
    with open(checklist_path, "r") as file:
        checklist = json.load(file)
    return checklist
