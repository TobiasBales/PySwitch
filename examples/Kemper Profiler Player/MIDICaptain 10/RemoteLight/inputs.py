from pyswitch.clients.kemper.actions.looper import LOOPER_REC_PLAY_OVERDUB
from pyswitch.clients.kemper.actions.looper import LOOPER_STOP
from pyswitch.clients.kemper.actions.looper import LOOPER_ERASE
from pyswitch.clients.kemper.actions.looper import LOOPER_CANCEL
from pyswitch.clients.kemper.actions.looper import LOOPER_REVERSE
from pyswitch.clients.kemper.actions.looper import LOOPER_TRIGGER
from pyswitch.clients.kemper.actions.looper import LOOPER_HALF_SPEED
from pyswitch.clients.kemper.actions.bank_up_down import BANK_UP
from pyswitch.clients.kemper.actions.bank_up_down import BANK_DOWN
from pyswitch.clients.kemper.actions.rig_select_and_morph_state import RIG_SELECT_AND_MORPH_STATE
from pyswitch.clients.kemper.actions.tuner import TUNER_MODE
from pyswitch.clients.local.actions.pager import PagerAction
from pyswitch.colors import Colors
from pyswitch.clients.kemper import KemperEffectSlot
from pyswitch.clients.kemper.actions.effect_button import EFFECT_BUTTON
from pyswitch.clients.kemper.actions.rig_select import RIG_SELECT_DISPLAY_TARGET_RIG
from display import FOOTER_SLOT_1
from display import FOOTER_SLOT_2
from display import FOOTER_SLOT_3
from display import FOOTER_SLOT_4
from display import FOOTER_SLOT_5
from pyswitch.hardware.devices.pa_midicaptain_10 import *

_pager = PagerAction(
    pages = [
        {
            "id": 1,
            "color": Colors.DARK_GREEN,

        },
        {
            "id": 2,
            "color": Colors.DARK_PURPLE,

        },

    ]
)

def rig_name(action, bank, rig):
    return f"{bank + 1}-{rig + 1}"

Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_1,
    },
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2,
    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER,
    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON,
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_1,
        "actions": [
            EFFECT_BUTTON(
                1,
                enable_callback = _pager.enable_callback
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [
            EFFECT_BUTTON(
                2,
                enable_callback = _pager.enable_callback,
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [
            EFFECT_BUTTON(
                3,
                enable_callback = _pager.enable_callback
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [
            EFFECT_BUTTON(
                4,
                enable_callback = _pager.enable_callback
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actionsHold": [
            BANK_UP(),
        ],
        "actions": [
            _pager,
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actions": [
            RIG_SELECT_AND_MORPH_STATE(
                rig = 1,
                id = 1,
                text_callback = rig_name,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_1,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG
            ),
            LOOPER_REC_PLAY_OVERDUB(
                id = 2,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_1,
                text = "Rec"
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [
            RIG_SELECT_AND_MORPH_STATE(
                rig = 2,
                id = 1,
                text_callback = rig_name,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_2,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG
            ),
            LOOPER_STOP(
                id = 2,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_2,
                text = "Stp"
            ),
        ],
        "actionsHold": [
            LOOPER_ERASE(
                text = "Era",
                id = 2,
                enable_callback = _pager.enable_callback
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [
            RIG_SELECT_AND_MORPH_STATE(
                rig = 3,
                id = 1,
                text_callback = rig_name,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_3,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG
            ),
            LOOPER_TRIGGER(
                id = 2,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_5,
                text = "Trg"
            ),
        ],
        "actionsHold": [
            LOOPER_CANCEL(
                id = 2,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_4,
                text = "Und"
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actionsHold": [
            TUNER_MODE(
                text = 'Tuner'
            ),

        ],
        "actions": [
            RIG_SELECT_AND_MORPH_STATE(
                rig = 4,
                id = 1,
                text_callback = rig_name,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_4,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG
            ),
            LOOPER_REVERSE(
                id = 2,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_3,
                text = "Rev"
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [
            BANK_DOWN(
                text = 'Bank dn'
            ),
        ],
        "actions": [
            RIG_SELECT_AND_MORPH_STATE(
                rig = 5,
                id = 1,
                text_callback = rig_name,
                enable_callback = _pager.enable_callback,
                display = FOOTER_SLOT_5,
                display_mode = RIG_SELECT_DISPLAY_TARGET_RIG
            ),
            LOOPER_HALF_SPEED(
                text = 'Spd',
                id = 2,
                enable_callback = _pager.enable_callback
            ),
        ],
    },
]
