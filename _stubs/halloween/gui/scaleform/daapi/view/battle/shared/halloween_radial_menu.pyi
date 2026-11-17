# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/shared/halloween_radial_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, MarkerType as MarkerType, DefaultMarkerSubType as DefaultMarkerSubType, INVALID_MARKER_SUBTYPE as INVALID_MARKER_SUBTYPE
from gui.Scaleform.genConsts.RADIAL_MENU_CONSTS import RADIAL_MENU_CONSTS as RADIAL_MENU_CONSTS
from gui.Scaleform.daapi.view.battle.shared.radial_menu import Shortcut as Shortcut, _MARKERS_TYPE_TO_SUBTYPE_MAP as _MARKERS_TYPE_TO_SUBTYPE_MAP, RadialMenu as RadialMenu
from gui.Scaleform.locale.INGAME_HELP import INGAME_HELP as INGAME_HELP
from halloween.gui.scaleform.genConsts.HW_RADIAL_MENU_CONSTS import HW_RADIAL_MENU_CONSTS as HW_RADIAL_MENU_CONSTS
REGULAR_BOTTOM_STATIC_SHORTCUTS: tuple
REGULAR_UPPER_STATIC_SHORTCUTS: tuple
_CAN_CANCEL_REPLY_SHORTCUT: Any

class HalloweenRadialMenu(RadialMenu):
    _CMD_CHAT_SHORTCUT_CONTEXT_COMMAND: tuple
    _CMD_CHAT_SHORTCUT_CONTEXT_COMMIT: tuple
    _ALL_TARGET_STATES: Any
    def _initShortCuts(self):
        ...
    def _getCanReplayShortcut(self, shortcut, canReplyAction):
        ...
    def _getCanCancelReplyShortcut(self):
        ...
