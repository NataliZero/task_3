import requests

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)

# Проверяем статус-код
print(response.status_code)

# Выводим ответ
print(response.json())
