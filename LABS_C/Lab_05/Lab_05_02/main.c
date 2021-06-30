#include <stdio.h>

#define Error_input_size      -1
#define Error_input_elements  -2
#define Error_matrix_input    -3
#define Empty_matrix          -4
#define Error_digit_input     -5
#define Max_size 10
//Тут вроде как удаляются столбцы которые содержат вводимое значение
int input(int matr [][Max_size], int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("Input [%d][%d] element:", i, j);
            if (scanf("%d", &(matr[i][j])) != 1)
                return Error_matrix_input;
        }
    }

    return 0;
}

void output_matrix(int matr[][Max_size], int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            printf("%d ", matr[i][j]);

        printf("\n");
    }
}

int has_digit(int number, int digit)
{
    number = number > 0 ? number : -number;
    if (number == digit && digit == 0)
        return 1;

    while (number != 0)
    {
        if (number % 10 == digit)
            return 1;
        number /= 10;
    }

    return 0;
}

int delete_columns(int matr[][Max_size], int n, int m, int digit)
{
    int temp_mas[Max_size] = {0};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            if (has_digit(matr[i][j], digit))
                temp_mas[j] = 1;
        }

    for (int i = m - 1; i >= 0; i--)
        if (temp_mas[i])
        {
            for (int k = 0; k < n; k++)
                for (int j = i; j <= m - 1; j++)
                    matr[k][j] = matr[k][j + 1];

            for (int j = i; j < m - 1; j++)
                temp_mas[j] = temp_mas[j + 1];
            m--;
        }

    return m;
}

int main()
{
    int k, n, m, digit;
    int matr[Max_size][Max_size];

    printf("Input size of matrix:");
    if (scanf("%d%d", &n, &m) != 2)
    {
        printf("Incorrect input of size!\n");
        return Error_input_size;
    }
    if ((n <= 0 || n > 10) || (m <= 0 || m > 10))
    {
        printf("Incorrect input of size!\n");
        return Error_input_elements;
    }
    k = input(matr, n, m);
    if (k != 0)
    {
        printf("Incorrect input of elements!\n");
        return k;
    }
    printf("Enter the digit: ");
    if (scanf("%d", &digit) != 1)
    {
        printf("Incorrect input of digit! ");
        return Error_digit_input;
    }
    if (digit < 0 || digit > 9)
    {
        printf("Incorrect input of digit! ");
        return Error_digit_input;
    }
    printf("Source matrix\n");
    output_matrix(matr, n, m);
    m = delete_columns(matr, n, m, digit);
    if (m == 0)
    {
        printf("Matrix is empty! ");
        return Empty_matrix;
    }
    printf("Calculated matrix\n");
    output_matrix(matr, n, m);

    return 0;
}
