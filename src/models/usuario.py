import uuid

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.types import Uuid
from werkzeug.security import generate_password_hash, check_password_hash

from models.mixin import DataMixin
from src.modules import db



class User(db.Model, DataMixin):
    __tablename__ = 'usuarios'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60),nullable=False)
    email_normalizado: Mapped[str] = mapped_column(String(256), nullable=False, unique=True, index=True)
    hash_password: Mapped[str] = mapped_column(String(256), nullable=False)

    @property
    def email(self):
        return self

    @email.setter
    def email(self, value: str):
        self.email_normalizado = value.lower()

        def set_password(self, password):
            self.password_hash = generate_password_hash(password)

        def check_password(self, password) -> bool:
            return check_password_hash(self.password_hash, password)