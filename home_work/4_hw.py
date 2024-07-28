# class Rectangle:
#
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)
#
# rect1 = Rectangle(8, 12)
# rect2 = Rectangle(6, 2)
# rect3 = Rectangle(7, 5)
#
# print(f"Прямоугольник 1: Площадь = {rect1.calculate_area()}, Периметр = {rect1.calculate_perimeter()}")
# print(f"Прямоугольник 2: Площадь = {rect2.calculate_area()}, Периметр = {rect2.calculate_perimeter()}")
# print(f"Прямоугольник 3: Площадь = {rect3.calculate_area()}, Периметр = {rect3.calculate_perimeter()}")



# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         print(f"Addition: {self.a + self.b}")
#
#     def multiplication(self):
#         print(f"Multiplication: {self.a * self.b}")



class Saidbar:

    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"

text_box = Saidbar("Text_Box")
text_check = Saidbar("Check_Box")
text_radio = Saidbar("Radio_Button")
text_web_tables = Saidbar("Web_Tables")
text_buttons = Saidbar("Buttons")
text_links = Saidbar("Links")
text_broken_links = Saidbar("Broken_Links - Images")
text_upload = Saidbar("Upload and Download")
text_dynamic = Saidbar("Dynamic Properties")

# клик для каждой кнопки
print(text_box.text)
print(text_check.text)
print(text_radio.text)
print(text_web_tables.text)
print(text_buttons.text)
print(text_links.text)
print(text_broken_links.text)
print(text_upload.text)
print(text_dynamic.text)


print(text_box.click())
print(text_check.click())
print(text_radio.click())
print(text_web_tables.click())
print(text_buttons.click())
print(text_links.click())
print(text_broken_links.click())
print(text_upload.click())
print(text_dynamic.click())