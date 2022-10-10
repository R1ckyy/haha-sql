from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:", echo=True)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name,
            self.fullname,
            self.nickname,
        )
    @staticmethod
    def filterName(name):
        return session.query(User).filter(User.name == name).all()
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
ed_user = User(name="ed", fullname="Ed Jones", nickname="edsnickname")
session.add(ed_user)
ed_user = User(name="ed1", fullname="Ed Jones", nickname="edsnickname")
session.add(ed_user)
ed_user = User(name="ed1", fullname="Ed Jones", nickname="edsnickname")
session.add(ed_user)
for row in session.query(User).all():
    print(row.id, row.name)
obj = session.query(User).filter(User.name == "ed").one()
session.delete(obj)
session.commit()
for row in User.filterName("ed1"):
    print(row.id, row.name)
