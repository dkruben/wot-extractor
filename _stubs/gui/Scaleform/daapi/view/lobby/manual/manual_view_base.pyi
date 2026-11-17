# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/manual_view_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.framework.entities.View import View as View
from helpers import dependency as dependency
from skeletons.gui.game_control import IManualController as IManualController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
_logger: Any

class ManualViewBase(View):
    lobbyContext: Any
    manualController: Any
    SOUND_SPACE = 'manual'
    SOUND_STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_MENU_GUIDE = 'STATE_hangar_place_menu_guide'
    BC_HANGAR_MUSIC_GUIDE_ENTER_SOUND_ID = 'bc_hangar_music_guide_enter'
    BC_HANGAR_MUSIC_GUIDE_EXIT_SOUND_ID = 'bc_hangar_music_guide_exit'
    _COMMON_SOUND_SPACE: Any
    _ctx: Any
    chaptersUIData: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def _close(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
