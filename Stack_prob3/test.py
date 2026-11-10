from browser import BrowserHistory

browser = BrowserHistory()

while True:
    print("\n===== BROWSER HISTORY =====")
    print("1. Visit a page")
    print("2. Back")
    print("3. Forward")
    print("4. Show current page")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        page = input("Enter a page address: ")
        if not page.strip():
            print("Page cannot be empty")
        else:
            browser.visit(page)

    elif choice == "2":
        browser.back()
        
    elif choice == "3":
        browser.forward()
    
    elif choice == "4":
        browser.show_current_page()
        
    elif choice == "5":
        print("Exiting Browser History...")
        break
    
    else:
        print("Invalid Input, Please try again!")