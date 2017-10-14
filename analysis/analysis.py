import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Documents, Sections

config = configparser.ConfigParser()
config.read('../config.ini')
DB_CONNECTION = config['USER']['DB_CONNECTION']

engine = create_engine(DB_CONNECTION)
Session = sessionmaker(bind=engine)
session = Session()

'''
results = session.query(Documents).all()
for result in results:
    print('document_id: {}'.format(result.document_id))
    print('path: {}'.format(result.path))
    print('last_modified_by: {}'.format(result.last_modified_by))
    print('author: {}'.format(result.author))
    print('created: {}'.format(result.created))
    print('last_printed: {}'.format(result.last_printed))
    print('revision: {}'.format(result.revision))
    print('num_tables: {}'.format(result.num_tables))
    print('document_text: {}'.format(result.document_text))
    print('table_text: {}'.format(result.table_text))
    print()
'''

results = session.query(Sections).all()
for result in results:
    print('section_id: {}'.format(result.section_id))
    print('document_name: {}'.format(result.document_name))

    try:
        print('section_name: {}'.format(result.section_name))
        print('section_text: {}'.format(result.section_text))
    except UnicodeEncodeError:
        print('encode error')
    print()














