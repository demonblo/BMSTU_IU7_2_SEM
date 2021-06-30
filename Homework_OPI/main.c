/**
  @author Блохин Дмитрий ИУ 7 - 22 Б
  @version 1.0.0
  */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#define Error_incorrect_input      -1
#define Error_incorrect_element    -2
/**
 * @brief Пользователь вводит по одному элементу матрицы.
 * @param a - матрица
 * @param n - количество строк
 * @param m - количество столбцов
 * @return 0 or -2 (0 - функция была выполнена корректно, а -2 - нет)
 */
int input(int a[][10], int n, int m)
{
    assert(n > 0);
    assert(n <= 10);
    assert(m > 0);
    assert(m <= 10);
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
/**
 * @brief Программа выводит исходную матрицу.
 * @param a - матрциа
 * @param n - количество строк
 * @param m - количество столбцов
 */
void output(int a[][10], int n, int m)
{
    assert(n > 0);
    assert(n <= 10);
    assert(m > 0);
    assert(m <= 10);
    printf("\nSource matrix:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            printf("%d ", a[i][j]);

        printf("\n");
    }

    printf("\n");
}
/**
 * @brief Данная функция берет по одному числу из матрицы и увеличивает количество встреч в массиве частотнике всех цифр в этом числе.
 * @param a - матрица
 * @param n - количество строк
 * @param m - количество столбцов
 * @param mass - массив частотник
 */
void calculate(int a[][10], int n, int m, int mass[])
{
    assert(n > 0);
    assert(n <= 10);
    assert(m > 0);
    assert(m <= 10);
    int numb, cur;

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

}
/**
 * @brief Данная функция определяет максимальный элемент массива.
 * @param mass - массив
 * @return max - максимальный элемент матрицы
 */
int max(int mass [])
{
    int max = 0;

    for (int i = 0; i < 10; i++)
    {
        if (mass[i] > mass[max])
            max = i;
    }

    return max;
}
/**
 * @brief main программы.\n Здесь вводится размерность матрицы и выводится ответ.
 * @return
 */
int main()
{
    int a[10][10], mass[10] = {0}, n, m, k;

    printf("Input count of lines:");
    if (scanf("%d", &n) != 1)
    {
        printf("Incorrect input of size!\n");
        return Error_incorrect_input;
    }
    printf("Input count of columns:");
    if (scanf("%d", &m) != 1)
    {
        printf("\nIncorrect input of size!\n");
        return Error_incorrect_input;
    }
    printf("\n");
    k = input(a, n, m);
    if (k != 0)
    {
        printf("Incorrect input of elemets!\n");
        return Error_incorrect_element;
    }
    output(a, n, m);
    calculate(a, n, m, mass);
    printf("The most recent number is %d\n", max(mass));
    return 0;
}
