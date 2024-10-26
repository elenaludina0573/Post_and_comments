## Ваша задача — разработать приложение, в котором пользователи могут писать посты и комментировать их.

Создайте модели и соответствующие точки API для взаимодействия с ними.

___Технические требования:___

* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

### Структура приложения

#### Задача 1 

### МОДЕЛИ

### ___Модель пользователя___                     

* логин
* пароль
* номер
* дата рождения
* дата создания
* дата редактирования

### ___Модель поста___

* заголовок
* текст
* изображение (если есть)
* автор
* комментарии
* дата создания
* дата редактирования

### ___Модель комментария___

* автор
* текст
* дата создания
* дата редактирования

#### Примечание: связи между моделями определите самостоятельно.

#### Задача 2
### ЭНДПОИНТЫ

Реализуйте CRUD для каждой модели.

### ___Пользователь:___

* CREATE: все пользователи (регистрация).
* READ: администратор/авторизованные пользователи.
* UPDATE: администратор/пользователь может редактировать только себя./
* DELETE: администратор.

### ___Пост:___

* CREATE: авторизованные пользователи.
* READ: все пользователи.
* UPDATE: администратор/пользователь может редактировать только себя.
* DELETE: администратор/пользователь может удалять свои посты.

### ___Комментарий:___

* CREATE: авторизованные пользователи.
* READ: все пользователи.
* UPDATE: администратор/пользователь может редактировать только себя.
* DELETE: администратор/пользователь может удалять свои комментарии.

#### Задача 3
### ВАЛИДАТОРЫ

___Модель пользователя___

* Реализуйте валидатор для пароля (должен быть не менее 8 символов, должен включать цифры).

* Реализуйте валидатор для почты (разрешены домены: mail.ru, yandex.ru).

___Модель поста___

* Реализуйте проверку того, что автор поста достиг возраста 18 лет.

* Реализуйте проверку, что автор в заголовок не вписал запрещенные слова: ерунда, глупость, чепуха.

#### Задача 4
### АДМИН. ПАНЕЛЬ

* Добавьте в объекте поста ссылку на автора.

* Добавьте фильтр по дате создания поста.


### Руководство по использованию проекта

___Клонируйте репозиторий:git clone___

https://github.com/elenaludina0573/Post_and_comments

___Установите зависимости:___

pip install -r requirements.txt

___Примените миграции:___

python manage.py makemigrations

python manage.py migrate

___Создайте суперпользователя:___

python manage.py csu

___Запустите сервер разработки:___

python manage.py runserver

