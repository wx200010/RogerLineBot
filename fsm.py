from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_end(self, event):
        text = event.message.text
        return text.lower() == "end"

    def on_enter_menu(self, event):
        print("I'm entering menu")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger menu")
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")

    def on_enter_end(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger end")
        self.go_back()

    def on_exit_end(self):
        print("Leaving end")
