# =========== Import libraries ===========
from datetime import datetime

# =========== Define functions ===========
def login():
    # Get username and password from user repeatedly until correct information is entered
    username_ok = False
    password_ok = False
    while (username_ok == False) and (password_ok == False):
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        # Open registered users database file 'user.txt'
        with open('user.txt') as f:
            # For every line in the file, store each word in the list 'words'
            for line in f:
                words = line.replace(',','').split()
                
                # If the first word in the line matches the entered username, set 'username_ok' to True, then check password
                if username == words[0]:
                    username_ok = True
                    
                    # If the second word in the line matches the entered password, set 'password_ok' to True, then terminate the loop
                    if password == words[1]:
                        password_ok = True
                        break
                    # Even if the password does not match, terminate the loop
                    
                    else:
                        break
                    
        # Error messages for invalid username or password            
        if username_ok == False:
            print(f'  ►  The username "{username}" is not registered in our database. Please try again.\n')
        
        if (username_ok == True) and (password_ok == False):
            # Re-initialize 'username_ok' for the start of the input block loop
            username_ok = False
            print(f'  ►  The password for username "{username}" is incorrect. Please try again.\n')
    
    return username


def reg_user():
    # START of New Username input block, loops until user enters a username that has not yet been taken.
    new_username_ok = False
    while new_username_ok == False:
        new_username = input('Enter a new username: ')
        
        # Open registered users database file 'user.txt'
        with open('user.txt') as f:
            # For every line in the file, store each word in the list 'words'
            for line in f:
                words = line.replace(',','').split()
                
                # If the first word in the line matches the entered username, set 'new_username_ok' to False then break the loop
                if new_username == words[0]:
                    print(f'  ►  The username "{new_username}" is already taken.\n')
                    new_username_ok = False
                    break
                
                else:
                    new_username_ok = True
    # END of New Username input block

    # START of New Password input block
    new_password = input('Set new password: ')
    re_password = input('Re-enter password: ')
    
    # Compare the two passwords entered by the user and if they match, append the new username and new password to 'user.txt'
    if new_password == re_password:
        with open('user.txt','a') as f:
            f.write('\n' + new_username + ', ' + new_password)
        print('  ►  User registration successful!')
    
    else:
        print('  ►  The passwords you entered did not match. Returning to menu.')
    # END of New Password input block


def add_task():
    # START of task owner username input block, loops until user enters a username that is found in the database
    username_ok = False
    while username_ok == False:
        task_username = input('Enter the username to whom this task will be assigned to: ')
        
        # Open registered users database file 'user.txt'
        with open('user.txt') as f:
            # For every line in the file, store each word in the list 'words'
            for line in f:
                words = line.replace(',','').split()
                
                # If the first word in the line matches the entered username, set 'username_ok' to True then break the loop
                if task_username == words[0]:
                    username_ok = True
                    break
        
        # If the entered username doesn't match any of the usernames in the database, an error message is displayed
        if username_ok == False:
            print(f'  ►  The username "{task_username}" is not registered in our database. Please try again.\n')
    # END of task owner username input block

    # Input task information then append this information to file 'tasks.txt'
    task_title = input('Enter the title of the task: ')
    task_desc = input('Enter the description of the task: ')
    task_due = input('Enter the due date of the task (ie. 14 Dec 2022): ')
    curr_date = datetime.today()
    curr_date = curr_date.strftime('%d %b %Y')
    
    with open('tasks.txt','a') as f:
        f.write(f'{task_username}, {task_title}, {task_desc}, {curr_date}, {task_due}, No\n')
    print('  ►  Task addition successful!')


def view_all():
    # Open file 'tasks.txt' then for every line in this file, parse through the task information and then display the information
    i = 0
    with open('tasks.txt') as f:
        for line in f:
            i += 1
            task_info = line.split(', ')
            task_info5 = task_info[5].removesuffix('\n')
            print(f'''───────────────────────► TASK {i} ◄─────────────────────────────
Task:               {task_info[1]}
Assigned to:        {task_info[0]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task complete?      {task_info5}
Task description:
    {task_info[2]}
──────────────────────────────────────────────────────────────\n''')


