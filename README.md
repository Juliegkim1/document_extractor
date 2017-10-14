# document_extractor
Extract and structure text from word documents

## Instructions

### 1. Update config.ini:

Update the DB_CONNECTION AND RAW_DATA directory in the config.ini file. For instance, if the codebase is on your desktop, use the following paths with your own username:

##### DB_CONNECTION=sqlite:///C:\Users\INSERT YOUR USERNAME\Desktop\document_extractor\database\documents.db
##### RAW_DATA=C:\Users\INSERT YOUR USERNAME\Desktop\document_extractor\raw_data

### 2. Raw Data:

Insert all documents that you want to extract and struture text from into the raw data directory. All documents must be .docx files, older versions of Microsoft Word (i.e. .doc) are not compatible. Please save non-compatible files as .docx for expected functionality.

### 3. main.py:

Run main.py to populate the database

### 4. Analysis (option)

To view results, open the analysis.ipynb Jupyter Notebook in the analysis directory. Pandas code is provided to connect to the database and view the results in the Documents and Sections tables.