from faker import Faker

faker = Faker('ru_RU')

def generate_registration_data():
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password  # Возвращаем кортеж (name, email, password)
