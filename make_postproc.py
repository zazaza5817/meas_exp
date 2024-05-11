import os
import matplotlib.pyplot as plt

# Функция для чтения данных из файла
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        min_value = float(lines[0].split(': ')[1])  # Извлекаем значение MIN
        max_value = float(lines[1].split(': ')[1])  # Извлекаем значение MAX
        mean_value = float(lines[2].split(': ')[1])  # Извлекаем значение MEAN
        rse_value = float(lines[3].split(': ')[1])  # Извлекаем значение RSE
    return min_value, max_value, mean_value, rse_value

# Функция для построения графика
def plot_graph(app_name, data):
    # Сортируем данные по ключам (число элементов массива)
    sorted_data = dict(sorted(data.items()))
    
    # Линейный график
    plt.figure(figsize=(10, 6))
    plt.plot(list(sorted_data.keys()), [value[2] for value in sorted_data.values()], marker='o', linestyle='-')
    plt.title(f'Линейный график ({app_name})')
    plt.xlabel('Число элементов массива')
    plt.ylabel('Время выполнения (среднее)')
    plt.grid(True)
    plt.savefig(f'{app_name}_linear_graph.svg')
    
    # График с ошибками
    plt.figure(figsize=(10, 6))
    # Преобразуем список списков ошибок в одномерный список
    print("======")
    errors_min = [error[0] for error in sorted_data.values()]
    errors_max = [error[1] for error in sorted_data.values()]
    # errors = [(error[0], error[1]) for error in sorted_data.values()]
    plt.errorbar(list(sorted_data.keys()), [value[2] for value in sorted_data.values()], yerr=[errors_min, errors_max], fmt='o', capsize=5)
    plt.plot(list(sorted_data.keys()), errors_max, marker='o', linestyle='-')
    plt.plot(list(sorted_data.keys()), errors_min, marker='o', linestyle='-')
    plt.title(f'График с ошибками ({app_name})')
    plt.xlabel('Число элементов массива')
    plt.ylabel('Время выполнения (среднее)')
    plt.grid(True)
    plt.savefig(f'{app_name}_error_graph.svg')



# Основная функция для обработки всех файлов и построения графиков
def process_files_and_plot_graphs():
    base_dir = './preprocessed'
    for app_name in os.listdir(base_dir):
        if not os.path.isdir(os.path.join(base_dir, app_name)):
            continue
        data = {}
        for file_name in os.listdir(os.path.join(base_dir, app_name)):
            if not file_name.endswith('.txt'):
                continue
            file_path = os.path.join(base_dir, app_name, file_name)
            min_value, max_value, mean_value, rse_value = read_data_from_file(file_path)
            num_elements = int(file_name.split('.')[0])
            data[num_elements] = (min_value, max_value, mean_value, rse_value)
        plot_graph(app_name, data)

if __name__ == '__main__':
    process_files_and_plot_graphs()
