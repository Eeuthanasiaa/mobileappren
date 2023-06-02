from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp


class MainApp(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Главная'
            icon: 'home-circle'


            MDLabel:
                text: 'Главная'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Связаться'
            icon: 'information'


            MDLabel:
                text: 'обратная связь'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Профиль'
            icon: 'account-circle'

            MDLabel:
                text: 'Профиль'
                halign: 'center'
'''
        )

if __name__ == '__main__':
    MainApp().run()