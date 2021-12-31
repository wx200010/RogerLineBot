from fsm import TocMachine

def create_machine():
    machine = TocMachine(
    states=["user", "menu", "end"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "end",
            "conditions": "is_going_to_end",
        },
        {"trigger": "go_back", "source":  "end", "dest": "menu"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

    return machine
machine = create_machine()
