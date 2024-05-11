#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define MAX_N 200000
#define FILE_NAME "temp_times.txt"

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

double calculate_relative_standard_error(size_t n)
{
    double mean;
    double m_sum = 0;
    long cur_term;
    FILE *file = fopen(FILE_NAME, "r");


    for (size_t i = 0; i < n; i++)
    {
        fscanf(file, "%ld", &cur_term);
        m_sum += cur_term;
    }
    mean = m_sum / n;
    double sq_sum = 0;
    for (size_t i = 0; i < n; i++)
    {
        fscanf(file, "%ld", &cur_term);
        sq_sum += pow((cur_term - mean), 2);
    }
    sq_sum = sq_sum / (n - 1);
    double standard_deviation = sqrt(sq_sum);
    double standard_error = standard_deviation / sqrt(n);
    double rse = (standard_error / mean) * 100;
    return rse;
}


int main()
{
    FILE *file = fopen(FILE_NAME, "w");
    fclose(file);

    size_t n;
    scanf("%zu", &n);

    int arr[MAX_N];
    srand(time(NULL));

    double rse = 100;
    long ticks;
    struct timespec start, end;
    size_t data_n = 0;



    while (rse >= 1)
    {
        for (size_t i = 0; i < n; i++)
        {
            arr[i] = rand() % 100;
        }
        clock_gettime(CLOCK_MONOTONIC_RAW, &start);
        selection_sort(arr, n);
        clock_gettime(CLOCK_MONOTONIC_RAW, &end);

        ticks = end.tv_sec * 1000000000L + end.tv_nsec - start.tv_sec * 1000000000L - start.tv_nsec;

        FILE *file = fopen(FILE_NAME, "a");
        fprintf(file, "%ld ", ticks);
        printf("%ld ", ticks);
        fclose(file);

        arr[0] = arr[1];
        arr[1] = 1234;
        data_n++;
        if (data_n > 1)
            rse = calculate_relative_standard_error(data_n);
    }

    return 0;
}
