import os
import shutil

def process_file(file_path):
    # Проверяем, что файл существует и имеет расширение.txt
    if not os.path.isfile(file_path) or not file_path.endswith('.txt'):
        return
    # Извлекаем название приложения из пути к файлу
    app_name = os.path.basename(os.path.dirname(file_path))
    x = int(os.path.basename(file_path).split(".")[0])
    
    # Открываем исходный файл и новый файл для записи
    with open(file_path, 'r') as src_file:
        # Читаем исходный файл построчно
        lines = src_file.readlines()
        min_value = float(lines[0].split(': ')[1])  # Извлекаем значение MIN
        max_value = float(lines[1].split(': ')[1])  # Извлекаем значение MAX
        mean_value = float(lines[2].split(': ')[1])  # Извлекаем значение MEAN
        rse_value = float(lines[3].split(': ')[1])  # Извлекаем значение RSE
        l_qurtile = float(lines[4].split(': ')[1])
        median = float(lines[5].split(': ')[1])
        u_qurtile = float(lines[6].split(': ')[1])
    
    new_file_path = f'./plot_data/linear/{app_name}.txt'
    os.makedirs('./plot_data/linear/', exist_ok=True)
    with open(new_file_path, 'a') as dst_file:
        dst_file.write(f'{x} {mean_value}\n')
    
    new_file_path = f'./plot_data/error/{app_name}.txt'
    os.makedirs('./plot_data/error/', exist_ok=True)
    with open(new_file_path, 'a') as dst_file:
        dst_file.write(f'{x} {mean_value} {max_value} {min_value}\n')
    
    new_file_path = f'./plot_data/mustache/{app_name}.txt'
    os.makedirs('./plot_data/mustache/', exist_ok=True)
    with open(new_file_path, 'a') as dst_file:
        dst_file.write(f'{x} {min_value} {l_qurtile} {mean_value} {u_qurtile} {max_value}\n')
    


def sort_file_by_first_column(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Сортировка строк по первому столбцу как числам
    sorted_lines = sorted(lines, key=lambda line: float(line.split()[0]))
    
    # Запись отсортированных строк обратно в файл
    with open(filename, 'w') as file:
        file.writelines(sorted_lines)


for root, dirs, files in os.walk('./plot_data/'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            os.remove(file_path)

# Проходим по всем файлам в директории./preprocessed/
for root, dirs, files in os.walk('./preprocessed/'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            process_file(file_path)

for root, dirs, files in os.walk('./plot_data/'):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            sort_file_by_first_column(file_path)




print("Обработка завершена.")
