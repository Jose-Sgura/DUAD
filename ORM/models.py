from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(100), nullable = False)
    email = Column(String(120), nullable = False, unique = True)
    phone = Column(String(20), nullable = True)

    cars = relationship("Automobile", back_populates = "user")
    addresses = relationship(
        "Address", back_populates = "user", cascade = "all, delete-orphan"
        )
    def __repr__(self):
        return f"<User id = {self.id} name = {self.name!r} email = {self.email!r}>"
    
class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key = True, autoincrement = True)
    street = Column(String(150), nullable = False)
    city = Column(String(80), nullable = False)
    zip_code = Column(String(15), nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    user = relationship("User", back_populates = "addresses")

    def __repr__(self):
        return(
        f"<Address id = {self.id} Street = {self.street}, "
        f"city = {self.city} user_id = {self.user_id}>")
class Automobile(Base):
    __tablename__ = "automobiles"

    id = Column(Integer, primary_key = True, autoincrement = True)
    brand = Column(String(60), nullable = False)
    model = Column(String(60), nullable = True)
    year = Column(Integer, nullable = True)
    plate = Column(String(20), nullable = False, unique = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = True)
    user = relationship("User", back_populates = "cars")
    
    def __repr__(self):
        return ( f"<Automobile id = {self.id} brand = {self.brand!r} model = {self.model!r}, " 
        f"plate = {self.plate !r} user_id = {self.user_id}>"
        )