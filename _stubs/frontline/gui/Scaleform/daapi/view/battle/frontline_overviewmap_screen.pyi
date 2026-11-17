# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_overviewmap_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME, _MISSION_SECTOR_ID_MAPPING as _MISSION_SECTOR_ID_MAPPING
from debug_utils import LOG_ERROR as LOG_ERROR
from frontline.gui.Scaleform.daapi.view.meta.FrontlineOverviewMapScreenMeta import FrontlineOverviewMapScreenMeta as FrontlineOverviewMapScreenMeta
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.Scaleform.locale.READABLE_KEY_NAMES import READABLE_KEY_NAMES as READABLE_KEY_NAMES
from helpers import dependency as dependency
from helpers import i18n as i18n
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
EpicOverviewMapScreenVO: Any

class OverviewMapScreen(FrontlineOverviewMapScreenMeta):
    sessionProvider: Any
    def start(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setKeyBindings(self):
        ...
    def __getCurrentZoneNamePerLane(self, lane):
        ...
    def __onSectorBaseCaptured(self, id_, isPlayerTeam):
        ...
    def __updateLaneButtons(self):
        ...
