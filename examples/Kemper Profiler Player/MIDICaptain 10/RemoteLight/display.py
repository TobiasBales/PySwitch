from pyswitch.clients.kemper import KemperRigNameCallback
from pyswitch.clients.kemper import TunerDisplayCallback
from micropython import const
from pyswitch.colors import DEFAULT_LABEL_COLOR, Colors
from pyswitch.controller.callbacks import Callback
from pyswitch.ui.ui import DisplayElement
from pyswitch.ui.ui import DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.ui.elements import BidirectionalProtocolState
from pyswitch.clients.kemper import KemperEffectSlot
from pyswitch.clients.kemper.actions.rig_select import KemperRigSelectCallback
from pyswitch.clients.kemper import KemperMappings

_ACTION_LABEL_LAYOUT = {
	"font": "/fonts/H20.pcf",
	"backColor": DEFAULT_LABEL_COLOR,
	"stroke": 1,
}

CATEGORY_NONE = const(0)
CATEGORY_WAH = const(1)
CATEGORY_DISTORTION = const(2)
CATEGORY_COMPRESSOR = const(3)
CATEGORY_NOISE_GATE = const(4)
CATEGORY_SPACE = const(5)
CATEGORY_CHORUS = const(6)
CATEGORY_TREMOLO = const(7)
CATEGORY_PHASER = const(8)
CATEGORY_FLANGER = const(9)
CATEGORY_EQUALIZER = const(10)
CATEGORY_BOOSTER = const(11)
CATEGORY_LOOPER = const(12)
CATEGORY_PITCH = const(13)
CATEGORY_DUAL = const(14)
CATEGORY_DELAY = const(15)
CATEGORY_REVERB = const(16)

CATEGORY_COLORS = (
	DEFAULT_LABEL_COLOR,                            # None
	Colors.ORANGE,                                  # Wah
	Colors.RED,                                     # Distortion
	Colors.BLUE,                                    # Comp
	Colors.BLUE,                                    # Gate
	Colors.GREEN,                                   # Space
	Colors.BLUE,                                    # Chorus
	Colors.BLUE,                                    # Tremolo
	Colors.PURPLE,                                  # Phaser
	Colors.PURPLE,                                  # Flanger
	Colors.YELLOW,                                  # EQ
	Colors.RED,                                     # Booster
	Colors.PURPLE,                                  # Looper
	Colors.WHITE,                                   # Pitch
	Colors.GREEN,                                   # Dual
	Colors.GREEN,                                   # Delay
	Colors.GREEN,                                   # Reverb
)

CATEGORY_NAMES = (
	"-",
	"Wa",
	"Di",
	"Co",
	"Ga",
	"Sp",
	"Ch",
	"Tr",
	"Ph",
	"Fl",
	"EQ",
	"Bo",
	"Lo",
	"Pi",
	"Du",
	"De",
	"Re",
)

class EffectDisplayLabelCallback(Callback):
	def __init__(self, slot_id):
		super().__init__()
		self.mapping_state = KemperMappings.EFFECT_STATE(slot_id)
		self.mapping_type = KemperMappings.EFFECT_TYPE(slot_id)

		self.register_mapping(self.mapping_state)
		self.register_mapping(self.mapping_type)

	def update_label(self, label):
		effect_category = self.get_effect_category(self.mapping_type.value)

		if self.mapping_state.value == True:
			label.back_color = CATEGORY_COLORS[effect_category]
		elif self.mapping_state.value == False:
			label.back_color = DEFAULT_LABEL_COLOR

		label.text = CATEGORY_NAMES[effect_category]

	def get_effect_category(self, kpp_effect_type):
		if (kpp_effect_type == None):
			return CATEGORY_NONE
		elif (kpp_effect_type == 0):
			return CATEGORY_NONE
		elif (0 < kpp_effect_type and kpp_effect_type <= 10) or kpp_effect_type == 12:
			return CATEGORY_WAH
		elif kpp_effect_type == 11 or kpp_effect_type == 13:
			return CATEGORY_PITCH
		elif (14 < kpp_effect_type and kpp_effect_type <= 45):
			return CATEGORY_DISTORTION
		elif (45 < kpp_effect_type and kpp_effect_type <= 55):
			return CATEGORY_COMPRESSOR
		elif (55 < kpp_effect_type and kpp_effect_type <= 60):
			return CATEGORY_NOISE_GATE
		elif (60 < kpp_effect_type and kpp_effect_type <= 64):
			return CATEGORY_SPACE
		elif (64 < kpp_effect_type and kpp_effect_type <= 69):
			return CATEGORY_CHORUS
		elif (69 < kpp_effect_type and kpp_effect_type <= 80):
			return CATEGORY_TREMOLO
		elif (80 < kpp_effect_type and kpp_effect_type <= 88):
			return CATEGORY_PHASER
		elif (88 < kpp_effect_type and kpp_effect_type <= 95):
			return CATEGORY_FLANGER
		elif (95 < kpp_effect_type and kpp_effect_type <= 110):
			return CATEGORY_EQUALIZER
		elif (110 < kpp_effect_type and kpp_effect_type <= 120):
			return CATEGORY_BOOSTER
		elif (120 < kpp_effect_type and kpp_effect_type <= 125):
			return CATEGORY_LOOPER
		elif (125 < kpp_effect_type and kpp_effect_type <= 135):
			return CATEGORY_PITCH
		elif (135 < kpp_effect_type and kpp_effect_type <= 143):
			return CATEGORY_DUAL
		elif (143 < kpp_effect_type and kpp_effect_type <= 170):
			return CATEGORY_DELAY
		else:
			return CATEGORY_REVERB

