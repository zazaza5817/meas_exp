#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_REPEATS 100000

void selection_sort(int arr[], size_t n)
{
    size_t i, j;
    size_t min_index;
    int temp;
    for (i = 0; i < n - 1; i++)
    {
        min_index = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_index])
            {
                min_index = j;
            }
        }
        temp = arr[min_index];
        arr[min_index] = arr[i];
        arr[i] = temp;
    }
}
double calculate_mean(long arr[], int n)
{
    long sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    return (double)sum / n;
}
double calculate_standard_deviation(long arr[], int n)
{
    double mean = calculate_mean(arr, n);
    double sq_sum = 0;
    for (int i = 0; i < n; i++)
    {
        sq_sum += pow(arr[i] - mean, 2);
    }
    return sqrt(sq_sum / (n - 1));
}
double calculate_relative_standard_error(long arr[], int n)
{
    double standard_deviation = calculate_standard_deviation(arr, n);
    double mean = calculate_mean(arr, n);
    return (standard_deviation / mean) * 100;
}

void copyArray(int* src, int* dest, int size) {
    // Копируем элементы из исходного массива в новый
    for (int i = 0; i < size; i++) {
        dest[i] = src[i];
    }
}

int main()
{
    size_t n;
    printf("Введите количество элементов в массиве: ");
    scanf("%zu", &n);

    int arr_for_sort[n];
    int arr[n];
    srand(time(NULL)); // Инициализация генератора случайных чисел

    double total_time = 0;
    size_t repeats = 0;
    double mean_time;
    double rse = 100;
    struct timespec start, end;
    long data[MAX_REPEATS];
    size_t data_n = 0;

    for (size_t i = 0; i < n; i++)
    {
        arr_for_sort[i] = rand() % 100;
    }

    do
    {
        copyArray(arr_for_sort, arr, n);
        clock_gettime(CLOCK_MONOTONIC_RAW, &start); // Запуск таймера перед сортировкой

        selection_sort(arr, n);

        clock_gettime(CLOCK_MONOTONIC_RAW, &end); // Остановка таймера после сортировки

        long ticks = end.tv_sec * 1000000000L + end.tv_nsec - start.tv_sec * 1000000000L - start.tv_nsec;
        data[data_n] = ticks;
        printf("%zu: %ld\n", data_n, ticks);
        data_n ++;
        if (data_n > 1)
        {
            rse = calculate_relative_standard_error(data, data_n);
        }
        if (data_n >= MAX_REPEATS)
        {
            printf("ERROR MAXIMUM REPEATS REACHED\n");
            break;
        }
        printf("repeats: %zu, rse: %lf\n", data_n, rse);
    } while (rse > 1);
    printf("====RESULT====");
    printf("Размер исходного массива: %zu\n", n);
    printf("Среднее время: %.2f ticks\n", calculate_mean(data, data_n));
    printf("Количество повторов: %zu\n", data_n);
    printf("RSE: %.2lf\n", rse);

    return 0;
}
