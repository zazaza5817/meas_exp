import os
import math
import shutil
import numpy as np

def get_relative_standard_error(arr):
    mean = get_mean(arr)
    sq_sum = sum((x - mean) ** 2 for x in arr)
    n = len(arr)
    variance = sq_sum / (n - 1)
    standard_deviation = math.sqrt(variance)
    standard_error = standard_deviation / math.sqrt(n)
    rse = (standard_error / mean) * 100
    return rse

def get_mean(arr):
    return sum(arr) / len(arr)

def calculate_percentiles(arr):
    lower_quartile = np.percentile(arr, 25)
    median = np.percentile(arr, 50)
    upper_quartile = np.percentile(arr, 75)
    return lower_quartile, median, upper_quartile

def process(content):
    data = [int(time) for time in content.split()]
    res = f"MIN: {min(data)}\n"
    res += f"MAX: {max(data)}\n"
    res += f"MEAN: {get_mean(data)}\n"
    res += f"RSE: {get_relative_standard_error(data)}\n"
    lower_quartile, median, upper_quartile = calculate_percentiles(data)
    res += f"LOWER QUARTILE: {lower_quartile}\n"
    res += f"MEDIAN: {median}\n"
    res += f"UPPER QUARTILE: {upper_quartile}\n"
    res += f"REPEATS: {len(data)}\n"
    return res


# Путь к исходной директории
source_dir = './dataset/'
# Путь к целевой директории
target_dir = './preprocessed/'

# Очищаем целевую директорию перед началом обработки
if os.path.exists(target_dir):
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    
# Перебираем все поддиректории в source_dir
for subdir, _, files in os.walk(source_dir):
    # Перебираем все файлы в текущей поддиректории
    for file in files:
        # Проверяем, что файл соответствует шаблону
        if not file.endswith('.txt'):
            continue
        # Полный путь к исходному файлу
        source_file_path = os.path.join(subdir, file)
        # Полный путь к целевому файлу
        target_file_path = os.path.join(target_dir, os.path.relpath(subdir, source_dir), file)
            
        # Создаем целевую директорию, если она не существует
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        
        # Открываем исходный файл для чтения
        with open(source_file_path, 'r') as src_file:
            # Читаем содержимое файла
            content = src_file.read()
        processed_content = process(content)
        with open(target_file_path, 'w') as tgt_file:
            # Записываем содержимое в целевой файл
            tgt_file.write(processed_content)

print("Обработка завершена.")