def view_mine():
    # Open file 'tasks.txt' then for every line in this file, parse through the task information
    i = 0
    task_num_list = []
    with open('tasks.txt') as f:
        for line in f:
            i += 1
            task_info = line.split(', ')
            
            # If the first word in the line matches the logged-in username, display the task information
            if task_info[0] == username:
                # Append current line/task number to 'task_num_list'
                task_num_list.append(str(i))
                task_info5 = task_info[5].removesuffix('\n')
                print(f'''───────────────────────► TASK {i} ◄─────────────────────────────
Task:               {task_info[1]}
Assigned to:        {task_info[0]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task complete?      {task_info5}
Task description:
    {task_info[2]}
──────────────────────────────────────────────────────────────\n''')

    # If no tasks have been assigned to the user, skip 'Task selection' and 'Mark complete or edit task' blocks, then return to main menu
    if task_num_list == []:
        print(f'  ►  No tasks have been assigned to username "{username}".')

    task_num_ok = False
    # START of 'Task selection' block
        # Loop until user enters a valid task number
    while task_num_ok == False and task_num_list != []:
        task_num = input('Select task to edit. Enter TASK #, or enter "-1" to go back to main menu: ')
        
        if task_num == '-1':
            task_num_ok = True
            break
        
        else:
            # Check if the task number entered by the user is in his list of tasks
            for x in task_num_list:
                if x == task_num:
                    task_num_ok = True
                    print(f'  ►  TASK {task_num} has been selected.')
                    break

            if task_num_ok == False:
                print('  ►  Invalid TASK #.')
    # END of 'Task selection' block

    # START of 'Mark complete or edit task' block
    if task_num_ok == True and task_num != '-1' and task_num_list != []:
        # Ask user whether to mark task as complete or edit task
        task_selected1 = input('''\nSelect one of the following Options below:
m - Mark task as complete
e - Edit task
: ''').lower()

        # START of 'Mark task as complete' block
        if task_selected1 == 'm':

            # Read contents of 'tasks.txt' and load all lines to memory
            with open('tasks.txt') as f:
                contents = f.readlines()

            # Open 'tasks.txt' for writing
            with open('tasks.txt','w') as f:
                # Find line corresponding to task selected, then replace completeness info with 'Yes'
                for j, line in enumerate(contents,1):
                    if j == int(task_num):
                        task_info = line.split(', ')
                        task_info[5] = 'Yes\n'
                        task_info = ', '.join(task_info)
                        f.writelines(task_info)

                    else:
                        f.writelines(line)
                        
            print(f'  ►  TASK {task_num} has been marked complete.')            
        # END of 'Mark task as complete' block
        
        # START of 'Edit task' block
        elif task_selected1 == 'e':

            # Check if task has been completed
            # Read contents of 'tasks.txt' and load all lines to memory
            with open('tasks.txt') as f:
                contents = f.readlines()
                # Find line corresponding to task selected, then store that line to 'task_info'
                for j, line in enumerate(contents,1):
                    if j == int(task_num):
                        task_info = line.split(', ')
                        break
            
            # If task has not been completed, proceed to edit task
            if task_info[5] == 'No\n' or task_info[5] == 'No':
                
                # START of 'Task user reassign' block
                username_ok = False
                while username_ok == False:
                    task_username = input(f'Enter the username to whom TASK {task_num} will be reassigned to: ')
                    
                    # Open registered users database file 'user.txt'
                    with open('user.txt') as f:
                        # For every line in the file, store each word in the list 'words'
                        for line in f:
                            words = line.replace(',','').split()
                            
                            # If the first word in the line matches the entered username, set 'username_ok' to True then break the loop
                            if task_username == words[0]:
                                username_ok = True
                                break
                    
                    # If the entered username doesn't match any of the usernames in the database, an error message is displayed
                    if username_ok == False:
                        print(f'  ►  The username "{task_username}" is not registered in our database. Please try again.\n')
                # END of 'Task user reassign' block

                task_due = input('Enter the adjusted due date of the task (ie. 22 Dec 2022): ')
                curr_date = datetime.today()

                # Read contents of 'tasks.txt' and load all lines to memory
                with open('tasks.txt') as f:
                    contents = f.readlines()

                # Open 'tasks.txt' for writing
                with open('tasks.txt','w') as f:
                    # Find line corresponding to task selected, then replace username, date assigned, and due date
                    for j, line in enumerate(contents,1):
                        if j == int(task_num):
                            task_info = line.split(', ')
                            task_info[0] = task_username
                            task_info[4] = task_due
                            task_info[3] = curr_date.strftime('%d %b %Y')
                            task_info = ', '.join(task_info)
                            f.writelines(task_info)

                        else:
                            f.writelines(line)

                print(f'  ►  TASK {task_num} has been successfully edited.\n')
            
            # If task has been completed, return to main menu
            elif task_info[5] == 'Yes\n' or task_info[5] == 'Yes':
                print(f'  ►  TASK {task_num} cannot be edited as it has already been completed.\n')
        # END of 'Edit task' block
        
        else:
            print('  ►  Invalid input. Returning to main menu.')
    # END of 'Mark complete or edit task' block


