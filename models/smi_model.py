from shared.shared_libs_model import *

class Base(DeclarativeBase):
    pass

class SMI(Base):
    __tablename__ = "smis"

    id: Mapped[int] = mapped_column(primary_key=True)
    hash: Mapped[str] = mapped_column(String(64), nullable=False)
    ecgains: Mapped[str] = mapped_column(String(21), nullable=False)
    bidno: Mapped[str] = mapped_column(String(20), nullable=False)
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    duedate: Mapped[str] = mapped_column(String(10), nullable=False)
    baseurl: Mapped[str] = mapped_column(String(150), nullable=False)
    fileurl: Mapped[str] = mapped_column(String(150), nullable=False)
    filename: Mapped[str] = mapped_column(String(150), nullable=False)
    filesize: Mapped[str] = mapped_column(String(10), nullable=False)