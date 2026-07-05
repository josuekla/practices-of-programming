class OperationFunctions:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def show_menu_add():
        print("LIST OF FUNCTION ADD ➕")
        print("1. Insert the value in the first position")
        print("2. Insert the value in the last position")
        print("3. Insert the value in a specific position")
        print("0. Back to menu")
    
    @staticmethod
    def show_menu_remove():
        print("LIST OF FUNCTION REMOVE ➖")
        print("4. Remove the first value")
        print("5. Remove the last value")
        print("6. Remove the value in a item position")
        print("0. Back to menu")
        
        
    @staticmethod
    def menu(flag_operator) -> int | None:
        while True:
            if flag_operator == "add":
                OperationFunctions.show_menu_add()
            elif flag_operator == "remove":
                OperationFunctions.show_menu_remove()
                
            value = int(input("Enter the number: "))
            match value:
                case 1:
                    print("Insert the value in the first position")
                    return 0
                case 2:
                    print("Insert the value in the last position")
                    return -1
                case 3:
                    value_to_insert = int(input("Enter the number to add in the list: "))
                    return value_to_insert
                case 4:
                    return 0
                case 5:
                    return -1
                case 6:
                    value_to_remove = int(input("Enter the number to remove in the list: "))
                    return value_to_remove
                case 0:
                    return None # Ou return -2, dependendo da sua lógica
                    
                
            
        