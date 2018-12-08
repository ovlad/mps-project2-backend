from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_connect_string = 'mysql://mps2admin@mps2db:ParolaSecure1!@mps2db.mysql.database.azure.com/mps2projectdev2'
ssl_args = {'ssl': ''}
engine = create_engine(db_connect_string, connect_args=ssl_args, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Doctor, Donation, Donor, Employee, Hospital, Request, TransfusionCenter
    Base.metadata.create_all(bind=engine)
    return engine.table_names()


