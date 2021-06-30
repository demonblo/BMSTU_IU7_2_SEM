#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Реализация strchr
char *strchr_by_me(const char *s, int c)
{
    while(*s != (char)c)
    {
        s++;

        if (*s == '\0')
            return NULL;
    }

    return (char *)s;
}

int main()
{
    char *first_test = "abevgdei";
    char *my_first_strchar = strchr_by_me(first_test, 'e');
    char *standart_first_strchar = strchr(first_test, 'e');
    char *second_test = "Work hard die hard";
    char *my_second_strchar = strchr_by_me(second_test, ' ');
    char *standart_second_strchar = strchr(second_test, ' ');

    printf("\nThe first test: %s\n", first_test);
    printf("Expected answer - %s\nMy answer - %s\n", my_first_strchar, standart_first_strchar);
    printf("\nSecond test:%s\n", second_test);
    printf("Expected answer -%s\nMy answer -%s\n", my_second_strchar, standart_second_strchar);
    return 0;
}
