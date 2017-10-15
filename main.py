import os
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Documents, Sections
from documents.document import Document

config = configparser.ConfigParser()
config.read('config.ini')
DB_CONNECTION = config['USER']['DB_CONNECTION']
RAW_DATA = config['USER']['RAW_DATA']


def main():
    engine = create_engine(DB_CONNECTION)
    Session = sessionmaker(bind=engine)
    session = Session()

    for filename in os.listdir(RAW_DATA):
        print('Opening document: {}'.format(filename))
        path = os.path.join(RAW_DATA, filename)
        doc = Document(path)

        # create an instance (database row) for a annual report
        document = Documents(
            path=doc.path
            , filename=filename
            , document_text=doc.text
            , table_text=doc.table_text
            , last_modified_by=doc.last_modified_by
            , author=doc.author
            , created=doc.created
            , last_printed=doc.last_printed
            , revision=doc.revision
            , num_tables=doc.num_tables
        )
        session.add(document)

        for section_name, section_text in doc.sections.items():
            section = Sections(
                filename=filename
                , section_name=section_name
                , section_text=section_text
            )
            session.add(section)

        session.commit()


if __name__ == "__main__": main()




