import spacy

def extract_information(data):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(data)

    patterns = [
        [{"LOWER": "cornerstone"}, {"LOWER": "university"}],
        [{"LOWER": "covenant"}, {"LOWER": "college"}],
        [{"ENT_TYPE": "GPE"}],
        [{"SHAPE": "ddd-ddd-dddd"}],
        [{"LOWER": "affiliation"}, {"IS_PUNCT": True}, {"IS_ALPHA": True}]
    ]

    matcher = spacy.matcher.Matcher(nlp.vocab)
    for i, pattern in enumerate(patterns):
        matcher.add(f"Pattern_{i}", None, pattern)

    information = {}
    for match_id, start, end in matcher(doc):
        label = nlp.vocab.strings[match_id]
        information[label] = doc[start:end].text

    return information

def main():
    file_path = "CornellUni.txt"  # Replace with the actual file path
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    extracted_info = extract_information(data)

    print("Extracted Information:")
    for key, value in extracted_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
