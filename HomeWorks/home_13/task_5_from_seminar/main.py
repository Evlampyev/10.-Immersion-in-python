from my_error import ValueInRangeError
from user import User
from company import Company

company = Company('Temp')
user = User('Alex-3', '3', 2)
print(user)
print(company)
company.add_user(user)

print(company)

# while True:
try:
    user_2 = User("Al", 4,9)
except ValueInRangeError as e:
    print(f'Я отхватил нужнную ошибку {e}')




