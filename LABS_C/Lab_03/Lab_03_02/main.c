# include <stdio.h>
# include <math.h>

# define File_error          -1
# define Empty_file          -2
# define Incorrect_input     -3
//Правило 3 сигм, даже не спрашивайте, я не помню
int count_numbers(FILE *f)
{
    int counter = 0, scan = 0;
    float numb;

    scan = fscanf(f, "%f", &numb);
    while (scan == 1)
    {
        counter++;
        scan = fscanf(f, "%f", &numb);
    }

    if (scan == EOF)
        return counter;
    else
        return Incorrect_input;
}

float medium(FILE *f, int count)
{
    float numb, sum = 0;

    while (fscanf(f, "%f", &numb) != EOF)
        sum += numb;

    return sum / count;
}

float sigma(FILE *f, int count, float medium)
{
    float temp, sum_x_sum = 0;

    while (fscanf(f, "%f", &temp) != EOF)
        sum_x_sum += (temp - medium) * (temp - medium);

    return sqrt(sum_x_sum / count);
}

int three_sigmas_rule(FILE *f, float f_medium, float f_sigma)
{
    float numb;

    while (fscanf(f, "%f", &numb) != EOF)
        if ((numb - f_medium >= 3 * f_sigma) || (f_medium - numb >= 3 * f_sigma))
            return 0;
    return 1;
}

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Incorrect console input!\n");
        return File_error;
    }
    FILE* file = fopen(argv[1], "rt");
    int counter;
    float f_medium, f_sigma;

    if (!file)
    {
        printf("Incorrect file!\n");
        return File_error;
    }
    counter = count_numbers(file);
    if (counter > 0)
        rewind(file);
    else if (!counter)
    {
        printf("File is empty!\n");
        fclose(file);
        return Empty_file;
    }
    else
    {
        printf("Incorrect input data!");
        fclose(file);
        return Incorrect_input;
    }
    f_medium = medium(file, counter);
    rewind(file);
    f_sigma = sigma(file, counter, f_medium);
    rewind(file);
    if (three_sigmas_rule(file, f_medium, f_sigma))
        printf("The rule of three sigmas has worked!\n");
    else
        printf("The rule of three sigmas hasn't worked!\n");
    fclose(file);
    return 0;
}
