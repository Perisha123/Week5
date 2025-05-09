from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced Search (by ID and Name)")
    print("7. Insert Cousrse")
    print("8. Search Course by ID and Name")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-8): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
        elif choice == '6':
            name = input("Enter name to search:")
            id = input("Enter id to search:")
            users = advanced_search(id, name)
            if users:
             for user in users:
               print(user)
        elif choice == '7':
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            unit = int(input("Enter Course Unit: "))
            insert_course(course_id, course_name, unit)
            print("Course inserted successfully.")

        elif choice == '8':
            course_id = input("Enter Course ID: ")
            user_name = input("Enter Associated User Name: ")
            courses = search_course(course_id, course_name)
            if courses:
                for c in courses:
                    print(f"Course ID: {c[0]}, Name: {c[1]}, Unit: {c[2]}")
            else:
                print("No course found.")
            break
        else:
            print("Invalid choice, try again.")
        


if __name__ == "__main__":
    main()
