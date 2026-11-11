from text_editor import TextEditor

editor = TextEditor()

while True:
    print("\n===== TEXT EDITOR =====")
    print("1. Type text")
    print("2. Delete last character")
    print("3. Undo")
    print("4. Show text")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text to append: ")
        editor.type_text(text)

    elif choice == "2":
        editor.delete_last_character()

    elif choice == "3":
        editor.undo()

    elif choice == "4":
        editor.show_text()

    elif choice == "5":
        print("Exiting Text Editor...")
        break

    else:
        print("Invalid choice.")