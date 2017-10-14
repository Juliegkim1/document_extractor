# document_extractor
Extract and structure text from word documents.

document_extractor populates a database with two tables, Documents and Sections. The Documents table includes document properties and the full text of the document. The Sections table uses customizable hueristics to structure the documents into sections.


## Instructions

#### 1. Update config.ini:

Update the DB_CONNECTION AND RAW_DATA directory in the config.ini file. For instance, if the codebase is on your desktop, use the following paths with your own username:

##### DB_CONNECTION=sqlite:///C:\Users\INSERT YOUR USERNAME\Desktop\document_extractor\database\documents.db
##### RAW_DATA=C:\Users\INSERT YOUR USERNAME\Desktop\document_extractor\raw_data

#### 2. Raw Data:

Insert all documents that you want to extract and struture text from into the raw data directory. All documents must be .docx files, older versions of Microsoft Word (i.e. .doc) are not compatible. Please save non-compatible files as .docx for expected functionality.

#### 3. database/models.py:

In the database directory, run models.py to create the database

#### 4. main.py:

Run main.py to populate the database

#### 5. Analysis (optional)

To view results, open the analysis.ipynb Jupyter Notebook in the analysis directory. Pandas code is provided to connect to the database and view the results in the Documents and Sections tables.


#### 6. Alter the way that sections are created

Modify the following parameters (default is True for all) in the set_sections method in documents.document.py 

    :param use_headings: uses a header formatting (e.g. table of contents)
    :param use_capitalization: capitalization of every letter often indicates section header
    :param use_bold: all words in a sentence are bold
    :param use_underline: all words in a sentence are underlined
    :param use_bold_until_colon: all words in a sentence are bold until a colon (e.g. SECTION: ...)
    :param use_capital_letter_list: sentence starts with capital letter (e.g. A.)
    :param use_roman_numeral_list: sentence starts with a roman numeral (e.g. II.)
    :param ignore_bullets: ignore list of bullet points
