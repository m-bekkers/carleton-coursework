/********* main.c ********
	
	Student Name 	= Matthé Bekkers
	Student Number	= 101297066
*/

//Complete the includes
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "a1_functions.h"
#include "a1_data_structures.h"
//#include "a1_data_structures.h"

int main()
{
    char project_name[255];
    unsigned short int number_milestones, actual_project_duration;
    float planned_project_duration = 0;
    float planned_project_cost = 0;
    _Bool project_completed = 0;
    const int *num_activities = NUM_ACTIVITIES;

    /** 1-  Display a welcome message **/
    
    printf("*-----------------------------------------------------*\n");
    printf("*            Welcome to the scheduler tool!           *\n");
    printf("*-----------------------------------------------------*\n");
    printf("                                                       \n");

    /** 2- Get the project's name and number of milestones **/

    printf("*-----------------------------------------------------*\n");
    printf("*                    Main Menu                        *\n");
    printf("*-----------------------------------------------------*\n");
    printf("                                                       \n");
    printf("* Please enter the project name: ");
    scanf("%s", project_name);
    printf("* You selected '%s' as your project.\n", project_name);
    printf("* Select your number of milestones below.\n");
    number_milestones = get_input_usi();
    while (number_milestones < 1 || number_milestones > 5) {
        printf("Please select a value between 1 and 5: ");
        scanf("%hu", &number_milestones);
    }
    printf("*  You selected '%d' as your number of milestones.\n", number_milestones);


    /** 3- Initialize all milestones and activities.
     * You need an array of milestones. 
     * The capacity of the array must be the max number of milestones the program 
     * can handle as per the instructions **/

    milestone_t milestone_arr[5];
    //activity_t activity_arr[5][3];

    
    
    printf("Project initialisation sucessful. Loading into main menu...\n");
    
    /** 4- Initialize the project **/

    project_t project = init_project(project_name, milestone_arr, number_milestones, num_activities);
    
    // Calculate project cost & project duration
    for (int i = 0; i < number_milestones; i++) {
        for (int j = 0; j < NUM_ACTIVITIES; j++) {
            printf("Milestone %hu, activity %d cost: %.f\n", i + 1, j + 1, milestone_arr[i].activity_list[j].planned_cost);
            planned_project_cost += milestone_arr[i].activity_list[j].planned_cost;
            planned_project_duration += milestone_arr[i].activity_list[j].planned_duration;
        }
    }

    planned_project_duration = (ceil(planned_project_duration / 8));

    printf("The total planned cost for the project is %.f$.\n", planned_project_cost);
    printf("The total planned duration for the project is %.f hours.\n", planned_project_duration);

    project.planned_cost = planned_project_cost;
    project.planned_duration = planned_project_duration;

    /** 5- Print the main menu **/
    print_main_menu();

    /** 6- Get user choice and handle it as per the instructions**/
    unsigned short int initchoice = get_input_usi();
    while (initchoice < 1 || initchoice > 3) {
        printf("Incorrect value. Please enter a value between 1 and 3\n");
        initchoice = get_input_usi();
    }

    while (initchoice != 3) {
        if (initchoice == 2) {
            print_project_stats(project, milestone_arr, number_milestones, NUM_ACTIVITIES);
            break;
        }
        else if (initchoice == 1) {
            for (int i = 0; i < number_milestones; i++) {
                printf("Milestone %d name: %s", i + 1, milestone_arr[i].name);
                for (int j = 0; j < NUM_ACTIVITIES; j++) {
                    printf("Activity %d name: %s", i + 1, milestone_arr[i].activity_list[j].name);
                }
            }
            break;
        }
    }
    
    printf("Exiting...");
    
    return EXIT_SUCCESS;
}