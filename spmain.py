import spacy
import pandas as pd
import re

nlp = spacy.load("en_core_web_sm")

current_name = None
current_location = None
current_job_title = None
current_org_title = None
current_phone = None
current_email = None
current_url = None

extracted_info = []

def process_sentence(sentence):
    """
    Process a sentence and extract information about people, their job titles, locations, phone numbers, email addresses, and URLs.
    """
    global current_name, current_location, current_job_title, current_org_title, current_phone, current_email, current_url

    doc = nlp(sentence)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            current_name = ent.text
        elif ent.label_ == "GPE":
            current_location = ent.text
        elif ent.label_ == "JOB_TITLE":
            current_job_title = ent.text
        elif ent.label_ == "ORG":
            current_org_title = ent.text
        elif ent.label_ == "PHONE":
            current_phone = ent.text
        elif ent.label_ == "EMAIL":
            current_email = ent.text
        elif ent.label_ == "URL":
            current_url = ent.text

    if current_name and (current_location or current_job_title):
        extracted_info.append({"Name": current_name, "Location": current_location, "Job Title": current_job_title,"ORG": current_org_title, "Phone": current_phone, "Email": current_email, "URL": current_url})

    # Reset the global variables
    current_name = None
    current_location = None
    current_job_title = None
    current_org_title = None
    current_phone = None
    current_email = None
    current_url = None

def extract_phone_numbers(text):
    """
    Extract phone numbers from the given text.
    """
    phone_regex = re.compile(r'\b(\+\d{1,3}\s?)?((\(\d{1,3}\))|\d{1,3})[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}\b')
    return phone_regex.findall(text)

def extract_email_addresses(text):
    """
    Extract email addresses from the given text.
    """
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Z-z0-9]+\.[A-Za-z]{2,}\b')
    return email_regex.findall(text)

def extract_urls(text):
    """
    Extract URLs from the given text.
    """
    url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return url_regex.findall(text)

with open("tesseract_file.txt", "r") as file:
    content = file.read()

    print("File Content:")
    print(content)

    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line:
            print("\nProcessing Line:")
            print(line)
            process_sentence(line)
            current_phone = extract_phone_numbers(line)
            current_email = extract_email_addresses(line)
            current_url = extract_urls(line)

file.close()

df = pd.DataFrame(extracted_info)
print("\nExtracted Information:")
print(df)

# Add the following line to print available categories
print("\nAvailable categories:", df.columns)

filter_category = input("Do you want to filter the search by category? (yes/no): ").lower()


if filter_category == "yes":
    category = input("Enter the category (Name/Location/Job Title/Org/Phone/Email/URL): ").capitalize()

    if category in df.columns:
        filter_value = input(f"Enter the {category} to filter by: ")
        filtered_df = df[df[category].str.contains(filter_value, case= False, na=False)]
        print("\nFiltered Results:")
        print(filtered_df)
    else:
        print(f"Invalid category '{category}'. Please enter a valid category (Name/Location/Job Title/Org/Phone/Email/URL).")
else:
    print("Search without filtering.")
