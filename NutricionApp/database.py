from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'postgresql://nutricionapp_rzuk_user:kWPcQqdeZSu4osYCrCJIf6AIHShqflqb@dpg-chs0o3e4dadfn67en5g0-a.oregon-postgres.render.com/nutricionapp_rzuk'
engine = create_engine(SQLALCHAMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
