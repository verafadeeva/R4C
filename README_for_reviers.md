## R4C

Если необходимо смотреть только файлы и код, которые относятся непосредственно к заданиям:
- [Task 1](https://github.com/verafadeeva/R4C/commit/ad6a9b814aa04bdbf7ab2b521b084c580c0f04ee)
- [Task 2](https://github.com/verafadeeva/R4C/commit/dafef0d5346ce4828d718e51f6b5a27f10aec697)
- [Task 3](https://github.com/verafadeeva/R4C/commit/8a5cb8bb0c0d25f31a1cd56475e9e2a01582a8bc)

### Endpoints

1. Создание робота
```
POST api/robot/create/
Content-Type: application/json

{
    "model": "R3",
    "version": "D5",
    "created": "2023-10-04 23:59:59"
}
```
2. Скачивание отчета в .xlsx
```
GET api/report/
```

### Installation

1. Клонируйте репозиторий

```
git clone git@github.com:verafadeeva/R4C.git
```
2. Установите виртуальное окружение
```
python3.9 -m venv .venv
```
3. Активируйте виртуальное окружение
```
source .venv/bin/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
5. Выполните миграции
```
python manage.py migrate
```
6. Загрузите тестовые данные в базу
```
python manage.py loaddata data.json
```
7. Запустите сервер
```
python manage.py runserver
```

### Authors

Вера Фадеева (lunatik.yar@gmail.com)
