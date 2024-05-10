#!/bin/bash

# Путь к директории с приложениями
apps_dir="./apps"

# Путь к директории для сохранения результатов
results_dir="./dataset"

rm -rf "${results_dir:?}"/*
mkdir -p "$results_dir"

for exe_file in "$apps_dir"/*.exe; do
    # Извлекаем имя файла без расширения
    echo "Обработка файла: $exe_file"
    exe_name=$(basename "$exe_file")
    exe_name="${exe_name%.*}"
    
    # Создаем поддиректорию для текущего.exe файла, если она еще не существует
    mkdir -p "$results_dir/$exe_name"
    
    # Запускаем.exe файл с различными входными данными и сохраняем результаты
    echo "Запуск тестов для $exe_name..."
    for i in {1000..100000..500}; do
        # Формируем команду для запуска.exe файла с входными данными
        command="echo $i > input.txt && $exe_file < input.txt"
        
        # Запускаем команду и сохраняем результат в файл
        echo "Обработка входных данных: $i"
        formatted_i=$(printf "%05d" "$i")
        (eval "$command") > "$results_dir/$exe_name/$formatted_i.txt"
        # Удаляем input.txt после каждого запуска
        rm input.txt
    done
    echo "Тестирование $exe_name завершено."
done
echo "Все .exe файлы обработаны."
