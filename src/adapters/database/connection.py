from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão ao PostgreSQL
DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/mydatabase"

# Criação do engine
engine = create_engine(DATABASE_URL, echo=True)

# Criação do SessionLocal para gerenciar sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependência para obter uma sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()