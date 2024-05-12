#!/bin/bash

tests_n=30
min_size=1000
max_size=50000
step=1000
# Путь к директории для сохранения результатов
results_dir="./dataset"

# Путь к директории с приложениями
apps_dir="./in_apps"

for exe_file in "$apps_dir"/*.exe; do
    # Извлекаем имя файла без расширения
    exe_name=$(basename "$exe_file")
    exe_name="${exe_name%.*}_in"
    
    # Создаем поддиректорию для текущего.exe файла, если она еще не существует
    mkdir -p "$results_dir/$exe_name"
    
    # Запускаем.exe файл с различными входными данными и сохраняем результаты
    echo "Запуск тестов для $exe_name..."
    for ((i=min_size; i<=max_size; i+=step)); do
        # Формируем команду для запуска.exe файла с входными данными
        command="echo $i > input.txt && $exe_file < input.txt"
        formatted_i=$(printf "%05d" "$i")
        (eval "$command") >> "$results_dir/$exe_name/$formatted_i.txt"
        # Удаляем input.txt после каждого запуска
        rm input.txt
    done
    echo "Тестирование $exe_name завершено."
done

apps_dir="./out_apps"

for exe_file in "$apps_dir"/*.exe; do
    # Извлекаем имя файла без расширения
    exe_name=$(basename "$exe_file")
    exe_name="${exe_name%.*}_out"
    
    # Создаем поддиректорию для текущего.exe файла, если она еще не существует
    mkdir -p "$results_dir/$exe_name"
    
    # Запускаем.exe файл с различными входными данными и сохраняем результаты
    echo "Запуск тестов для $exe_name..."
    for ((j=1; j<=tests_n; j++)); do
        echo "$j/$tests_n"
        for ((i=min_size; i<=max_size; i+=step)); do
            command="echo $i > input.txt && $exe_file < input.txt"
            formatted_i=$(printf "%05d" "$i")
            (eval "$command") >> "$results_dir/$exe_name/$formatted_i.txt"
            # Удаляем input.txt после каждого запуска
            rm input.txt
        done
    done
    echo "Тестирование $exe_name завершено."
done
echo "Все .exe файлы обработаны."
