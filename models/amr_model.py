from shared.shared_libs_model import *

class Base(DeclarativeBase):
    pass

class AMR(Base):
    __tablename__ = "amrs"

    id: Mapped[int] = mapped_column(primary_key=True)
    hash: Mapped[str] = mapped_column(String(64))
    ecgains: Mapped[str] = mapped_column(String(16))
    bidno: Mapped[str] = mapped_column(String(22))
    title: Mapped[str] = mapped_column(String(40))
    broadcastdate: Mapped[str] = mapped_column(String(10))
    duedate: Mapped[str] = mapped_column(String(10))
    baseurl: Mapped[str] = mapped_column(String(100))
    fileurl: Mapped[str] = mapped_column(String(100))
    filename: Mapped[str] = mapped_column(String(100))