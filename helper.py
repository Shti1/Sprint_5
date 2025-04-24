from faker import Faker

faker = Faker('ru_RU')

def generate_registration_data():
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password  # Возвращаем кортеж (name, email, password)

# Генерация тестовых данных
name, email, password = generate_registration_data()

# Вывод в консоль
print("Сгенерированные тестовые данные:")
print(f"Имя: {name}")
print(f"Email: {email}")
print(f"Пароль: {password}")