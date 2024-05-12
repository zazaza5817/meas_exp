#!/bin/bash

# Проверяем, существует ли директория apps, если нет - создаем
if [ ! -d "./in_apps" ]; then
    mkdir ./in_apps
    echo "Создание папки для скомпилированных файлов"
fi

# Проверяем, существует ли директория apps, если нет - создаем
if [ ! -d "./out_apps" ]; then
    mkdir ./out_apps
    echo "Создание папки для скомпилированных файлов"
fi

for file in ./in_c_files/*.c; do
    # Получаем имя файла без расширения
    name=$(basename "$file")
    name="${name%.*}"
    # Компилируем файл и сохраняем результат в папку apps с тем же именем
    gcc "$file" -o "./in_apps/$name.exe" -lm -O0
done

for file in ./out_c_files/*.c; do
    # Получаем имя файла без расширения
    name=$(basename "$file")
    name="${name%.*}"
    # Компилируем файл и сохраняем результат в папку apps с тем же именем
    gcc "$file" -o "./out_apps/$name.exe" -lm -O0
done

echo "Компиляция завершена"
