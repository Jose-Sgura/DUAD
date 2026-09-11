from models import User, Address, Automobile
from sqlalchemy import func

class UserManager:
    def __init__(self, session):
        self.session = session
    
    def create_user(self, name, email, phone = None):
        user = User(name = name, email = email, phone = phone)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def modify_user(self, user_id, **changes):
        user = self.session.get(User, user_id)
        if user is None:
            return None
        valid_fields = User.__table__.columns.keys()
        for field, value in changes.items():
            if field not in valid_fields:
                raise ValueError(f"'{field}' is not a valid field of User")
            setattr(user, field, value)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete_user(self, user_id):
        user = self.session.get(User, user_id)
        if user is None:
            return False
        self.session.delete(user)
        self.session.commit()
        return True
    
    def get_user(self, user_id):
        return self.session.get(User, user_id)
    def query_all(self):
        return self.session.query(User).all()
    
    def get_with_more_than_n_car(self, n = 1):
        return (
            self.session.query(User)
            .join(Automobile, Automobile.user_id == User.id)
            .group_by(User.id)
            .having(func.count(Automobile.id) > n)
            .all()
        )

class AutomobileManager:
    def __init__(self, session):
        self.session = session
    
    def create_automobile(self, brand, model, plate, year = None, user_id = None):
        automobile = Automobile(
            brand = brand, model = model, plate =  plate, year = year, user_id = user_id
        )
        self.session.add(automobile)
        self.session.commit()
        self.session.refresh(automobile)
        return automobile
    def modify_automobile(self, automobile_id, **changes):
        automobile = self.session.get(Automobile, automobile_id)
        if automobile is None:
            return None
        valid_fields = Automobile.__table__.columns.keys()
        for field, value in changes.items():
            if field not in valid_fields:
                raise ValueError(f"'{field}' is not a valid field of Automobile")
            setattr(automobile, field, value)
        self.session.commit()
        self.session.refresh(automobile)
        return automobile
    def delete_automobile(self, automobile_id):
        automobile = self.session.get(Automobile, automobile_id)
        if automobile is None:
            return False
        self.session.delete(automobile)
        self.session.commit()
        return True
    
    def affiliate_user(self,automobile_id, user_id):
        automobile = self.session.get(Automobile, automobile_id)
        user = self.session.get(User, user_id)
        if automobile is None or user is None:
            return False
        automobile.user_id = user.id
        self.session.commit()
        self.session.refresh(automobile)
        return automobile
    def unaffiliate_user(self, automobile_id):
        automobile = self.session.get(Automobile, automobile_id)
        if automobile is None:
            return None
        automobile.user_id = None
        self.session.commit()
        self.session.refresh(automobile)
        return automobile
    
    def query_all(self):
        return self.session.query(Automobile).all()
    
    def get_with_no_owner(self):
        return self.session.query(Automobile).filter(Automobile.user_id.is_(None)).all()
    
class AddressManager:
    def __init__(self, session):
        self.session = session

    def create_address(self, street, city, zip_code, user_id):
        user = self.session.get(User, user_id)
        if user is None:
            return None
        address = Address(
            street = street, city = city, zip_code = zip_code, user_id = user_id
        )
        self.session.add(address)
        self.session.commit()
        self.session.refresh(address)
        return address
    def modify_address(self, address_id, **changes):
        address = self.session.get(Address, address_id)
        if address is None:
            return None
        valid_fields = Address.__table__.columns.keys()
        for field, value in changes.items():
            if field not in valid_fields:
                raise ValueError(f"'{field}' is not a valid field of address")
            setattr(address, field, value)
        self.session.commit()
        self.session.refresh(address)
        return address
    def delete_address(self, address_id):
        address = self.session.get(Address, address_id)
        if address is None:
            return False
        self.session.delete(address)
        self.session.commit()
        return True
    def query_all(self):
        return self.session.query(Address).all()
    
    def look_for_street(self, text):
        return(
            self.session.query(Address)
            .filter(Address.street.ilike(f"%{text}%"))
            .all()       
        )