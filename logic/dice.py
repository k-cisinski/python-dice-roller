
import random

class Dice:
    
    _TEMPLATES = {
'd4': [
            "      /\\        ",
            "     /  \\       ",
            "    /    \\      ",
            "   /  /\\  \\    ",
            "  /  /  \\  \\   ",
            " /____{val}____\\",
            " \\__________/  " 
        ],
        'd6': [
            "    ________       ",
            "   /\\       \\    ",
            "  /  \\       \\   ",
            " /    \\_______\\  ",
            " \\    /       /   ",
            "  \\  /   {val}  / ",
            "   \\/_______/     "
        ],
        'd8': [
            "      /\\       ",
            "     /  \\      ",
            "    /    \\     ",
            "   /  {val}  \\ ",
            "  /________\\   ",
            "  \\        /   ",
            "   \\      /    ",
            "    \\    /     ",
            "     \\  /      ",
            "      \\/       "
        ],
        'd10': [
            "      /\\       ",
            "     /  \\      ",
            "    /    \\     ",
            "   /      \\    ",
            "  /   {val}   \\",
            " |          |    ",
            "  \\        /   ",
            "   \\      /    ",
            "    \\    /     ",
            "     \\  /      ",
            "      \\/       "
        ],
        'd12': [
            "    ____    ",
            "  .'    '.  ",
            " /  /\\    \\ ",
            "|  |  |    |",
            "|  |{val}|    |",
            " \\  \\/    / ",
            "  '.____.'  "
        ],
        'd20': [
            "      /\\      ",
            "     /  \\     ",
            "    / /\\ \\    ",
            "   / /  \\ \\   ",
            "  / / {val} \\ \\  ",
            " / /______\\ \\ ",
            " \\__________/ "
        ]
    }
    
    def __init__(self, dice_type):
        
        self.dice_type = dice_type
        
        if dice_type not in self._TEMPLATES:
            raise ValueError(f"Unknown dice type: {dice_type}")
    
    @classmethod
    def is_valid_type(cls, dice_type):
        return dice_type in cls._TEMPLATES
    
    
    def roll(self):
        sides = int(self.dice_type[1:])
        return random.randint(1, sides)
    
    def get_drawing(self, rolled_value):
        template = self._TEMPLATES[self.dice_type]
        
        value_str = f"{rolled_value:^2}"
        
        raw_lines = [line.replace("{val}", value_str) for line in template]
        
        max_width = max(len(line) for line in raw_lines)
        
        padded_lines = [line.ljust(max_width) for line in raw_lines]
        
        return padded_lines