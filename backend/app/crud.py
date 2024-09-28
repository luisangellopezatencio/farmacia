from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas
import re


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).all()

def get_user_by_username(db: Session, username: str):
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_user_login(db: Session, user_identifier: str):
    # Expresión regular para detectar correo electrónico
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_regex, user_identifier):
        # Si es un correo electrónico
        return db.query(models.Usuario.email, models.Usuario.password).filter(
            models.Usuario.email == user_identifier,
        ).first()
    else:
        # Si es un nombre de usuario (texto plano)
        return db.query(models.Usuario.username, models.Usuario.password).filter(
            models.Usuario.username == user_identifier,
        ).first()


def get_all_medicamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medicamento).all()

def get_all_transacciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransaccionMedicamento).all()