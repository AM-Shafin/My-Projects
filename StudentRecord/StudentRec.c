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
        printf("\t\t\t\t=====Add Students Info======\n\n\n");
        fp=fopen("information.txt","a");
        printf("\n\t\t\tEnter First Name    : ");
        scanf("%s", &info.first_name);
        printf("\n\t\t\tEnter Last Name     : ");
        scanf("%s", &info.last_name);
        printf("\n\t\t\tEnter Enter Roll-No : ");
        scanf("%s", &info.roll_no);
        printf("\n\t\t\tEnter Class(course) : ");
        scanf("%s", &info.Class);
        printf("\n\t\t\tEnter Address       : ");
        scanf("%s", &info.vill);
        printf("\n\t\t\tEnter Percentage    : ");
        scanf("%s", &info.per);
        printf("\n\t\t\t______________________________\n");

        if(fp==NULL){
            fprintf(stderr,"can't open file");
        }else{
            printf("\t\t\tRecord stored sucessfully\n");
        }

        fwrite(&info, sizeof(struct student), 1, fp);
        fclose(fp);

        printf("\t\t\tYou want to add another record?(y/n) : ");
        scanf("%s",&another);
    }while(another=='y'||another=='Y');
}


void studentrecord(){
    FILE *fp;
    struct student info;
    fp=fopen("information.txt","r");
    printf("\t\t\t======STUDENTS RECORD======\n\n\n");
    if(fp==NULL){
        fprintf(stderr,"can't open file\n");
        exit(0);
    }else{
        printf("\t\t\t\tRECORDS :");
        printf("\t\t\t\t_____________");
    }

    while(ferad(&info,sizeof(struct student),1,fp))
    {
        printf("\n\t\t\t\t Student Name : %s %s",info.first_name,info.last_name);
        printf("\n\t\t\t\tRoll NO       : %d",info.roll_no);
        printf("\n\t\t\t\tClass         : %s",info.Class);
        printf("\n\t\t\t\tVillage/City  : %s",info.vill);
        printf("\n\t\t\t\tPercentage    : %f%",info.per);
        printf("\n\t\t\t\t________________________________\n");
    }
    fclose(fp);
    getch();
}

void searchstudent(){
    struct student info;
    FILE *fp;
    int roll_no, found=0;

    fp=fopen("information.txt","r");
    printf("\t\t\t\t======SEARCH STUDENTS RECORD======\n\n\n");
    printf("\t\t\tEnter the roll no : ");
    scanf("%d",&roll_no);
    while (fread(&info.sizeof(struct student),1,fp)>0){
        if(info.roll_no==roll_no){
            found=1;
            printf("\n\n\t\t\tStudent Name : %s %s",info.first_name,info.last_name);
            printf("\n\t\t\tRoll NO        : %d",info.roll_no);
            printf("\n\t\t\tClass          : %s",info.Class);
            printf("\n\t\t\tAddress        : %s",info.vill);
            printf("\n\t\t\tPercentage     : %f%",info.per);
            printf("\n\t\t\t______________________________________\n");
        }
    }
    if(!found){
        printf("\n\t\t\tRecord not found\n");
    }
    fclose(fp);
    getch();
}

void delete(){
    struct student info;
    FILE *fp, *fp1;
}