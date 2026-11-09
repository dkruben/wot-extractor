# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_operation_awards_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.Scaleform.daapi.view.meta.PersonalMissionsOperationAwardsScreenMeta import PersonalMissionsOperationAwardsScreenMeta as PersonalMissionsOperationAwardsScreenMeta
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, LABEL_ALIGN as LABEL_ALIGN
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.server_events.pm_constants import SOUNDS as SOUNDS, PERSONAL_MISSIONS_SOUND_SPACE as PERSONAL_MISSIONS_SOUND_SPACE
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from gui.server_events import finders as finders
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache

class PersonalMissionsOperationAwardsScreen(PersonalMissionsOperationAwardsScreenMeta):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SOUND_SPACE
    _eventsCache: Any
    __branch: Any
    __operationID: Any
    __questsIds: Any
    __vehicleAward: Any
    def __init__(self, ctx):
        ...
    def onPlaySound(self, soundType):
        ...
    def onCloseWindow(self):
        ...
    def _populate(self):
        ...
    def __getHeader(self):
        ...
    def __getVehicleData(self):
        ...
    def __packBadges(self, badges):
        ...
    def __getBonuses(self, tokensQuestsIds):
        ...
