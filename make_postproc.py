import os
import matplotlib.pyplot as plt

# Функция для чтения данных из файла
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        mean = float(lines[2].split(': ')[1])  # Извлекаем значение mean
    return mean

# Функция для построения графика
def plot_graph(app_name, data):
    # Сортируем данные по ключам (числу элементов массива)
    sorted_data = dict(sorted(data.items()))
    
    plt.figure(figsize=(10, 6))
    plt.plot(list(sorted_data.keys()), list(sorted_data.values()), marker='o', linestyle='-')
    plt.title(f'Время выполнения ({app_name})')
    plt.xlabel('Число элементов массива')
    plt.ylabel('Время выполнения (среднее)')
    plt.grid(True)
    plt.savefig(f'{app_name}_graph.svg')

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
            mean = read_data_from_file(file_path)
            num_elements = int(file_name.split('.')[0])
            data[num_elements] = mean
        plot_graph(app_name, data)

if __name__ == '__main__':
    process_files_and_plot_graphs()
