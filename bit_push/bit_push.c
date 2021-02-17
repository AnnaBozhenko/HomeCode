#include <stdio.h>
#include <stdlib.h>

void print_front_page(){
    system("cls||clear");
    printf("\n┌────────────────────────────────────────────────────────────────────────────────────────────┐");
    printf("\n│                          Laboratory work №1                                                │");
    printf("\n│                                                                                            │");
    printf("\n│ Theme: 'Base type of data, input-output, operations with bits, operations of bit shifting' │");
    printf("\n│                                                                                            │");
    printf("\n│     Done by st. of gr. КМ-01                                        Nimchenko M.           │");
    printf("\n│                                                                                            │");
    printf("\n│                                                                                            │");
    printf("\n│                                  2020                                                      │");
    printf("\n└────────────────────────────────────────────────────────────────────────────────────────────┘");
}

void print_line(){
    printf("\n----------\n");
}

int input_number(char *det){
    // det - string, determine type or bound of input:
    // days - from 0 to 31
    // month - from 0 to 12
    // years - from 1980 to 2043
    // type is dec or hex numbers.
    int number;
    char last;
    if(det == "day")
        while(!scanf("%d%c", &number, &last) || last != '\n' || number < 0 || number > 31){
            rewind(stdin);
            printf("\nWrong value. Try again(from 0 till 31): ");
            fflush(stdin);
        }
    else if(det == "month")
        while(!scanf("%d%c", &number, &last) || last != '\n' || number < 0 || number > 12){
            rewind(stdin);
            printf("\nWrong value. Try again(from 0 till 12): ");
            fflush(stdin);
        }
    else if(det == "year")
        while(!scanf("%d%c", &number, &last) || last != '\n' || number < 1980 || number > 2043){
            rewind(stdin);
            printf("\nWrong value. Try again(from 1980 till 2043): ");
            fflush(stdin);
        }
    else if(det == "hex")
        while(!scanf("%x%c", &number, &last) || last != '\n' || number < 0 || number > 65535){
        // 0xffff(hex) === 65535(dec) is max value of word.
        rewind(stdin);
        printf("\nWrong word. Try again(len of word no more than 4): ");
        fflush(stdin);
    }

    return number;
}

int is_quit(){
    int type;
    char last;
    printf("Exit to menu(input 0),\n"
            "repeat work of programm(input 1): ");
    // Check if input is 1 or 0.
    while((!scanf("%d%c", &type, &last) || last != '\n') || (type != 1 && type != 0)){
        rewind(stdin);
        printf("Wrong value. Try again(input 0 or 1): ");
        fflush(stdin);
    }
    print_line();
    return type;
}

int pack(){
    int day, month, year, word;

    printf("Input day: ");
    day = input_number("day");
    printf("Input month: ");
    month = input_number("month");
    printf("Input year(from 1980 till 2043): ");
    // Substract 1980 to easily operate value from 0 to 63(<2^6).
    year = input_number("year") - 1980;

    // Write five bits in the end of the word(bit realization)
    // dddd dd00 0000 0000
    word = (day & 0x1f) << 11;
    // Write five bits in the middle of the word(bit realization)
    // 0000 0mmm mm00 0000
    word |= (month & 0x1f) << 6;
    // Write six bits in the beginning of the word(bit realization)
    // 0000 0000 0000 yyyy
    word |= year & 0x3f;

    return word;
}

void unpack(int *day_ptr, int *month_ptr, int *year_ptr){
    int word;
    printf("Input word: ");
    word = input_number("hex");

    // Write in *year_ptr first six bits.
    *year_ptr = word & 0x3f;
    // Write in *month_ptr five bits after first six bits.
    *month_ptr = (word >> 6) & 0x1f;
    // Write in *day_ptr five bits after first 11 bits.
    *day_ptr = (word >> 11) & 0x1f;
}

// examples of inputting data
// dddd dmmm mmyy yyyy
// 01 01 1981 -> 0000 1000 0100 0001 -> 841
// 10 05 1985 -> 0101 0001 0100 0101 -> 5145
// 31 12 2043 -> 1111 1011 0011 1111 -> FB3F
// 32 12 2043 -> error: in month 31 days.
// 31 13 2043 -> error: there are only 12 months.
// 31 12 2044 -> error: to record years properly
// it is available only 2043 years as 2043 - 1980 = 63 < 2^6,
// as there available only 6 bits for writing a year into hex.

int main(){
    print_front_page();    
    int choose = -1;
    char last;
    while(choose){
        printf("\nChoose programm:"
                "\n0 - exit from programm,"
                "\n1 - programm of packing,"
                "\n2 - programm of unpacking: ");
        // Сhecking if choose is 0, 1, 2.
        while((!scanf("%d%c", &choose, &last) || last != '\n') || (choose != 0 && choose != 1 && choose != 2)){
            // Fixing and pointing buffer at the beginning.
            rewind(stdin);
            printf("\nWrong value. Try again(введіть 0, 1 або 2): ");
            // Clear buffer.
            fflush(stdin);
        }
        print_line();
        if(choose == 1)
            do{
                printf("\nWord: %04x", pack());
                print_line();
                // User input 0 - exit, 1 - continue working.
            }while(is_quit());
        else if(choose == 2)
            do{
                int day, month, year, r = 0;
                unpack(&day, &month, &year);
                // In case month is more than 12,
                // translate it to years by mod 12.
                if(month > 12){
                    r = month / 12;
                    month = month % 12;
                }
                printf("\nDay: %d,"
                        "\nMonth: %d,"
                        "\nYear: %d", day, month, year + 1980 + r);
                print_line();
            }while(is_quit());
        }
    return 0;
}