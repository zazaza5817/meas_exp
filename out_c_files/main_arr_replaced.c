#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

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
            if (*(arr+j) < *(arr+min_index))
            {
                min_index = j;
            }
        }
        temp = *(arr+min_index);
        *(arr+min_index) = *(arr+i);
        *(arr+i) = temp;
    }
}


int main()
{
    size_t n;
    scanf("%zu", &n);

    int arr[MAX_N];
    srand(time(NULL));

    long ncesecs;
    struct timespec start, end;
    size_t data_n = 0;

    for (size_t i = 0; i < n; i++)
    {
        arr[i] = rand() % 1000;
    }
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
    selection_sort(arr, n);
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);

    ncesecs = end.tv_sec * 1000000000L + end.tv_nsec - start.tv_sec * 1000000000L - start.tv_nsec;

    printf("%ld ", ncesecs);

    arr[0] = arr[1];
    arr[1] = 1234;
    

    return 0;
}
