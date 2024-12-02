import os

def generate_report_structure(checklist, base_path="generated_report"):
    """Generates the folder and file structure of the report based on the checklist."""
    # Create the base report folder
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # Iterate through the checklist and create folders for each section
    for section in checklist:
        section_folder = os.path.join(base_path, section['name'])
        if not os.path.exists(section_folder):
            os.makedirs(section_folder)
        
        # Create a placeholder file for each section if no content is present
        if 'content' not in section:
            with open(os.path.join(section_folder, "placeholder.txt"), 'w') as f:
                f.write("This section requires content based on the checklist.")
    
    print(f"Report structure generated at {base_path}")

import os

file_path = r"task2\documents\CertificateOfCompletion_Build GANs and Diffusion Models with TensorFlow and PyTorch.pdf"
print("File exists:", os.path.exists(file_path))
