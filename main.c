#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_REPEATS 10000
#define MAX_N 200000

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

double calculate_relative_standard_error(long arr[], int n)
{
    double mean;
    double m_sum = 0;
    for (size_t i = 0; i < n; i++)
    {
        m_sum += arr[i];
    }
    mean = m_sum / n;
    double sq_sum = 0;
    for (size_t i = 0; i < n; i++)
    {
        sq_sum += pow((arr[i] - mean), 2);
    }
    sq_sum = sq_sum / (n - 1);
    double standard_deviation = sqrt(sq_sum);
    double standard_error = standard_deviation / sqrt(n);
    double rse = (standard_error / mean) * 100;
    return rse;
}

void copyArray(int *src, int *dest, int size)
{
    for (int i = 0; i < size; i++)
    {
        dest[i] = src[i];
    }
}

int main()
{
    size_t n;
    scanf("%zu", &n);

    int arr_for_sort[MAX_N];
    int arr[MAX_N];
    srand(time(NULL));

    double rse = 100;
    struct timespec start, end;
    long data[MAX_REPEATS];
    size_t data_n = 0;

    for (size_t i = 0; i < n; i++)
    {
        arr_for_sort[i] = rand() % 100;
    }

    while (rse >= 1)
    {
        copyArray(arr_for_sort, arr, n);
        clock_gettime(CLOCK_MONOTONIC_RAW, &start);

        selection_sort(arr, n);

        clock_gettime(CLOCK_MONOTONIC_RAW, &end);

        long ticks = end.tv_sec * 1000000000L + end.tv_nsec - start.tv_sec * 1000000000L - start.tv_nsec;
        data[data_n] = ticks;
        data_n++;
        if (data_n > 1)
        {
            rse = calculate_relative_standard_error(data, data_n);
        }
        if (data_n >= MAX_REPEATS)
        {
            break;
        }
    }

    for (size_t i = 0; i < data_n; i++)
        printf("%ld ", data[i]);
    return 0;
}
