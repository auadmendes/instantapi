import re

def extract_case_details(text: str):
    subject_match = re.search(r"(?i)Subject:\s*(.*)", text)
    description_match = re.search(r"(?i)Description:\s*(.*)", text)
    extra_match = re.search(r"(?i)^\s*Extra(?: information)?:\s*(.*)", text, re.MULTILINE | re.DOTALL)
    
    subject = subject_match.group(1).strip() if subject_match else "No Subject Found"
    description = description_match.group(1).strip() if description_match else "No Description Found"
    extra = extra_match.group(1).strip() if extra_match else None
    
    return subject, description, extra
