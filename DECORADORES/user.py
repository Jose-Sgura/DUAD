from datetime import date
class User:
    def __init__(self, name,date_of_birth):
        self.date_of_birth=date_of_birth
        self.name=name
    
    @property
    def age(self):
        today=date.today()
        years=today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

def require_adult(func):
        def joined(user, *args, **kwargs):
        
            if user.age < 18:
                raise ValueError("User must be legal age")
            return func(user, *args, **kwargs)

        return joined

@require_adult
def club_entrance(user):
    print(f"The booking is under the name of: {user.name}")


user1 = User("Ana", date(2000, 5, 10))
user2 = User("Luis", date(2010, 3, 20))
club_entrance(user1)


#extras
print("extra1")
def repeat_twice(again):
    def twice(*args, **kwargs):
        again(*args, **kwargs)
        again(*args, **kwargs)   
    return twice


@repeat_twice
def say_hi(name):
    print(f"Hola, {name}")



say_hi("Jeanca")

#extras2
print("extra2")
user_logged_in=False
def requires_login(user):
    def info(*args, **kwargs):
        if not user_logged_in:
            raise Exception("User not authenticated")
        return user(*args, **kwargs)
    return info


@requires_login
def profile():
    print("Showing the user profile")

print("Trying seeing the profile no authenticated:")

try:
    profile()
except Exception as e:
    print("Error:", e)

user_logged_in = True
print("\n Here the user is authenticated.")
print("Trying seeing the profile again:")