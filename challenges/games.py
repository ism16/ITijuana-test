from typing import List, Generator


class Rook:
    def __init__(self, sequence: str):
        self.x: int = 0
        self.y: int = 0
        self.distance: int = 0

        commands: List = sequence.split(',')

        for command in commands:
            cmd, steps = command.strip().split(' ')
            steps: int = int(steps)  # type: ignore

            if cmd == 'up':
                self.up(steps)
            elif cmd == 'down':
                self.down(steps)
            elif cmd == 'right':
                self.right(steps)
            elif cmd == 'left':
                self.left(steps)
            else:
                pass
        
        self.steps: int = abs(self.x)+abs(self.y)
        self.euclidean: float = ((self.x**2) + (self.y**2))**(1/2)
        print(f'Traveled distance: {self.distance} units')
        print(f'Distance in steps: {self.steps} units')
        print(f'Distance from origin: {self.euclidean} units')

    
    def up(self, steps: int):
        self.y += steps
        self.distance += steps
    
    def down(self, steps: int):
        self.y -= steps
        self.distance += steps

    def right(self, steps: int):
        self.x += steps
        self.distance += steps
    
    def left(self, steps: int):
        self.x -= steps
        self.distance += steps