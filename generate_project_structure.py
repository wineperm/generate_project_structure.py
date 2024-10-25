import os

def generate_project_structure(root_dir, output_file):
    def print_tree(root, prefix=''):
        # Пропускаем директорию .git
        if '.git' in root:
            return
        # Записываем путь к текущей директории относительно root_dir
        relative_path = os.path.relpath(root, root_dir)
        if relative_path == '.':
            relative_path = ''
        # Записываем директорию
        if relative_path:
            f.write(f"{prefix}├── {os.path.basename(root)}/\n")
        else:
            f.write(f"{prefix}├── {os.path.basename(root)}/\n")
        # Записываем файлы в текущей директории
        for file in sorted(os.listdir(root)):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                # Пропускаем сам скрипт, его файл вывода и дополнительные файлы
                if file in [os.path.basename(__file__), output_file, 'info.tai', 'create_structure.py', 'read_files.py']:
                    continue
                f.write(f"{prefix}│   ├── {file}\n")
            elif os.path.isdir(file_path):
                print_tree(file_path, prefix + '│   ')

    with open(output_file, 'w') as f:
        f.write(f"{os.path.basename(root_dir)}/\n")
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)
            if os.path.isfile(item_path):
                # Пропускаем сам скрипт, его файл вывода и дополнительные файлы
                if item in [os.path.basename(__file__), output_file, 'info.tai', 'create_structure.py', 'read_files.py']:
                    continue
                f.write(f"├── {item}\n")
            elif os.path.isdir(item_path):
                print_tree(item_path, '├── ')

if __name__ == "__main__":
    # Получаем текущую директорию, где запущен скрипт
    current_dir = os.getcwd()
    # Указываем имя выходного файла
    output_file = 'project_structure.txt'
    # Генерируем структуру проекта
    generate_project_structure(current_dir, output_file)
    print(f"Project structure has been written to {output_file}")
