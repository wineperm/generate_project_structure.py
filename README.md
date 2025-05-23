# generate_project_structure.py
```
wget https://raw.githubusercontent.com/wineperm/generate_project_structure.py/main/generate_project_structure.py
```
### Описание

Скрипт на Python рекурсивно обходит все файлы и директории в указанной корневой директории и записывает их структуру в выходной файл `project_structure.txt`. Скрипт позволяет исключить определенные файлы и директории из обхода.

### Инструкция

#### Сохранение скрипта:

1. Сохраните этот скрипт в файл с именем `generate_project_structure.py`.

#### Настройка параметров:

1. Убедитесь, что скрипт находится в корневой директории проекта, который вы хотите обработать.
2. В переменной `output_file` укажите путь к файлу, в который будет записана структура проекта.
3. В переменной `exclude_files` укажите множество имен файлов, которые нужно исключить из обхода.
4. В переменной `exclude_dirs` укажите множество имен директорий, которые нужно исключить из обхода.

#### Запуск скрипта:

1. Откройте терминал или командную строку.
2. Перейдите в директорию, где находится скрипт `generate_project_structure.py`.
3. Запустите скрипт с помощью команды:
   ```sh
   python3 generate_project_structure.py
   ```

### Пример использования

#### Создание структуры проекта:

1. Создайте директорию `my_project` с несколькими файлами и поддиректориями.
2. Поместите скрипт `generate_project_structure.py` в корневую директорию `my_project`.

#### Настройка скрипта:

1. Откройте скрипт `generate_project_structure.py` и убедитесь, что переменные `output_file`, `exclude_files` и `exclude_dirs` настроены правильно.
   Например:
   ```python
   output_file = os.path.join(current_dir, 'project_structure.txt')
   exclude_files = {'project_structure.txt', 'generate_project_structure.py', 'info.tai', 'create_structure.py', 'read_files.py'}
   exclude_dirs = {'.git'}
   ```

#### Запуск скрипта:

1. Откройте терминал и перейдите в директорию `my_project`.
2. Запустите скрипт:
   ```sh
   python3 generate_project_structure.py
   ```

#### Проверка результата:

1. После завершения работы скрипта в корневой директории `my_project` появится файл `project_structure.txt`, содержащий структуру всех файлов и директорий, исключая указанные в `exclude_files` и `exclude_dirs`.

### Пример вывода

Предположим, что структура вашего проекта выглядит следующим образом:

```
my_project/
├── main.py
├── utils/
│   ├── helper.py
│   └── config.py
├── data/
│   ├── dataset1.csv
│   └── dataset2.csv
└── .git/
```

После запуска скрипта `generate_project_structure.py`, файл `project_structure.txt` будет содержать следующее:

```
my_project/
├── main.py
├── utils/
│   ├── helper.py
│   └── config.py
├── data/
│   ├── dataset1.csv
│   └── dataset2.csv
```

### Заключение

Этот скрипт полезен для автоматизации процесса создания структуры проекта, что может быть полезно для различных задач, таких как создание резервных копий, анализ кода или генерация документации.
