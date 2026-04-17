import re

def extract_data(filename):
    with open(filename, 'r') as file:
        text = file.read()

    names = re.findall(r'\b([A-Z][a-z]+\s[A-Z][a-z]+)\b', text)
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    phones = re.findall(r'\+91[-.\s]?\d{10}|\d{5}[-.\s]?\d{5}', text)
    dates = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b', text)

    print("Extracted Indian Names:", names)
    print("Extracted Emails:", emails)
    print("Extracted Phone Numbers:", phones)
    print("Extracted Dates:", ["/".join(date) for date in dates])

extract_data("sample.txt")
