# Stellar Burgers — UI Test Automation

Учебный проект по автоматизации UI-тестирования веб-приложения [Stellar Burgers](https://stellarburgers.education-services.ru).

Тесты написаны на Python с использованием Selenium WebDriver, Pytest, Page Object Model и Allure.

> **Статус:** проект создан для учебного тестового стенда. Доступность приложения на момент просмотра репозитория не подтверждена; актуальный успешный прогон тестов не заявляется.

## Стек

- Python
- Selenium WebDriver
- Pytest
- Allure Pytest
- Page Object Model (POM)
- Chrome и Firefox

## Тестовые сценарии

### Конструктор бургеров
- Переход к конструктору.
- Переход к ленте заказов.
- Открытие окна с деталями ингредиента.
- Закрытие окна с деталями ингредиента.
- Увеличение счётчика ингредиента при добавлении в заказ.

### Лента заказов
- Изменение счётчика «Выполнено за всё время» после заказа.
- Изменение счётчика «Выполнено за сегодня» после заказа.
- Отображение номера созданного заказа в разделе «В работе».

## Структура проекта

```text
Diplom_3/
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   ├── feed_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_constructor.py
│   └── test_feed.py
├── utils/
│   ├── data.py
│   └── locators.py
├── requirements.txt
└── README.md
```

- `pages/` — Page Object-классы и общие методы работы с интерфейсом.
- `tests/` — тесты и фикстуры Pytest.
- `utils/` — локаторы и тестовые данные.

## Установка

Требуется Python, установленный Chrome и/или Firefox и доступ к учебному стенду.

```bash
git clone https://github.com/Denis-Kostomarkin/Diplom_3.git
cd Diplom_3
python -m venv .venv
```

Активация окружения:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## Запуск тестов

В Chrome:

```bash
pytest tests/ --browser=chrome
```

В Firefox:

```bash
pytest tests/ --browser=firefox
```

Для тестов создания заказа необходима действующая тестовая учётная запись. В текущей версии её данные задаются в `utils/data.py`. Учебный стенд может быть недоступен или изменён, поэтому запуск и результаты зависят от его состояния.

## Отчёт Allure

```bash
pytest tests/ --browser=chrome --alluredir=allure-results
```

При установленном Allure CLI:

```bash
allure serve allure-results
```

## Особенности реализации

- Page Object Model для разделения логики тестов и взаимодействия с UI.
- Фикстуры Pytest для запуска и закрытия браузера.
- Выбор браузера через параметр `--browser`.
- Явные ожидания Selenium.
- Allure-аннотации тестовых сценариев.

## Автор

[Denis-Kostomarkin](https://github.com/Denis-Kostomarkin)
