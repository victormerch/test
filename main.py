from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # Crea un layout vertical
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Crea un Label y un Button y los añade al BoxLayout
        self.label = Label(text='Presiona el botón')
        button = Button(text='Púlsame')
        button.bind(on_press=self.on_button_press)  # Enlaza el evento on_press a la función

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Cambia el texto del label
        self.label.text = '¡Botón presionado!'

if __name__ == '__main__':
    SimpleApp().run()
