from time import sleep
import keyboard

# =====================
from utils import Utils
from list_structure import ListSeq


obj = ListSeq()

def show_menu():
    Utils.clear_screen()
    print("\t EDITOR OF LISTS")
    print("\t 1. SHOW ALL ITEMS")
    print("\t 2. ADD ITEM")
    print("\t 3. REMOVE ITEM")
    print("\t 4. SHOW SPECIFIC ITEM")
    print("\t 5. SHOW THE POSITION OF AN ITEM")
    print("\t 6. CLEAR THE LIST")
    print("0. EXIT")


def input_item():
    while True:
        try:
            show_menu()
            value = int(input(">> Choose an option: "))
            if value in [0, 1, 2, 3, 4, 5, 6]:
                return value
        except Exception:
            print("INVALID OPTION! Please try again.")
            sleep(1)
            
def action_item(option):
    match option:
        case 1:
            obj.show_itens()
        case 2:
            obj.insert_item()
        case 3:
            obj.remove_item()
        case 4:
            obj.show_item()
        case 5:
            obj.show_position()
        case 6:
            obj.clear_list()
        
    

def main():
    while True:
        value = input_item()
        if value == 0:
            print("Exiting the program...")
            sleep(1.5)
            break
        action_item(value)
    




if __name__ == '__main__':
    main()