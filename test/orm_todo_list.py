# Test ORM for to do list app

from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(63), nullable=False)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    lists: Mapped[List["Lists"]] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        return (f'User(id={self.id!r}, username={self.username!r},'
                f' name={self.name!r}, fullname={self.fullname!r})')


class Lists(Base):
    __tablename__ = 'list'
    id: Mapped[int] = mapped_column(primary_key=True)
    list_name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship(back_populates='lists')
    tasks: Mapped[List["Task"]] = relationship(back_populates='list',
                                               cascade='all, delete')

    def __repr__(self) -> str:
        return f'Lists(id={self.id!r}, list_name={self.list_name!r})'


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    task_info: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    list_id: Mapped[int] = mapped_column(ForeignKey('list.id'))
    user: Mapped["User"] = relationship(back_populates='addresses')
    list: Mapped["List"] = relationship(back_populates='tasks')

    def __repr__(self) -> str:
        return f'Tasks(id={self.id!r}, task_info={self.task_info!r})'
