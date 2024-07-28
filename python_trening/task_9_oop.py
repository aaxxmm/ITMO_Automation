#
# class Button:
#
#     Type: str = 'Кнопка'
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
# #созд экземпляры класса
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
# #получ доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.text)
#
# print('/n')

# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)



# class ButtonTwo:
#
#      def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#      def click(self):
#          return "Клик по локатору - {}".format(self.loc)
# #создаем экземпляры класса
# home_two = ButtonTwo('Домой', '/home', 'button#home')
#
# #вызываем метод
# print(home_two.click())


# class Input:
#
#     def __init__(self, Loc):
#         self.Loc = Loc
# search = Input('Input#search')
#
# print(search.Loc)


class Input:
class Button:
class Title:
class Link:

    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text

search = Input('Input#search')

print(search.Loc)