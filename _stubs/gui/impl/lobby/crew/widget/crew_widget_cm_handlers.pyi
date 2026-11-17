# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/widget/crew_widget_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import SystemMessages as SystemMessages
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.impl.dialogs import dialogs as dialogs
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.gui_items.processors.tankman import TankmanUnload as TankmanUnload
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
CM_RETRAIN_COLOR = 13347959

class CREW(object):
    PERSONAL_FILE = 'personalFile'
    RETRAIN = 'retrain'
    CHANGE_CREW_MEMBER = 'changeCrewMember'
    SEND_TO_BARRACKS = 'sendToToBarracks'
    DISMISS = 'dismiss'
    QUICK_TRAINING = 'quickTraining'
    CHANGE_SPECIALIZATION = 'changeSpecialization'

class CrewContextMenuHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache: Any
    _slotIdx: Any
    _tankmanID: Any
    _previousViewID: Any
    _tankman: Any
    _vehicle: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def showPersonalFile(self):
        ...
    def showQuickTraining(self):
        ...
    def retrain(self):
        ...
    def changeCrewMember(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def sendToToBarracks(self):
        ...
    def dismiss(self):
        ...
    def changeSpecialization(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
