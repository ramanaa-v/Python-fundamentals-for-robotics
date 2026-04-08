import re

def find_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    dates = re.findall(pattern, text)
    return dates

log_entry = 'Error reported on 18-02-2025 at node 3. Previous error was on 01-10-2024.'
found_dates = find_dates(log_entry)
print('Dates found:', found_dates)