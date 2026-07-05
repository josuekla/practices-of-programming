class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def clear_screen():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')