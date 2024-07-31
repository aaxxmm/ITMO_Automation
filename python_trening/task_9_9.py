# task_9_oop_1.py

class Checks:
    def __init__(self, loc):
        self.loc = loc

    def check_text(self):
        return self.loc

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Button(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Image(Checks):
    def __init__(self, loc):
        super().__init__(loc)

# Usage
from task_9_oop_1 import Link, Input, Button, Image

link = Link('home', 'Homepage link')
input_field = Input('search')
button = Button('submit')
image = Image('logo')

objects = [link, input_field, button, image]

for obj in objects:
    print(obj.check_text())