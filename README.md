# README: Historical Data Extraction Project

## Overview

This project focuses on the extraction of historical data from the National Directory of College Athletics (NDCA) handbook, specifically the 2007-08 edition. By employing Optical Character Recognition (OCR) technology, specifically Tesseract, alongside Natural Language Processing (NLP) methods via SpaCy, and data manipulation with Pandas, we aim to convert the scanned images of the NDCA handbook into structured digital data. This structured data can then be used for various computational analyses, archival purposes, and to facilitate easier access to the information contained within the handbook.

## Project Structure

The project is divided into several key scripts and notebooks, each fulfilling a specific role in the process of converting the scanned handbook into structured, digital format:

### 1. Tesseract OCR Conversion (`tesseract_full_vol_read.ipynb`)

- **Purpose**: Converts scanned images of the NCDA handbook into a text file.
- **Input**: Scanned images located at `../ndca_2007_08/`.
- **Output**: A text file named `ncda_2007_08_tesseract_full_vol_read.txt` saved in the project's root directory.

### 2. Parsing the Index (`parsing_colleges.ipynb` and `./app/parsing_index.py`)

- **Purpose**: These files contain similar functionality, designed to convert the index portion of the Tesseract-generated text file into parsable, structured data.
- **Input**: The text file generated by `tesseract_full_vol_read.ipynb`.
- **Output**: Structured data representing the index of the handbook, facilitating easier access to specific sections or entries.

### 3. Parsing the Body (`./app/parsing_body.py`)

- **Purpose**: Similar to `parsing_index.py`, but focuses on parsing the body of the Tesseract-generated text file.
- **Input**: The text file generated by `tesseract_full_vol_read.ipynb`.
- **Output**: Structured data representing the body of the handbook, allowing for detailed analysis and retrieval of information.

## Requirements

- **Tesseract OCR**: For converting scanned images to text.
- **SpaCy**: For employing NLP techniques to process and understand the text.
- **Pandas**: For organizing the text into structured dataframes, making it easier to manipulate and analyze.

## Usage

To use this project, follow these steps:

1. **Prepare the scanned images**: Ensure all pages of the NDCA handbook are scanned and placed in the directory `../ndca_2007_08/`.
2. **Run Tesseract OCR Conversion**: Execute `tesseract_full_vol_read.ipynb` to convert the scanned images into a text file.
3. **Parse the Index and Body**: Use `parsing_colleges.ipynb`, `./app/parsing_index.py`, and `./app/parsing_body.py` as needed to parse different sections of the generated text file into structured data.
4. **Analyze and Utilize Data**: With the structured data, perform various computational analyses, archival tasks, or any other intended use case.

## Conclusion

By converting the NDCA handbook into a structured digital format, this project opens up new avenues for historical data analysis, archival, and research. The combination of OCR, NLP, and data manipulation technologies provides a powerful toolkit for handling and extracting meaningful information from scanned documents.
