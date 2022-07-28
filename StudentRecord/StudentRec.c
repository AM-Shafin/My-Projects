#include<stdio.h>
#include<conio.h>

void addstudent();
void studentrecord();
void searchstudent();
void delete();

struct student{
    char first_name[20];
    char last_name[20];
    int roll_no;
    char Class[10];
    char vill[20];
    float per;
};

void main(){
    int choice;
    while (choice!=5)
    {
        printf("\t\t\t=====STUDENT DATABASE MANAGEMENT SYSTEM=====");
        printf("\n\n\n\t\t\t\t  1. Add Student Record\n");
        printf("\t\t\t\t    2. All Student Records\n");
        printf("\t\t\t\t    3. Search Student\n");
        printf("\t\t\t\t    4. Delete Record\n");
        printf("\t\t\t\t    5. Exit\n");
        printf("\t\t\t\t    __________________________\n");
        printf("\t\t\t\t    ");
        scanf("%d",&choice);

        switch (choice)
        {
        case 1:
            clrscr();
            addstudent();
            clrscr();
            break;
        }
    }
}


void addstudent(){
    char another;
    FILE *fp;
    struct student info;

    do{
        clrscr();
    }while(1);
}