_DISPLAY_WIDTH = const(
	240
)
_DISPLAY_HEIGHT = const(
	240
)
_FOOTER_SLOT_WIDTH = const(
	48 # _DISPLAY_WIDTH / 5
)
_EFFECT_SLOT_WIDTH = const(
	30 # _DISPLAY_WIDTH / 8
)
_SLOT_HEIGHT = const(
	40
)
_FOOTER_Y = const(
	200
)
_RIG_NAME_HEIGHT = const(
	160
)

EFFECT_SLOT_A = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(0 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(KemperEffectSlot.EFFECT_SLOT_ID_A)
)

EFFECT_SLOT_B = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(1 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_B)
)

EFFECT_SLOT_C = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(2 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_C)
)

EFFECT_SLOT_D = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(3 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_D)
)

EFFECT_SLOT_X = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(4 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_X)
)

EFFECT_SLOT_MOD = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(5 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_MOD)
)

EFFECT_SLOT_DELAY = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(6 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_DLY)
)

EFFECT_SLOT_REVERB = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(7 * _EFFECT_SLOT_WIDTH, 0, _EFFECT_SLOT_WIDTH, _SLOT_HEIGHT),
	callback = EffectDisplayLabelCallback(slot_id=KemperEffectSlot.EFFECT_SLOT_ID_REV)
)

FOOTER_SLOT_1 = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(0 * _FOOTER_SLOT_WIDTH, _FOOTER_Y, _FOOTER_SLOT_WIDTH, _SLOT_HEIGHT),
)
FOOTER_SLOT_2 = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(1 * _FOOTER_SLOT_WIDTH, _FOOTER_Y, _FOOTER_SLOT_WIDTH, _SLOT_HEIGHT),
)
FOOTER_SLOT_3 = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(2 * _FOOTER_SLOT_WIDTH, _FOOTER_Y, _FOOTER_SLOT_WIDTH, _SLOT_HEIGHT),
)
FOOTER_SLOT_4 = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(3 * _FOOTER_SLOT_WIDTH, _FOOTER_Y, _FOOTER_SLOT_WIDTH, _SLOT_HEIGHT),
)
FOOTER_SLOT_5 = DisplayLabel(
	layout = _ACTION_LABEL_LAYOUT,
	bounds = DisplayBounds(4 * _FOOTER_SLOT_WIDTH, _FOOTER_Y, _FOOTER_SLOT_WIDTH, _SLOT_HEIGHT),
)

Splashes = TunerDisplayCallback(
	splash_default = DisplayElement(
		bounds = DisplayBounds(
			x = 0,
			y = 0,
			w = _DISPLAY_WIDTH,
			h = _DISPLAY_HEIGHT
		),
		children = [
			EFFECT_SLOT_A,
			EFFECT_SLOT_B,
			EFFECT_SLOT_C,
			EFFECT_SLOT_D,
			EFFECT_SLOT_X,
			EFFECT_SLOT_MOD,
			EFFECT_SLOT_DELAY,
			EFFECT_SLOT_REVERB,
			FOOTER_SLOT_1,
			FOOTER_SLOT_2,
			FOOTER_SLOT_3,
			FOOTER_SLOT_4,
			FOOTER_SLOT_5,
			DisplayLabel(
				bounds = DisplayBounds(
					x = 0,
					y = _SLOT_HEIGHT,
					w = _DISPLAY_WIDTH,
					h = _RIG_NAME_HEIGHT
				),
				layout = {
					"font": "/fonts/PTSans-NarrowBold-40.pcf",
					"lineSpacing": 0.8,
					"maxTextWidth": 220,
					"text": KemperRigNameCallback.DEFAULT_TEXT,

				},
				callback = KemperRigNameCallback()
			),
			BidirectionalProtocolState(
				DisplayBounds(
					x = 0,
					y = _SLOT_HEIGHT,
					w = _DISPLAY_WIDTH,
					h = _RIG_NAME_HEIGHT
				)
			),
		]
	)
)
