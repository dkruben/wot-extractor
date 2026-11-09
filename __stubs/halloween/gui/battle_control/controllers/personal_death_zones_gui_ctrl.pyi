# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/personal_death_zones_gui_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
from gui.battle_control.controllers.personal_death_zones_gui_ctrl import PersonalDeathZonesGUIController as PersonalDeathZonesGUIController
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE

class HWPersonalDeathZonesGUIController(PersonalDeathZonesGUIController):
    _guiSessionProvider: Any
    _ZONE_TO_STATE: dict
    def _updateWarningNotification(self, zone, visible):
        ...
