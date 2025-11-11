thonimport re

def extract_location(text):
    """Extracts location information from text."""
    location_pattern = r"Location: (.*)"
    match = re.search(location_pattern, text)
    return match.group(1) if match else "Unknown"

def clean_text(text):
    """Cleans up unnecessary whitespace from text."""
    return ' '.join(text.split())