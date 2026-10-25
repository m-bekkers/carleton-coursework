// SYSC 2006 - Lab 2 Template

#include "lab2.h"
#include <stdbool.h> // Include the necessary header for _Bool
#include <stdio.h>
#include <stdlib.h>

/* Replace these lines with your information */
const char *author_main = "Matthé Bekkers";
const char *student_number_main = "101297066";

int main(void) {
  // Tests exercise 1 - Complete for a comprehensive test harness
  int expected_week_non_vac = 7;
  int expected_week_vac = 10;
  int expected_weekend_non_vac = 10;
  int expected_weekend_vac = -1;

  for (int day = 1; day <= 5; day++) { // loop for weekdays non-vac
    int alarm_time = alarm_clock(day, false);
    if (alarm_time == expected_week_non_vac) {
      printf("Day %d, Non vacation: TEST PASS.\n", day);
    } else {
      printf("Day %d, Non vacation: TEST FAIL.\n", day);
    }
  }
  for (int day = 1; day <= 5; day++) {
    int alarm_time = alarm_clock(day, true);
    if (alarm_time == expected_week_vac) {
      printf("Day %d, Vacation: TEST PASS.\n", day);
    } else {
      printf("Day %d, Vacation: TEST FAIL.\n", day);
    }
  }

  int sun_nVac = alarm_clock(6, false);
  int sat_nVac = alarm_clock(6, false);
  int sun_vac = alarm_clock(6, true);
  int sat_vac = alarm_clock(6, true);

  if (sun_nVac != expected_weekend_non_vac) {
    printf("Day 0, Non Vacation: TEST FAIL.\n");
  } else {
    printf("Day 0, Non Vacation: TEST PASS.\n");
  }
  if (sat_nVac != expected_weekend_non_vac) {
    printf("Day 6, Non Vacation: TEST FAIL.\n");
  } else {
    printf("Day 6, Non Vacation: TEST PASS.\n");
  }

  if (sun_vac == expected_weekend_vac) {
    printf("Day 0, Vacation: TEST PASS.\n");
  } else {
    printf("Day 0, Vacation: TEST FAIL.\n");
  }
  if (sat_vac == expected_weekend_vac) {
    printf("Day 6, Vacation: TEST PASS.\n");
  } else {
    printf("Day 6, Vacation: TEST FAIL.\n");
  }

  // Type your test cases for exercise 2. Make sure to include border line cases
  int e2_test1 = 10;
  int e2_test2 = 15;
  int e2_test3 = 0;
  int e2_test4 = 3;

  printf("Expected output for Test 1: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz\n"
         "Actual output: ");
  count_replace(e2_test1);
  printf("\n");
  printf("Expected output for Test 2: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 "
         "Fizz 13 14 FizzBuzz\nActual output: ");
  count_replace(e2_test2);
  printf("\n");
  printf("Expected output for Test 3:\nActual output: ");
  count_replace(e2_test3);
  printf("\n");
  printf("Expected output for Test 4: 1 2 Fizz\nActual output: ");
  count_replace(e2_test4);
  printf("\n");

  // Type your test cases for exercise 3. Make sure to include border line cases
  int e3_test1 = 1;
  int e3_test2 = 4;
  int e3_test3 = 31;
  int e3_test4 = 123456;

  if (is_prime(e3_test1) == false) {
    printf("Is Prime Test 1 PASS.\n");
  } else {
    printf("Is Prime Test 1 FAIL.\n");
  }

  if (is_prime(e3_test2) == false) {
    printf("Is Prime Test 2 PASS.\n");
  } else {
    printf("Is Prime Test 2 FAIL.\n");
  }

  if (is_prime(e3_test3) == true) {
    printf("Is Prime Test 3 PASS.\n");
  } else {
    printf("Is Prime Test 3 FAIL.\n");
  }

  if (is_prime(e3_test4) == false) {
    printf("Is Prime Test 4 PASS.\n");
  } else {
    printf("Is Prime Test 4 FAIL.\n");
  }
  // Type your test cases for exercise 4. Make sure to include border line cases
  int e4_test1 = 4;
  int e4_test2 = 10;
  int e4_test3 = 20;
  int e4_test4 = 0;

  if (sum_even(e4_test1) == 6) {
    printf("Sum Even Test 1 PASS.\n");
  } else {
    printf("Sum Even Test 1 FAIL.\n");
  }

  if (sum_even(e4_test2) == 30) {
    printf("Sum Even Test 2 PASS.\n");
  } else {
    printf("Sum Even Test 2 FAIL.\n");
  }

  if (sum_even(e4_test3) == 110) {
    printf("Sum Even Test 3 PASS.\n");
  } else {
    printf("Sum Even Test 3 FAIL.\n");
  }

  if (sum_even(e4_test4) == 0) {
    printf("Sum Even Test 4 PASS.\n");
  } else {
    printf("Sum Even Test 4 FAIL.\n");
  }

  printf("Test harness finished\n");
  return EXIT_SUCCESS;
}

int alarm_clock(int day, _Bool vacation) {
  if (vacation) {
    if (day > 0 && day < 6) {
      return (10);
    } else {
      return (-1);
    }
  } else {
    if (day > 0 && day < 6) {
      return (7);
    } else {
      return (10);
    }
  }
}

void count_replace(int num) {
  for (int i = 1; i <= num; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      printf("FizzBuzz");
    } else if (i % 5 == 0) {
      printf("Buzz");
    } else if (i % 3 == 0) {
      printf("Fizz");
    } else {
      printf("%d", i);
    }
    if (i < num) {
      printf(" ");
    } else {
      printf("\n");
    }
  }
}

bool is_prime(int prime_check) {
  if (prime_check < 2) {
    return false;
  }
  for (int i = 2; i < prime_check; i++) {

    if (prime_check % i == 0) {
      return false;
    }
  }

  return true;
}

int sum_even(int even_base) {
  int sum = 0;
  for (int i = 1; i <= even_base; i++) {
    if (i % 2 == 0) {
      sum += i;
    }
  }
  return sum;
}