#include<stdio.h>
#include<string.h>

#define Legth_string        256
#define Quantity_of_words    16
#define Word_length          17
#define Empty_error          -1
#define Length_error         -2
#define Words_error          -3
#define String_length_error  -4
//Ну тут в зависимости от условии лабы, там что-то связанное со словами
//Удачи)
int unique_words(char matrix_of_words[Quantity_of_words][32], int initial_count)
{
    int i, j;

    for (i = 0; i < initial_count; i++)
    {
        for (j = i + 1; j < initial_count; j++)
            if (strcmp(matrix_of_words[j], matrix_of_words[i]) == 0)
            {
                strcpy(matrix_of_words[j], matrix_of_words[initial_count - 1]);
                initial_count--;
                j--;
            }
    }

    return initial_count;
}

int split_on_words(char matrix_of_words[Quantity_of_words][32], int initial_count)
{
    char c = getchar();
    char word[32];
    int length_of_word = 0, count_symbol = 0;

    if ((c == '\n') || (c == '\0'))
        return Empty_error;
    while ((c == ' ') || (c == ',') || (c == ';') || (c == ':') ||
        (c == '-') || (c == '.') || (c == '!') || (c == '?'))
    {
        count_symbol++;
        c = getchar();
    }

    while ((c != '\n') && (c != '\0') && (c != EOF))
    {
        if ((c == ' ') || (c == ',') || (c == ';') || (c == ':') ||
            (c == '-') || (c == '.') || (c == '!') || (c == '?'))
        {
            if (length_of_word != 0)
            {
                if ((initial_count + 1) > Quantity_of_words)
                    return Words_error;
                word[length_of_word] = '\0';
                strcpy(matrix_of_words[initial_count], word);
                initial_count++;
                length_of_word = 0;
            }
        }
        else
        {
            // Checking space for '/0'
            if (length_of_word == Word_length - 1)
                return Length_error;
            word[length_of_word] = c;
            length_of_word++;
        }
        count_symbol++;
        c = getchar();
    }

    if (length_of_word != 0)
    {
        if ((initial_count + 1) > Quantity_of_words)
            return Words_error;
        if (length_of_word > Word_length - 1)
            return Length_error;
        word[length_of_word] = '\0';
        strcpy(matrix_of_words[initial_count], word);
        initial_count++;
        length_of_word = 0;
    }
    if (count_symbol > Legth_string)
        return String_length_error;
    return initial_count;
}

void sort_words(char matrix_of_words[Quantity_of_words][32], int initial_cnt)
{
    int pos_to_swap;
    char tmp[32];

    for (int i = 0; i < initial_cnt; i++)
    {
        pos_to_swap = i;
        for (int j = i; j < initial_cnt; j++)
            if (strcmp(matrix_of_words[j], matrix_of_words[pos_to_swap]) < 0)
                pos_to_swap = j;

        strcpy(tmp, matrix_of_words[pos_to_swap]);
        strcpy(matrix_of_words[pos_to_swap], matrix_of_words[i]);
        strcpy(matrix_of_words[i], tmp);
    }
}

typedef char matr_words_t[Quantity_of_words][32];

int main()
{
    matr_words_t matrix_of_words;
    int initial_count = 0;

    initial_count = split_on_words(matrix_of_words, initial_count);
    if (initial_count <= 0)
    {
        if (initial_count == Length_error)
        {
            printf("Incorrect length!\n");
            return Length_error;
        }
        if (initial_count == Words_error)
        {
            printf("Incorrect words!\n");
            return Words_error;
        }
        if (initial_count == String_length_error)
        {
            printf("Incorrect length of string!\n");
            return String_length_error;
        }
        if ((initial_count == Empty_error) || (!initial_count))
        {
            printf("Error!\n");
            return Empty_error;
        }
    }
    initial_count = unique_words(matrix_of_words, initial_count);
    sort_words(matrix_of_words, initial_count);
    printf("Result:");
    for (int i = 0; i < initial_count; i++)
        printf("%s ", matrix_of_words[i]);

    return 0;
}
