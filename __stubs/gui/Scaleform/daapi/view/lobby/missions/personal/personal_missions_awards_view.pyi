# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui import makeHtmlString as makeHtmlString, SystemMessages as SystemMessages
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import MainOperationAwardComposer as MainOperationAwardComposer, AddOperationAwardComposer as AddOperationAwardComposer
from gui.Scaleform.daapi.view.meta.PersonalMissionsAwardsViewMeta import PersonalMissionsAwardsViewMeta as PersonalMissionsAwardsViewMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.events_dispatcher import showPersonalMissionsChain as showPersonalMissionsChain, showPersonalMissionOperationsPage as showPersonalMissionOperationsPage
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.server_events.pm_constants import SOUNDS as SOUNDS, PERSONAL_MISSIONS_SOUND_SPACE as PERSONAL_MISSIONS_SOUND_SPACE
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME, getTypeBigIconPath as getTypeBigIconPath
from gui.shared.gui_items.processors import quests as quests
from gui.shared.utils import decorators as decorators
from nations import Alliances as Alliances, ALLIANCES_TAGS_ORDER as ALLIANCES_TAGS_ORDER
from personal_missions import PM_BRANCH as PM_BRANCH
from shared_utils import findFirst as findFirst
_FRAME_NAME: tuple
_TOKEN_SLOTS: dict

class PersonalMissionsAwardsView(LobbySubView, PersonalMissionsAwardsViewMeta, PersonalMissionsNavigation):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SOUND_SPACE
    __mainAwardsFormatter: Any
    __addAwardsFormatter: Any
    def __init__(self, ctx):
        ...
    def showVehiclePreview(self):
        ...
    def refresh(self):
        ...
    def closeView(self):
        ...
    def changeOperation(self, operationID):
        ...
    def showMissionByVehicleType(self, vehicleType):
        ...
    # decorador original: @decorators.adisp_process(...)
    def buyMissionsByVehicleType(self, vehicleType):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getAwardsVO(self):
        ...
    def __onQuestsUpdated(self, *args):
        ...
    def __getVehicleAward(self):
        ...
    def __getVehicleAwardVO(self):
        ...
    def __getVehiclePartSlot(self, tokenType, iconSource, isCollected, canUnlock, unlockCost):
        ...
    def __getAdditionalAwards(self):
        ...
    def __getMainAwards(self):
        ...
    def __updateHeader(self):
        ...
