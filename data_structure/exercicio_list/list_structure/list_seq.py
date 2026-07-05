from list_structure.add_remove_functions import OperationFunctions
from time import sleep
class ListSeq:
    def __init__(self) -> None:
        self.itens = [1,3,2,4,4,4,2]
        self.n = 0
        
            
    def show_itens(self):
        if len(self.itens) != 0:
            print("SHOWING ALL ITEMS IN THE LIST")
            print("The size of the list is: ", len(self.itens))
            print("The content of the list is: ", self.itens)        
        
        else: print(f"Exist {self.n} elements on the list.")
        
        input("\n>> Press any key to continue...")
        
        
    def insert_item(self):
        try:
            value = int(input("Value to be added:"))
            position = int(input("Position to be added: Enter -1 for more functions"))
        
        
            if position == -1:
                position = OperationFunctions.menu('add')
                position = len(self.itens) -1 if position == -1 else position
                
            if position is not None:
                for i in range(len(self.itens) - 1 , -1, -1):
                    if i > position:
                        self.itens[i] = self.itens[i - 1]
                self.itens[position] = value 
                print("✅ Item added successfully ", self.itens)
                input("\n>> Press any key to continue...")
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            sleep(1.3)
            return
        
        
    def remove_item(self):
        try:
            position = int(input("Enter index position to remove: Enter -1 for more functions"))
    
            if position == -1:
                position = OperationFunctions.menu('remove')
                position = len(self.itens) -1 if position == -1 else position
            if position is not None:
                len_filled = len(self.itens)
                if position < 0 or position >= len_filled:
                    print("Invalid position! Please try again.")
                    return
                if self.itens[position] == 0:
                    print("This position is already empty! Please try again.")
                    return
                for i in range(position, len_filled - 1):
                    self.itens[i] = self.itens[i + 1]
                self.itens[len_filled - 1] = 0
                        
                print("✅ Item removed successfully ", self.itens)
                input("\n>> Press any key to continue...")
                
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            sleep(1.3)
            return
    
    def show_item(self):
        while True:
            position = int(input(f"Enter index position to show: [0-{len(self.itens)}]"))
            try:
                print("The number that is on the this Position", self.itens[position])
                input("\n>> Press any key to continue...")
                break
            except IndexError:
                print(f"Try again! Exist  indices in list:  {self.itens}")
                
    def show_position(self):
        while True:
            try:
                value_to_get = int(input(f"Enter the value to return your indice: {self.itens}: "))
            
            
                count = 0
                list_indices = []
                for i, value in enumerate(self.itens):
                    if value_to_get == value:
                        count += 1
                        list_indices.append(i)
                if count == 0:
                    print("Doesn't exist this number in the list! Try again!")
                elif count == 1:
                    # Unpack list_indices to show without brackets, separated by comma
                    print(f"The number is on the indice {*list_indices,}")
                    break
                else:
                    # Unpack list_indices to show without brackets, separated by commas
                    print(f"The number {value_to_get} appear {count} times in the indices {*list_indices,}")
                    break
            
                input("\n>> Press any key to continue...")
            except ValueError:
                    print("Invalid input! Please enter a valid integer.")
                    sleep(1.3)
                    return
            
    def clear_list(self):
        for i in range(len(self.itens)):
            self.itens[i] = 0
            
        print("✅ All elements of list set to 0!")
        input("\n>> Press any key to continue...")
        