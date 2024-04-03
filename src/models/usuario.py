import uuid

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.types import Uuid

from src.modules import db



class User(db.Model):
    __tablename__ = 'usuarios'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60),nullable=False)
    hash_password: Mapped[str] = mapped_column(String(256), nullable=False)


