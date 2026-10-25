/* SYSC 2006 - Lab 13 - demonstrate ADT dictionary/map.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

int main(void)
{
    printf("Creating a dictionary of names & email addresses\n");
    dict_t *addresses = make_dictionary();

    printf("Adding key: %s, value: %s\n", "Lynn", "lynn.marshall@carleton.ca");
    put(addresses, "Lynn", "lynn.marshall@carleton.ca");

    // Multiple keys can be associated with the duplicate values
    printf("Adding key: %s, value: %s\n", "Don", "donald.bailey@carleton.ca");
    put(addresses, "Don", "donald.bailey@carleton.ca");
    printf("Adding key: %s, value: %s\n", "Donald", "donald.bailey@carleton.ca");
    put(addresses, "Donald", "donald.bailey@carleton.ca");

    printf("Adding key: %s, value: %s\n", "Babak", "babak.esfandiari@carleton.ca");
    put(addresses, "Babak", "babak.esfandiari@carleton.ca");
    printf("Adding key: %s, value: %s\n", "Greg", "gregory.franks@carleton.ca");
    put(addresses, "Greg", "gregory.franks@carleton.ca");
    printf("Adding key: %s, value: %s\n", "Jason", "jason.jaskolka@carleton.ca");
    put(addresses, "Jason", "jason.jaskolka@carleton.ca");

    printf("Email for Babak is %s\n", get(addresses, "Babak"));
    printf("Email for Lynn is %s\n", get(addresses, "Lynn"));
    printf("Email for Jason is %s\n", get(addresses, "Jason"));
    printf("Email for Don is %s\n", get(addresses, "Don"));
    printf("Email for Donald is %s\n", get(addresses, "Donald"));
    printf("Email for Greg is %s\n", get(addresses, "Greg"));

    printf("Changing %s to %s\n", "Babak", "babak@sce.carleton.ca");
    put(addresses, "Babak", "babak@sce.carleton.ca");
    printf("Email for Babak is now %s\n", get(addresses, "Babak"));

    // Test case for print_dictionary
    print_dictionary(addresses);

    // Test cases for replace

    // Tests a valid replacement
    printf("Changing value at key 'Greg' to 'some_value'. Expected output: true, 'some_value'.\n");
    _Bool replaced1 = replace(addresses, "Greg", "some_value");
    printf("Actual output: %s, %s.\n", replaced1?"true":"false", get(addresses, "Greg"));

    // Tests an invalid key
    printf("Changing value at key 'John' to 'some_value'. Expected output: false, '(null)'.\n");
    _Bool replaced2 = replace(addresses, "John", "some_value");
    printf("Actual output: %s, %s.\n", replaced2?"true":"false", get(addresses, "John"));

    // Test case for clear

    // Test on a full hash table
    clear(addresses);
    print_dictionary(addresses);

    // Test on an empty table
    clear(addresses);
    print_dictionary(addresses);

    return EXIT_SUCCESS;
}
