#!/bin/bash

echo "Очистка скомпилированных файлов"
rm -rf ./apps
echo "Компиляция файлов..."
./build_apps.sh

echo "Обновление данных..."
./update_data.sh

echo "Очистка файлов препроцессинга"
rm -rf ./preprocessed
echo "Препроцессинг..."
python3 make_preproc.py

echo "Очистка файлов постпроцессинга"
rm -rf ./plot_data
echo "Постпроцессинг..."
python3 make_postproc.py

echo "Очистка графиков"
rm -rf ./plots
echo "Построение графиков..."
./plot_graphs.sh

echo "Все скрипты успешно выполнены."
