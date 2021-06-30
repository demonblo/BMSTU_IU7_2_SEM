#include <stdio.h>
#include <math.h>
#define Max_size              10
#define Error_input_size      -1
#define Error_input_elements  -2
//Дай бог вам понять что тут происходит
int input(int matr [][Max_size], int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("Input [%d][%d] element:", i, j);
            if (scanf("%d", &(matr[i][j])) != 1)
                return -2;
        }
    }

    return 0;
}

void output_matrix(int matr [][Max_size], int n, int m)
{
    printf("Source matrix\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matr[i][j]);
        }
        printf("\n");
    }
}

void output_massive(int mass [], int n)
{
    printf("Calculated massive\n");
    for (int i = 0; i < n; i++)
        printf("%d ", mass[i]);
}

int calculate(int mass[], int m)
{
    int flag_first = 0;
    int flag_second = 0;

    if (m == 1)
        return -1;
    for (int i = 0; i < m - 1; i++)
        if (mass[i] > mass[i + 1])
            flag_first = 1;
    if (flag_first == 1)
    {
        for (int i = 0; i < m - 1; i++)
            if (mass[i] < mass[i + 1])
                flag_second = 1;

        if (flag_second == 1)
            return -1;
        else
            return 0;
    }
    else
        return 0;
}

int main()
{
    char inout;

    scanf("%c", &inout);
    printf("%d", inout);

    return 0;
}
