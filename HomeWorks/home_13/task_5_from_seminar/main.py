from user import User
from company import Company

company = Company('Temp')
user = User('Alex-3', '3', 2)
print(user)
print(company)
company.add_user(user)

print(company)

