#!/bin/bash

# Запуск build_apps.sh
echo "Запуск build_apps.sh..."
./build_apps.sh

# Запуск update_data.sh
echo "Запуск update_data.sh..."
./update_data.sh

# Запуск make_preproc.py
echo "Запуск make_preproc.py..."
python3 make_preproc.py

# Запуск make_postproc.py
echo "Запуск make_postproc.py..."
python3 make_postproc.py

mkdir plots
gnuplot mustache.gpi
gnuplot linear.gpi
gnuplot errors.gpi
echo "Все скрипты успешно выполнены."
