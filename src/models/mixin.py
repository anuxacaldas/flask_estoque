
from typing import Optional


from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime
from sqlalchemy import func

class DataMixin:
    dta_cadastro: Mapped[DateTime] = mapped_column(DateTime,
                                            server_default=func.now(),
                                            nullable=False)

    dta_atualizacao: Mapped[Optional[DateTime]] = mapped_column(DateTime,
                                                                onupdate=func.now(),
                                                                default=func.now(),
                                                                nullable=True)
