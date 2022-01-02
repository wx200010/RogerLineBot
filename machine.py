from fsm import TocMachine

def create_machine():
    machine = TocMachine(
    states=["user", "menu", "show_fsm" , "roger", "roger_image","roger_database" , "roger_database_add_url" , "roger_database_del_url" ,
            "roger_database_add_imgur_url" , "roger_database_del_imgur_url" ,  "roger_video", "roger_video1", "roger_video5" , "roger_bad" ],
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
            "dest": "show_fsm",
            "conditions": "is_going_to_show_fsm",
        },
        {
            "trigger": "advance",
            "source": "show_fsm",
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
            "dest": "menu",
            "conditions": "is_going_to_menu",
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
            "source": "roger",
            "dest": "roger_database",
            "conditions": "is_going_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger_database",
            "conditions": "is_going_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger_database_add_url",
            "conditions": "is_going_to_roger_database_add_url",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger_database_del_url",
            "conditions": "is_going_to_roger_database_del_url",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger_database_add_imgur_url",
            "conditions": "is_going_to_roger_database_add_imgur_url",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger_database_del_imgur_url",
            "conditions": "is_going_to_roger_database_del_imgur_url",
        },
        {
            "trigger": "advance",
            "source": "roger_database_add_url",
            "dest": "roger_database",
            "conditions": "from_add_url_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database_del_url",
            "dest": "roger_database",
            "conditions": "from_del_url_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database_add_imgur_url",
            "dest": "roger_database",
            "conditions": "from_add_imgur_url_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database_del_imgur_url",
            "dest": "roger_database",
            "conditions": "from_del_imgur_url_to_roger_database",
        },
        {
            "trigger": "advance",
            "source": "roger_database",
            "dest": "roger",
            "conditions": "is_going_to_roger",
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
            "dest": "roger",
            "conditions": "is_going_to_roger",
        }
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
    )

    return machine
