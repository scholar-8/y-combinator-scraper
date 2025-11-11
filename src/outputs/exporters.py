thonimport csv
import json

def export_to_csv(data, filename='output.csv'):
    """Exports the data to a CSV file."""
    if not data:
        return
    keys = data[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def export_to_json(data, filename='output.json'):
    """Exports the data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)