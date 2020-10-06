# Changes screen size (delete before publish)
from kivy.config import Config

Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton

import firebase


class AllTodoScreen(Screen):
    pass


class NewTodoScreen(Screen):
    pass


class MainApp(MDApp):

    def on_start(self):
        # set color theme
        self.theme_cls.primary_palette = 'Blue'

        # gets tasks from database when loaded
        self.load_tasks()

    def load_tasks(self):
        # retrieve todo list and clears it
        todo_list = self.root.ids.all_todo_screen.ids.all_todo_list
        todo_list.clear_widgets()
        # loads existing tasks from firebase
        todos = firebase.db.child("todos").get()
        if not todos.each() == None:
            for todo in todos.each():
                todo_list.add_widget(OneLineListItem(text=todo.val()))

    def new_task(self):
        self.change_screen("new_todo_screen", "left")

    def add_task(self, task):
        firebase.db.child("todos").child(task.upper()).set(task.upper())
        self.root.ids.new_todo_screen.ids.new_task.text = ""
        self.load_tasks()
        self.change_screen("all_todo_screen", "right")

    dialog = None

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Er du sikker på, at du vil slette?",
                size_hint_x=".55",
                buttons=[
                    MDFlatButton(
                        text="NEJ", text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDRaisedButton(
                        text="SLET", on_release=self.delete_task_post
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, x):
        self.dialog.dismiss()

    delete_text = ""

    def delete_task_pre(self, text):
        self.delete_text = text
        self.show_alert_dialog()

    def delete_task_post(self, x):
        self.delete_task()
        self.close_dialog(x)

    def delete_task(self):
        firebase.db.child("todos").child(self.delete_text).remove()
        self.load_tasks()

    def change_screen(self, screen_name, direction):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name


MainApp().run()
