/********* main.c ********
    Student Name 	= Matthé Bekkers
    Student Number	= 101297066
*/
#ifndef MAIN_C
#define MAIN_C

// Includes go here
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>
#include "a2_nodes.h"
#include "a2_functions.h"

int main()
{
    FILE *csv_file = fopen("user_details.csv", "r");
    if (csv_file == NULL)
    {
        perror("Error opening the CSV file");
        return 1;
    }
    // Parse CSV data and create users
    user_t *users = read_CSV_and_create_users(csv_file, 50);

    fclose(csv_file);

    int choice = menu_choice();

    while(choice != 6){
        switch (choice){
        case 1:
            const char username[30] = "";
            const char password[30] = "";
            printf("Please enter a username: ");
            scanf("%s", &username);
            printf("Please enter a password: ");
            scanf("%s", &password);
            add_user(users, username, password);
            choice = menu_choice();
            break;
        case 2:
            const char user_to_find_1[30] = "";
            const char original_password[15] = "";
            printf("Please enter a username to update the password: ");
            scanf("%s", &user_to_find_1);
            user_t *found_user_1 = find_user(users, user_to_find_1);
            if(found_user_1 == NULL) {
                printf("***********************************************\n");
                printf("     User not found. Returning to menu...      \n");
                printf("***********************************************\n");
                choice = menu_choice();
                break;
            }
            printf("Please enter the old password for user %s: ", user_to_find_1);
            scanf("%s", original_password);
            if(strcmp(found_user_1->password, original_password) != 0) {
                printf("***********************************************\n");
                printf("    Incorrect password. Returning to menu...   \n");
                printf("***********************************************\n");
                choice = menu_choice();
                break;
            }
            printf("Password correct. Please enter the new password for user %s: ", user_to_find_1);
            scanf("%s", &found_user_1->password);
            printf("***********************************************\n");
            printf("    Password changed. Returning to menu...    \n");
            printf("***********************************************\n");
            choice = menu_choice();
            break;
        case 3:
            const char user_to_find_2[30] = "";
            int posts_choice = 0;
            printf("Please enter a username to manage posts: ");
            scanf("%s", &user_to_find_2);
            user_t *found_user_3 = find_user(users, user_to_find_2);
            if(found_user_3 == NULL) {
                printf("***********************************************\n");
                printf("     User not found. Returning to menu...      \n");
                printf("***********************************************\n");
                choice = menu_choice();
                break;
            }
            printf("***********************************************\n");
            printf("          Managing %s's posts...          \n", user_to_find_2);
            printf("***********************************************\n");
            if(found_user_3->posts == NULL) {
                printf("Note: no posts available for this user.\n");
            }
            printf("1. Add a new post\n2. Remove a post\n3. Return to main menu\nEnter your choice: ");
            scanf("%d", &posts_choice);
            switch (posts_choice) {
            case 1:
                const char post_content[250] = "";
                printf("Please enter your post's text: ");
                scanf(" %[^\n]s", post_content);
                add_post(found_user_3, post_content);

                choice = menu_choice();
                break;
            case 2:
                _Bool post_deleted_successfully = delete_post(found_user_3);
                if(post_deleted_successfully) {
                    printf("Deleted post successfully. Updated posts: \n");
                    if(found_user_3->posts == NULL) {
                        printf("No posts for this user.\n");
                    }
                    else {
                        display_all_user_posts(found_user_3);
                    }
                }
                choice = menu_choice();
                break;
            case 3:
            printf("Returning to menu...\n");
            choice = menu_choice();
                break;
            default:
                printf("Invalid option. Returning to menu...\n");
                break;
            }
            break;
        case 4:
            const char user_to_find_4[30] = "";
            int friends_choice = 0;
            printf("Please enter a username to manage friends: ");
            scanf("%s", &user_to_find_4);
            user_t *found_user_4 = find_user(users, user_to_find_4);
            if(found_user_4 == NULL) {
                printf("***********************************************\n");
                printf("     User not found. Returning to menu...      \n");
                printf("***********************************************\n");
                choice = menu_choice();
                break;
            }
            printf("1. Add a new friend\n2. Remove a friend\n3. Return to main menu\n Enter your choice: ");
            scanf("%d", &friends_choice);

            if (friends_choice == 1) {
                const char new_friend_name[30] = "";
                printf("Please enter a new friend: ");
                scanf("%s", &new_friend_name);
                add_friend(found_user_4, new_friend_name);
                choice = menu_choice();
                break;
            }
            else if(friends_choice == 2) {
                char friend_to_delete[30] = "";
                printf("Current friends list:\n");
                display_user_friends(found_user_4);
                printf("Please select the friend to delete: ");
                scanf("%s", &friend_to_delete);
                
                _Bool passed = delete_friend(found_user_4, friend_to_delete);
                if(!passed) {
                    printf("Error while deleting friend.\n");
                }
                choice = menu_choice();
                break;
            }
            else if(friends_choice == 3) {
                printf("Returning to menu...\n");
                choice = menu_choice();
                break;
            }
            
            else {
                printf("Invalid choice. Returning to menu...\n");
                choice = menu_choice();
                break;
            }
            break;
        case 5:
            int n_posts_to_display = 3;
            const char user_to_find_5[30];
            printf("Please enter a username for which the posts are to be displayed: ");
            scanf("%s", user_to_find_5);
            user_t *user_post_display = find_user(users, user_to_find_5);
            if(user_post_display->posts == NULL || user_post_display == NULL) {
                break;
            }
            if(user_post_display->posts == NULL) {
                printf("No posts for this user. Returning to menu...\n");
                choice = menu_choice();
                break;
            }
            display_posts_by_n(user_post_display, n_posts_to_display);
            
            //printf("No more posts to display.\n");
            choice = menu_choice();
            break;
        case 6:
            printf("Exiting...\n");
            break;
        default:
            printf("Invalid choice. Please make another selection.\n");
            choice = menu_choice();
        }
    }

}

#endif