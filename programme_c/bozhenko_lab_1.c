#include<stdio.h>
#include <ctype.h>
#include <stdlib.h>

int valid_number(char input_str[]);
void task_1();
void task_2();

void task_1()
{
  char execute[2] = "1", base[100], height[100];
  char *ptr_base, *ptr_height;

  while (execute[0] == '1' && execute[1] == '\0')
  {
    printf("\nВведіть значення основи трикутника (дійсне число): ");
    scanf("%s", base);
    printf("\nВведіть значення висоти, проведеної до основи (дійсне число): ");
    scanf("%s", height);
    if (valid_number(base) == 0 || valid_number(height) == 0)
    {
     printf("\nХибний формат даних. Бажаєте продовжити - введіть 1,\nякщо бажаєте завершити - введіть будь-що: ");
    scanf("%s",  execute);
    }
    else 
    {
      printf("\nПлоща трикутника з основою %s та висотою %s: %f", base, height, strtof(base, &ptr_base) * strtof(height, &ptr_height) * 0.5);
      printf("\n\nБажаєте продовжити - введіть 1,\nякщо бажаєте завершити - введіть будь-що: ");
      scanf("%s",  execute);
    }
  }
}


void task_2()
{
  char a[100], b[100], c[100], execute[2] = "1";
  char *ptr_a, *ptr_b, *ptr_c;
  while (execute[0] == '1' && execute[1] == '\0')
    {
      printf("\nВведіть значення ребра а:  (дійсне число): ");
      scanf("%s", a);
      printf("\nВведіть значення ребра b: (дійсне число): ");
      scanf("%s", b);
      printf("\nВведіть значення ребра c: (дійсне число): ");
      scanf("%s", c);
      if (valid_number(a) == 0 || valid_number(b) == 0 || valid_number(c) == 0)
      {
       printf("\nХибний формат даних. Бажаєте продовжити - введіть 1,\nякщо бажаєте завершити - введіть будь-що: ");
      scanf("%s",  execute);
      }
      else 
      {
        printf("\nОб'єм паралелепіпеда з ребрами a: %s, b: %s, c: %s: %f", a, b, c, strtof(a, &ptr_a) * strtof(b, &ptr_b) * strtof(c, &ptr_c));
        printf("\n\nБажаєте продовжити - введіть 1,\nякщо бажаєте завершити -   введіть будь-що: ");
        scanf("%s",  execute);
      }
    }

}


int valid_number(char input_str[])
{
  int i = 0;
  while (input_str[i] != '\0')
  {
    if ((isdigit(input_str[i])) || (input_str[i] == '.'))
    { 
      i++;
    }
    else
    {
      return 0;
    }
  }
  return 1;
}


int main()
{
    // system("chcp 65001");
    // system("cls");
    
    char run_program[2] = "1", choice[2];

    while (run_program[0] == '1' && run_program[1] == '\0')
    {
      printf("\n Ця програма розв'язує 2 задачі. Щоб вибрати введіть відповідне число, що нумерує задачу.\nНариклад, якщо Ви бажаєте запустити першу задачу Ви вводите 1: \n\n 1. Обчислити площу трикутника за основою та висотою.\n 2. Обчислити об’єм прямокутного паралелепіпеда за трьома сторонами.\n\n");
      printf("Ваш вибір: ");
      scanf("%s", choice);
      if (choice[0] == '1' && choice[1] == '\0')
      {   
        printf("\nВи вибрали першу програму.");
        task_1();
      }
      else if (choice[0] == '2' && choice[1] == '\0')
      {
        printf("\nВи вибрали другу програму.");
        break;
        //task_2();
      }
      else
      {
          printf("\n\nХибний формат даних. Бажаєте продовжити - введіть 1, \nякщо бажаєте завершити - введіть будь-що: ");
          scanf("%s",  run_program);
      }
    }
    printf("\nSuccesfully executed!!!");
    return 0;
}


