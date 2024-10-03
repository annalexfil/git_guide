import os


# Функция для создания директории и файлов
def create_directory_structure(base_path, structure):
    for item in structure:
        path = os.path.join(base_path, item["path"])
        if item["type"] == "directory":
            os.makedirs(path, exist_ok=True)
            if "contents" in item:
                create_directory_structure(path, item["contents"])
        elif item["type"] == "file":
            with open(path, "w", encoding="utf-8") as file:
                file.write(item["content"])


# Определяем структуру репозитория
structure = [
    {"path": "README.md", "type": "file", "content": "# Гид по Git\n\nОписание курса..."},
    {"path": "level1-basics", "type": "directory", "contents": [
        {"path": "01-introduction.md", "type": "file", "content": "# Введение в Git\n\n..."},
        {"path": "02-basic-commands.md", "type": "file", "content": "# Основные команды Git\n\n..."},
        {"path": "03-repositories.md", "type": "file", "content": "# Понимание репозиториев\n\n..."},
        {"path": "04-commits.md", "type": "file", "content": "# Концепция коммитов\n\n..."},
        {"path": "05-local-repositories.md", "type": "file",
         "content": "# Настройка и использование локальных репозиториев\n\n..."},
        {"path": "exercises", "type": "directory", "contents": [
            {"path": "exercise-1.md", "type": "file", "content": "# Упражнение 1\n\n..."},
            {"path": "exercise-2.md", "type": "file", "content": "# Упражнение 2\n\n..."}
        ]}
    ]},
    {"path": "level2-advanced", "type": "directory", "contents": [
        {"path": "01-branching.md", "type": "file", "content": "# Работа с ветками\n\n..."},
        {"path": "02-merging.md", "type": "file", "content": "# Слияние веток\n\n..."},
        {"path": "03-conflict-resolution.md", "type": "file", "content": "# Решение конфликтов слияния\n\n..."},
        {"path": "04-tags.md", "type": "file", "content": "# Использование тегов\n\n..."},
        {"path": "05-stash.md", "type": "file", "content": "# Сохранение изменений (stash)\n\n..."},
        {"path": "exercises", "type": "directory", "contents": [
            {"path": "exercise-1.md", "type": "file", "content": "# Упражнение 1\n\n..."},
            {"path": "exercise-2.md", "type": "file", "content": "# Упражнение 2\n\n..."}
        ]}
    ]},
    {"path": "level3-teamwork", "type": "directory", "contents": [
        {"path": "01-remote-repositories.md", "type": "file", "content": "# Работа с удаленными репозиториями\n\n..."},
        {"path": "02-pull-requests.md", "type": "file", "content": "# Использование pull requests\n\n..."},
        {"path": "03-code-reviews.md", "type": "file", "content": "# Код-ревью\n\n..."},
        {"path": "04-collaborative-project-management.md", "type": "file",
         "content": "# Совместное управление проектами\n\n..."},
        {"path": "exercises", "type": "directory", "contents": [
            {"path": "exercise-1.md", "type": "file", "content": "# Упражнение 1\n\n..."},
            {"path": "exercise-2.md", "type": "file", "content": "# Упражнение 2\n\n..."}
        ]}
    ]},
    {"path": "resources", "type": "directory", "contents": [
        {"path": "cheat-sheet.md", "type": "file", "content": "# Шпаргалка по Git\n\n..."},
        {"path": "best-practices.md", "type": "file", "content": "# Лучшие практики работы с Git\n\n..."},
        {"path": "additional-reading.md", "type": "file", "content": "# Дополнительные материалы для чтения\n\n..."}
    ]},
    {"path": ".gitignore", "type": "file", "content": "# .gitignore\n\n# Игнорируемые файлы\n*.log\n*.tmp\n..."}
]

# Создаем структуру репозитория
create_directory_structure("/Users/macbook/IdeaProjects/git_guide/", structure)

print("Структура репозитория успешно создана.")
