from fsm import TocMachine

def create_machine():
    machine = TocMachine(
    states=["user", "menu", "roger", "roger_image","roger_video", "roger_video1", "roger_video5" , "roger_bad" ],
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
            "dest": "roger",
            "conditions": "is_going_to_roger",
        },
        {
            "trigger": "advance",
            "source": "roger",
            "dest": "roger_video",
            "conditions": "is_going_to_roger_video",
        },
        {
            "trigger": "advance",
            "source": "roger",
            "dest": "roger_image",
            "conditions": "is_going_to_roger_image",
        },
        {
            "trigger": "advance",
            "source": "roger_image",
            "dest": "roger_image",
            "conditions": "is_going_to_roger_image",
        },
        {
            "trigger": "advance",
            "source": "roger_video",
            "dest": "roger_video1",
            "conditions": "is_going_to_roger_video1",
        },
        {
            "trigger": "advance",
            "source": "roger_video",
            "dest": "roger_video5",
            "conditions": "is_going_to_roger_video5",
        },
        {
            "trigger": "advance",
            "source": "roger_video",
            "dest": "roger_bad",
            "conditions": "is_going_to_roger_bad",
        },
        {
            "trigger": "advance",
            "source": ["roger_image" , "roger_video1", "roger_video5" , "roger_bad"],
            "dest": "menu",
            "conditions": "is_going_to_menu",
        }
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
    )

    return machine
