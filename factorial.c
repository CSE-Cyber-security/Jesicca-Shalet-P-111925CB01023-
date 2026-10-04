/*
 * Week 02 Mini Project - Factorial Calculator (C)
 * Features : iterative & recursive factorial, factorial table,
 *            history (file based), summary, input validation
 * Compile  : gcc src/factorial.c -o factorial
 * Run      : ./factorial   (run from the project root folder)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <limits.h>

#define MAX_N 20                       /* 20! is the largest that fits in unsigned long long */
#define HISTORY_FILE "data/factorial_history.txt"

typedef unsigned long long ull;

/* ---------- Core logic ---------- */
ull factorial_iterative(int n) {
    ull result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}

ull factorial_recursive(int n) {
    if (n <= 1)
        return 1;
    return (ull)n * factorial_recursive(n - 1);
}

/* ---------- Input helpers ---------- */
/* Returns 1 = valid integer, 0 = invalid, -1 = EOF */
int read_int(const char *prompt, int *out) {
    char buf[64], *end;
    printf("%s", prompt);
    if (!fgets(buf, sizeof buf, stdin))
        return -1;
    buf[strcspn(buf, "\r\n")] = '\0';
    if (buf[0] == '\0')
        return 0;
    errno = 0;
    long v = strtol(buf, &end, 10);
    if (errno != 0 || end == buf || *end != '\0' || v < INT_MIN || v > INT_MAX)
        return 0;
    *out = (int)v;
    return 1;
}

/* Reads n and validates range 0..MAX_N. Returns 1 if valid. */
int read_n(int *n) {
    int status = read_int("Enter a number (0-20): ", n);
    if (status == -1) exit(0);
    if (status == 0) {
        printf("[ERROR] Invalid input. Please enter a whole number.\n");
        return 0;
    }
    if (*n < 0) {
        printf("[ERROR] Factorial is not defined for negative numbers.\n");
        return 0;
    }
    if (*n > MAX_N) {
        printf("[ERROR] %d is too large. Maximum supported value is %d (overflow).\n", *n, MAX_N);
        return 0;
    }
    return 1;
}

/* ---------- History (file handling) ---------- */
void save_history(int n, const char *method, ull result) {
    FILE *fp = fopen(HISTORY_FILE, "a");
    if (!fp) {
        printf("[WARNING] Could not save history. Run the program from the project root.\n");
        return;
    }
    fprintf(fp, "%d %s %llu\n", n, method, result);
    fclose(fp);
}

void display_history(void) {
    FILE *fp = fopen(HISTORY_FILE, "r");
    int n, count = 0;
    char method[20];
    ull result;

    printf("\n=========================================\n");
    printf("        FACTORIAL CALCULATION HISTORY\n");
    printf("=========================================\n");
    if (!fp) {
        printf("No history file found.\n");
    } else {
        while (fscanf(fp, "%d %19s %llu", &n, method, &result) == 3) {
            printf("%2d! = %-20llu (%s)\n", n, result, method);
            count++;
        }
        fclose(fp);
        if (count == 0)
            printf("History is empty.\n");
    }
    printf("=========================================\n");
}

void clear_history(void) {
    FILE *fp = fopen(HISTORY_FILE, "w");
    if (!fp) {
        printf("[ERROR] Could not clear history.\n");
        return;
    }
    fclose(fp);
    printf("History cleared successfully.\n");
}

void show_summary(void) {
    FILE *fp = fopen(HISTORY_FILE, "r");
    int n, total = 0, iter = 0, rec = 0, largest = -1;
    char method[20];
    ull result;

    if (fp) {
        while (fscanf(fp, "%d %19s %llu", &n, method, &result) == 3) {
            total++;
            if (strcmp(method, "Iterative") == 0) iter++; else rec++;
            if (n > largest) largest = n;
        }
        fclose(fp);
    }
    printf("\n=========================================\n");
    printf("              SUMMARY\n");
    printf("=========================================\n");
    printf("Total Calculations     : %d\n", total);
    printf("Iterative Calculations : %d\n", iter);
    printf("Recursive Calculations : %d\n", rec);
    if (largest >= 0)
        printf("Largest Number Used    : %d\n", largest);
    else
        printf("Largest Number Used    : N/A\n");
    printf("=========================================\n");
}

/* ---------- Menu actions ---------- */
void calculate(int use_recursive) {
    int n;
    if (!read_n(&n)) return;
    ull result = use_recursive ? factorial_recursive(n) : factorial_iterative(n);
    const char *method = use_recursive ? "Recursive" : "Iterative";
    printf("\n%d! = %llu   (%s method)\n", n, result, method);
    save_history(n, method, result);
}

void factorial_table(void) {
    int n;
    if (!read_n(&n)) return;
    printf("\n-----------------------------------------\n");
    printf("%-5s | %s\n", "N", "N!");
    printf("-----------------------------------------\n");
    for (int i = 0; i <= n; i++)
        printf("%-5d | %llu\n", i, factorial_iterative(i));
    printf("-----------------------------------------\n");
}

void print_menu(void) {
    printf("\n=========================================\n");
    printf("          FACTORIAL CALCULATOR\n");
    printf("=========================================\n");
    printf("1. Calculate Factorial (Iterative)\n");
    printf("2. Calculate Factorial (Recursive)\n");
    printf("3. Display Factorial Table (0 to N)\n");
    printf("4. Display History\n");
    printf("5. Show Summary\n");
    printf("6. Clear History\n");
    printf("7. Exit\n");
    printf("=========================================\n");
}

int main(void) {
    int choice, status;
    while (1) {
        print_menu();
        status = read_int("Enter your choice: ", &choice);
        if (status == -1) break;
        if (status == 0) {
            printf("[ERROR] Invalid choice. Enter a number from 1 to 7.\n");
            continue;
        }
        switch (choice) {
            case 1: calculate(0);      break;
            case 2: calculate(1);      break;
            case 3: factorial_table(); break;
            case 4: display_history(); break;
            case 5: show_summary();    break;
            case 6: clear_history();   break;
            case 7: printf("Exiting... Goodbye!\n"); return 0;
            default: printf("[ERROR] Invalid choice. Enter a number from 1 to 7.\n");
        }
    }
    return 0;
}
