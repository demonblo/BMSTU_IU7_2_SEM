#include <stdio.h>
#define Empty_file      -1
#define Incorrect_input -2
//Тут уже работа с файлами(вау!) тут у нас последовательность символов
//И выводится сколько раз там меняется знак
int sign(int numb)
{
    if (numb < 0)
        return -1;
    else if (numb == 0)
        return 0;
    else
        return 1;
}

int calculate(FILE*f, int*counter)
{
    int numb, prev_sign, counter_of_changes = 0;

    if ((fscanf(f, "%i", &numb)) != 1)
        return Empty_file;

    prev_sign = sign(numb);
    *counter += 1;
    while (fscanf(f, "%i", &numb) == 1)
    {
        if ((numb * prev_sign <= 0) && !(prev_sign >= 0 && numb >= 0))
            counter_of_changes += 1;

        *counter += 1;
        prev_sign = sign(numb);
    }

    return counter_of_changes;
}

int main()
{
    int resource, counter = 0;

    resource = calculate(stdin, &counter);
    if (resource == Empty_file)
    {
        fprintf(stdout, "The sequence is empty!\n");
        return Empty_file;
    }
    if (counter != 1)
    {
        printf("Current sequnce changes its sign %i times\n", resource);
        return 0;
    }
    else
    {
        printf("There is the only one number in sequence!\n");
        return Incorrect_input;
    }
}
