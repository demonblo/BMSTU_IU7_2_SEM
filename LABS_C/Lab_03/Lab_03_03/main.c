#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//Это похоже даже не я делал
#define Error_of_seek        -1
#define Error_of_read        -2
#define Error_of_write       -3
#define Error_console        -4
#define Error_mode           -5
#define Scan_error           -6
#define Empty_file           -7
#define File_size            10

int get_number_by_pos(int *prt, FILE *file, long int position)
{
    int scan;

    scan = fseek(file, sizeof(int) * position, SEEK_SET);
    if (scan)
        return Error_of_seek;
    scan = fread(prt, sizeof(int), 1, file);
    if (scan)
        return 0;
    else
        return Error_of_read;
}

int put_number_by_pos(int *prt, FILE *file, long int position)
{
    int scan;

    scan = fseek(file, sizeof(int) * position, SEEK_SET);
    if (scan)
        return Error_of_seek;
    scan = fwrite(prt, sizeof(int), 1, file);
    if (scan)
        return 0;
    else
        return Error_of_write;
}

int swap(FILE *file, long int i, long int j)
{
    int temporary_i;
    int temporary_j;
    get_number_by_pos(&temporary_i, file, i);
    get_number_by_pos(&temporary_j, file, j);
    put_number_by_pos(&temporary_i, file, j);
    put_number_by_pos(&temporary_j, file, i);
    return 0;
}

int creation_of_file(char *name_of_file)
{
    FILE* file = fopen(name_of_file, "wb");
    int n, temporary;

    setbuf(stdout, NULL);
    if (!file)
        return Scan_error;
    n = 1 + rand() % (File_size - 1);
    for (long int position = 0; position < n; position++)
    {
        temporary = -1000 + rand() % 2000;
        printf("%d ", temporary);
        put_number_by_pos(&temporary, file, position);
    }

    fclose(file);
    return 0;
}

int print_of_file(char *name_of_file)
{
    FILE* file = fopen(name_of_file, "rb");
    long int pos = 0;
    int temporary, scan;

    setbuf(stdout, NULL);
    if (!file)
        return Scan_error;

    scan = get_number_by_pos(&temporary, file, pos);
    if (scan)
    {
        fclose(file);
        return Empty_file;
    }
    while (!scan)
    {
        printf("%d ", temporary);
        pos++;
        scan = get_number_by_pos(&temporary, file, pos);
    }

    fclose(file);
    return 0;
}

int sort_of_file(char *name_of_file)
{
    FILE* file = fopen(name_of_file, "rb+wb");
    long int n = 0, i, j, min_position;
    int temporary, iteration, min;

    setbuf(stdout, NULL);
    if (!file)
        return Scan_error;
    while (!get_number_by_pos(&temporary, file, n))
        n++;

    if (!n)
    {
        fclose(file);
        return Empty_file;
    }
    for (i = 0; i < n - 1; i++)
    {
        get_number_by_pos(&min, file, i);
        min_position = i;
        for (j = i + 1; j < n; j++)
        {
            get_number_by_pos(&iteration, file, j);
            if (iteration < min)
            {
                min = iteration;
                min_position = j;
            }
        }
        if (min_position != i)
            swap(file, i, min_position);
    }

    fclose(file);
    return 0;
}

int main(int argc, char **argv)
{
    srand(time(NULL));
    int answer = Error_mode;
    if (argc == 3)
    {
        if (!strcmp(argv[1], "c"))
            answer = creation_of_file(argv[2]);
        if (!strcmp(argv[1], "p"))
            answer = print_of_file(argv[2]);
        if (!strcmp(argv[1], "s"))
            answer = sort_of_file(argv[2]);
    }
    else
        answer = Error_console;

    switch (answer)
    {
        case Empty_file:
            printf("Current file is empty!\n");
            break;
        case Error_console:
            printf("Incorrect arguments format in colsole!\n");
            break;
        case Scan_error:
            printf("File scan failed!\n");
            break;
        case Error_mode:
            printf("Wrong mode!\n");
            break;
    }

    return answer;
}