def reports():
    i = 0
    task_info = []
    num_tasks = 0
    num_comp_tasks = 0
    num_uncomp_tasks = 0
    num_overdue_tasks = 0
    curr_date = datetime.today()

    # START of 'Tasks report' block
    with open('tasks.txt') as f:
        for line in f:
            # Count total tasks
            num_tasks += 1
            # Split the current line to get a list containing task information
            task_info = line.split(', ')
            
            # Count completed tasks
            if task_info[5] == 'Yes' or task_info[5] == 'Yes\n':
                num_comp_tasks += 1
            
            # Count uncompleted tasks
            if task_info[5] == 'No' or task_info[5] == 'No\n':
                num_uncomp_tasks += 1
            
            # Count uncompleted and overdue tasks
            task_due = datetime.strptime(task_info[4], '%d %b %Y')
            if (task_info[5] == 'No' or task_info[5] == 'No\n') and (task_due > curr_date):
                num_overdue_tasks += 1

    perc_comp_tasks = (num_comp_tasks / num_tasks) * 100
    perc_uncomp_tasks = (num_uncomp_tasks / num_tasks) * 100
    perc_overdue_tasks = (num_overdue_tasks / num_tasks) * 100

    with open('task_overview.txt','w',encoding='utf-8') as f:
        f.write(f'''───────────── TASK OVERVIEW ──────────────
Total Tasks         :       {num_tasks}
Completed Tasks     :       {num_comp_tasks} ({perc_comp_tasks:.2f}%)
Uncompleted Tasks   :       {num_uncomp_tasks} ({perc_uncomp_tasks:.2f}%)
Overdue Tasks       :       {num_overdue_tasks} ({perc_overdue_tasks:.2f}%)
──────────────────────────────────────────\n''')
    # END of 'Tasks report' block


    # START of 'Users report' block
    # Initialize 'user_overview.txt' file for appending task information per user
    with open('user_overview.txt','w',encoding='utf-8') as f:
        f.write('')

    # Initialize a dictionary to store the results for each user
    results = {}

    with open('tasks.txt') as f:
        for line in f:
            # Split the current line to get a list containing task information
            task_info = line.split(', ')

            # Get the user specified in the task information
            user = task_info[0]

            # Initialize an internal dictionary to store the results for the current user, if necessary
            if user not in results:
                results[user] = {
                    'assigned_tasks': 0,
                    'completed_tasks': 0,
                    'overdue_tasks': 0}

            # Increment the total tasks counter for the current user
            results[user]['assigned_tasks'] += 1

            # Check if the task is marked as completed
            if task_info[5].strip() == 'Yes':
                # Increment the completed tasks counter for the current user
                results[user]['completed_tasks'] += 1
            else:
                # Convert the due date to a datetime object
                due_date = datetime.strptime(task_info[4], '%d %b %Y')

                # Check if the current date is past the due date
                if datetime.now() > due_date:
                    # Increment the overdue tasks counter for the current user
                    results[user]['overdue_tasks'] += 1

        # Iterate over the results for each user
        for user, data in results.items():
            # Calculate the percentage of the total tasks that have been assigned to the user
            user_perc_assigned_tasks = data['assigned_tasks'] / num_tasks * 100

            # Calculate the percentage of the tasks assigned to the user that have been completed
            user_perc_comp_tasks = data['completed_tasks'] / data['assigned_tasks'] * 100

            # Calculate the percentage of the tasks assigned to the user that must still be completed
            user_perc_uncomp_tasks = (data['assigned_tasks'] - data['completed_tasks']) / data['assigned_tasks'] * 100

            # Calculate the percentage of the tasks assigned to the user that have not yet been completed and are overdue
            user_perc_overdue_tasks = data['overdue_tasks'] / data['assigned_tasks'] * 100

            # Append the task information for each user in file 'user_overview.txt'
            with open('user_overview.txt','a',encoding='utf-8') as f:
                f.write(f'''─────────────── USER OVERVIEW ────────────────
Username                    :       {user}
Assigned Tasks              :       {data["assigned_tasks"]} ({user_perc_assigned_tasks:.2f}%)
User's Completed Tasks      :       {data["completed_tasks"]} ({user_perc_comp_tasks:.2f}%)
User's Uncompleted Tasks    :       {data["assigned_tasks"] - data["completed_tasks"]} ({user_perc_uncomp_tasks:.2f}%)
User's Overdue Tasks        :       {data["overdue_tasks"]} ({user_perc_overdue_tasks:.2f}%)
──────────────────────────────────────────────\n''')
    # END of 'Users report' block

    print('  ►  Reports successfully generated!\n')


def stats():
    # Call function to generate reports
    reports()
    # Read report files and display the contents
    with open('task_overview.txt',encoding='utf-8') as f, open('user_overview.txt',encoding='utf-8') as g:
        print(f.read())
        print(g.read())


print('''
┌────────────────────────────────────┐
│   Welcome to Task Manager v2.0!    │
└────────────────────────────────────┘
\n''')


# Login screen
username = login()
    
# START of Main Menu screen
while True:
    # Main menu for admin user
    if username == 'admin':
        menu = input('''\nSelect one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # Main menu for non-admin user
    else:
        menu = input('''\nSelect one of the following Options below:
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()

    # 'Register a user'
    # Check if user logged in is 'admin'
    if (menu == 'r') and (username == 'admin'):
        reg_user()
        
    # 'Add a task'
    elif menu == 'a':
        add_task()

    # 'View all tasks'
    elif menu == 'va':
        view_all()

    # 'View my tasks'
    elif menu == 'vm':
        view_mine()

    # 'Generate reports'
    elif menu == 'gr':
        reports()

    # 'Display statistics'
    # Check if user logged in is 'admin'
    elif (menu == 'ds') and (username == 'admin'):
        stats()
        
    # 'Exit'
    elif menu == 'e':
        print('  ►  Thank you for using Task Manager v2.0!\n')
        exit()

    # If input is invalid, goes back to main menu
    else:
        print('  ►  Invalid input. Please try again.')
# END of Main Menu screen