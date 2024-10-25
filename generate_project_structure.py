import os

def generate_project_structure(root_dir, output_file):
    def print_tree(root, prefix=''):
        # Пропускаем директорию .git
        if '.git' in root:
            return
        # Записываем файлы и директории в текущей директории
        items = sorted(os.listdir(root))
        for i, item in enumerate(items):
            item_path = os.path.join(root, item)
            if os.path.isfile(item_path):
                # Пропускаем сам скрипт, его файл вывода и дополнительные файлы
                if item in [os.path.basename(__file__), output_file, 'info.tai', 'create_structure.py', 'read_files.py']:
                    continue
                if i == len(items) - 1:
                    f.write(f"{prefix}└── {item}\n")
                else:
                    f.write(f"{prefix}├── {item}\n")
            elif os.path.isdir(item_path):
                new_prefix = prefix + '│   ' if i < len(items) - 1 else prefix + '    '
                if i == len(items) - 1:
                    f.write(f"{prefix}└── {item}/\n")
                else:
                    f.write(f"{prefix}├── {item}/\n")
                print_tree(item_path, new_prefix)

    with open(output_file, 'w') as f:
        f.write(f"{os.path.basename(root_dir)}/\n")
        print_tree(root_dir, '    ')

if __name__ == "__main__":
    # Получаем текущую директорию, где запущен скрипт
    current_dir = os.getcwd()
    # Указываем имя выходного файла
    output_file = 'project_structure.txt'
    # Генерируем структуру проекта
    generate_project_structure(current_dir, output_file)
    print(f"Project structure has been written to {output_file}")
