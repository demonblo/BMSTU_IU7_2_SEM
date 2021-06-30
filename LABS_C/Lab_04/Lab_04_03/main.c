#include <stdio.h>
#include <math.h>
//Тут просто все крутиться, вертиться, крутиться, вертиться...
int input(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (scanf("%d", &(a[i])) != 1)
        {
            printf("Incorrect input!\n");
            return -2;
        }
    }

    return 0;
}

int rev(int cur)
{
    int reverse = 0;

    while (cur > 0)
    {
        reverse = reverse * 10 + cur % 10;
        cur /= 10;
    }

    return reverse;
}

void add(int a[], int j, int n)
{
    int temp, temp_next;

    temp = a[j + 1];
    a[j + 1] = rev(a[j]);
    for (int i = j + 1; i < n + 1; i++)
    {
        temp_next = a[i + 1];
        a[i + 1] = temp;
        temp = temp_next;
    }
}

int main()
{
    int a[20], n, k, i = 0, cur_n;

    if (scanf("%d", &n) != 1)
    {
        printf("Incorrect input!\n");
        return -1;
    }
    else if (n < 0)
    {
        printf("Incorrect input!\n");
        return -1;
    }
    else if (n > 10)
    {
        printf("Incorrect input!\n");
        return -1;
    }
    //
    k = input(a, n);
    if (k != 0)
        return -2;
    cur_n = n;
    while (i < cur_n)
    {
        if (a[i] > 0)
        {
            add(a, i, cur_n);
            i += 1;
            cur_n += 1;
        }
        i += 1;
    }

    if (cur_n == n)
    {
        printf("there are no positive elements\n");
        return -3;
    }

    for (int i = 0; i < cur_n; i++)
        printf("%d ", a[i]);

    printf("\n");
    return 0;
}

