import configparser
from sqlalchemy import Text, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()


class Documents(Base):
    __tablename__ = 'DOCUMENTS'

    document_id = Column(Integer(), primary_key=True)
    path = Column(Text())
    filename = Column(Text())
    document_text = Column(Text())
    table_text = Column(Text())
    last_modified_by = Column(Text())
    author = Column(Text())
    created = Column(Text())
    last_printed = Column(Text())
    revision = Column(Text())
    num_tables = Column(Text())


class Sections(Base):
    __tablename__ = 'SECTIONS'

    section_id = Column(Integer(), primary_key=True)
    filename = Column(Text())
    section_name = Column(Text())
    section_text = Column(Text())


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('../config.ini')
    DB_CONNECTION = config['USER']['DB_CONNECTION']

    # create database tables
    engine = create_engine(DB_CONNECTION)
    Base.metadata.create_all(engine)



