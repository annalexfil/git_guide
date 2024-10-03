# Слияние веток

Слияние веток (merging) — это процесс объединения изменений из одной ветки в другую. Это важный аспект работы с Git, который позволяет интегрировать работу разных разработчиков или разных частей проекта.

## Основные команды для слияния

- `git merge <branch>`: Сливает изменения из указанной ветки в текущую ветку.
- `git checkout <branch>`: Переключается на указанную ветку.
- `git branch`: Показывает список всех веток.

## Процесс слияния

1. Переключитесь на ветку, в которую хотите влить изменения**:
```sh
   git checkout main
```
2. Слейте изменения из другой ветки:

```sh
git merge feature-branch
```
3. Разрешите конфликты, если они возникли:

- Git автоматически объединяет изменения, но иногда могут возникнуть конфликты, которые нужно разрешить вручную.
После разрешения конфликтов, добавьте измененные файлы и завершите слияние:
    ```sh 
  git add <file>
    git commit 
  ```

## Пример слияния

Предположим, у вас есть две ветки: `main` и `feature-branch`. Вы хотите влить изменения из feature-branch в main.

1. Переключитесь на ветку `main`:

```sh
git checkout main
```
2. Слейте изменения из feature-branch:

```sh
git merge feature-branch
```
3. Если возникли конфликты, разрешите их вручную, затем добавьте измененные файлы и завершите слияние:

```sh
git add <file>
git commit
```
## Упражнения

#### Упражнение 1: Простое слияние

Создайте новую ветку `feature-branch` и переключитесь на нее:

```sh
git checkout -b feature-branch
```
Внесите изменения в `feature-branch` и закоммитьте их:

```sh
echo "New feature" >> feature.txt
git add feature.txt
git commit -m "Add new feature"
```
Переключитесь обратно на ветку `main`:

```sh
git checkout main
```

Слейте изменения из `feature-branch` в `main`:

```sh
git merge feature-branch
```
#### Упражнение 2: Разрешение конфликтов

Создайте новую ветку `conflict-branch` и переключитесь на нее:

```sh
git checkout -b conflict-branch
```
Внесите изменения в `conflict-branch` и закоммитьте их:

```sh
echo "Conflict content" >> conflict.txt
git add conflict.txt
git commit -m "Add conflict content"
```
Переключитесь обратно на ветку `main` и внесите изменения в тот же файл:

```sh
git checkout main
echo "Main content" >> conflict.txt
git add conflict.txt
git commit -m "Add main content"
```
Слейте изменения из `conflict-branch` в main:

```sh
git merge conflict-branch
```
Разрешите конфликты вручную, затем добавьте измененные файлы и завершите слияние:

```sh
git add conflict.txt
git commit
```
#### Следующий урок

После того как вы освоили слияние веток, перейдите к следующему уроку: [Решение конфликтов слияния](level2-advanced/03-conflict-resolution.md).
