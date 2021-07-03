#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define OK                        0
#define Error_invalid_param      -1
#define Error_incorrect_element  -2
#define Error_no_data            -3

int input(int a[][10], int n, int m)
{
    if (a == NULL || n < 0 || n > 10 || m < 0 || m > 10)
        return Error_invalid_param;
    if (n == 0 || m == 0)
        return Error_no_data;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("Input [%d][%d] element:", i, j);
            if (scanf("%d", &(a[i][j])) != 1)
                return Error_incorrect_element;
            if (a[i][j] < -2147483647)
                return Error_incorrect_element;
        }
    }

    return 0;
}



int fibonachchi_petuh(int n)
{
    int counter = 1;
    int prev = 1;
    int cur = 1;
    int fib = 1;

    while(counter <= n)
    {
        if (counter > 2)
        {
            fib = cur + prev;
            prev = cur;
            cur = fib;
        }
        counter += 1;
    }

    return fib;
}

void input_tests(void)
{
    int err_counter = 0;

    //
    // Неверные параметры
    //

    {
        int a[10][10];

        if (input(NULL, 2, 3) != Error_invalid_param)
            err_counter++;
        if (input(a, -3, 3) != Error_invalid_param)
            err_counter++;
        if (input(a, 2, 12) != Error_invalid_param)
            err_counter++;
    }

    //
    // Пустая матрциа
    //

    {
        int a[10][10];

        if (input(a, 0, 3) != Error_no_data)
            err_counter++;
        if (input(a, 2, 0) != Error_no_data)
            err_counter++;
    }

    //
    // Разные корректные случаи
    //

    {
        int a[10][10];
        int b[10][10];
        int c[10][10];

        if (input(a, 2, 3) != OK)
            err_counter++;
        if (input(b, 5, 2) != OK)
            err_counter++;
        if (input(c, 1, 1) != OK)
            err_counter++;
    }

    printf("%s: %s\n", __func__, err_counter ? "FAILED" : "OK");
}

int output(int a[][10], int n, int m)
{
    if (a == NULL || n < 0 || n > 10 || m < 0 || m > 10)
        return Error_invalid_param;
    if (n == 0 || m == 0)
        return Error_no_data;

    printf("\nSource matrix:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            printf("%d ", a[i][j]);

        printf("\n");
    }

    printf("\n");

    return 0;
}

void output_tests(void)
{
    int err_counter = 0;

    //
    // Неверные параметры
    //

    {
        int a[10][10];

        if (output(NULL, 2, 3) != Error_invalid_param)
            err_counter++;
        if (output(a, -3, 3) != Error_invalid_param)
            err_counter++;
        if (output(a, 2, 12) != Error_invalid_param)
            err_counter++;
    }

    //
    // Пустая матрциа
    //

    {
        int a[10][10];

        if (output(a, 0, 3) != Error_no_data)
            err_counter++;
        if (output(a, 2, 0) != Error_no_data)
            err_counter++;
    }

    //
    // Разные корректные случаи
    //

    {
        int a[10][10] = {{2, 3, 4}, {2, 3, 4}};
        int b[10][10] = {{2, 3}, {4, 5}, {6, 7}, {8, 9}, {10, 11}};
        int c[10][10] = {{2}};

        if (output(a, 2, 3) != OK)
            err_counter++;
        if (output(b, 5, 2) != OK)
            err_counter++;
        if (output(c, 1, 1) != OK)
            err_counter++;
    }

    printf("%s: %s\n", __func__, err_counter ? "FAILED" : "OK");
}

int calculate(int a[][10], int n, int m, int mass[])
{
    int numb, cur;

    if (a == NULL || n < 0 || n > 10 || m < 0 || m > 10 || mass == NULL)
        return Error_invalid_param;
    if (n == 0 || m == 0)
        return Error_no_data;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cur = abs(a[i][j]);
            while (cur > 0)
            {
                numb = cur % 10;
                mass[numb] += 1;
                cur /= 10;
            }
        }
    }

    return 0;
}

void calculate_tests(void)
{
    int err_counter = 0;

    //
    // Неверные параметры
    //

    {
        int a[2][10] = {{1, 2, 3}, {4, 5, 6}};
        int mass[10];

        if (calculate(NULL, 2, 3, mass) != Error_invalid_param)
            err_counter++;
        if (calculate(a, 2, 3, NULL) != Error_invalid_param)
            err_counter++;
        if (calculate(a, -2, 3, mass) != Error_invalid_param)
            err_counter++;
        if (calculate(a, 2, 13, mass) != Error_invalid_param)
            err_counter++;
    }

    //
    // Пустая матрица
    //

    {
        int a[2][10] = {{1, 2, 3}, {4, 5, 6}};
        int mass[10];

        if (calculate(a, 0, 3, mass) != Error_no_data )
            err_counter++;
        if (calculate(a, 2, 0, mass) != Error_no_data )
            err_counter++;
    }

    //
    // Разные корректные случаи
    //

    {
        int a[2][10] = {{2, 32}, {-11, 2}};
        int b[3][10] = {{3, 2}, {423, 684}, {2, -111}};
        int c[2][10] = {{3, 109, -76}, {222, -12345, 2}};
        int mass[10] = {0};

        if (calculate(a, 2, 2, mass) != OK)
            err_counter++;
        if (calculate(b, 3, 2, mass) != OK)
            err_counter++;
        if (calculate(c, 2, 3, mass) != OK)
            err_counter++;
    }

    printf("%s: %s\n", __func__, err_counter ? "FAILED" : "OK");
}

int max(int mass[])
{
    if (mass == NULL)
        return Error_invalid_param;
    int max = 0;

    for (int i = 0; i < 10; i++)
    {
        if (mass[i] > mass[max])
            max = i;
    }

    return max;
}

void max_tests(void)
{
    int err_counter = 0;

    //
    // Неверные параметры
    //

    {
        if (max(NULL) != Error_invalid_param)
            err_counter++;
    }

    //
    // Разные корректные случаи
    //

    {
        int mass_1[10] = {0, 10, 2, 3, 4, 5, 6, 7, 8, 9};
        int mass_2[10] = {0, 1, 2, 3, 4, 5, 6, 7, 7, 2};
        int mass_3[10] = {0, 3, 5, 0, 0, 3, 3, 4, 2, 1};

        if (max(mass_1) != 1)
            err_counter++;
        if (max(mass_2) != 7)
            err_counter++;
        if (max(mass_3) != 2)
            err_counter++;
    }

    printf("%s: %s\n", __func__, err_counter ? "FAILED" : "OK");
}

int main()
{
    output_tests();
    input_tests();
    calculate_tests();
    max_tests();

    return 0;
}
