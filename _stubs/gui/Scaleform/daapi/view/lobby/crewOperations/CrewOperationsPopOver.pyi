# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/crewOperations/CrewOperationsPopOver.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.CrewOperationsPopOverMeta import CrewOperationsPopOverMeta as CrewOperationsPopOverMeta
from gui.Scaleform.locale.CREW_OPERATIONS import CREW_OPERATIONS as CREW_OPERATIONS
from gui.impl.dialogs.dialogs import showRetrainMassiveDialog as showRetrainMassiveDialog, showRetrainSingleDialog as showRetrainSingleDialog
from gui.prb_control import prb_getters as prb_getters
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, getLowEfficiencyCrew as getLowEfficiencyCrew
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.gui_items.processors.tankman import TankmanAutoReturn as TankmanAutoReturn, TankmanReturn as TankmanReturn
from gui.shared.gui_items.processors.vehicle import VehicleAutoReturnProcessor as VehicleAutoReturnProcessor
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from helpers import i18n as i18n
from skeletons.gui.shared import IItemsCache as IItemsCache
OPERATION_RETRAIN = 'retrain'
OPERATION_RETURN = 'return'
OPERATION_DROP_IN_BARRACK = 'dropInBarrack'

class CrewOperationsPopOver(CrewOperationsPopOverMeta):
    itemsCache: Any
    __slots__: tuple
    _ctxData: Any
    def __init__(self, ctx):
        ...
    def _populate(self):
        ...
    def onWindowClose(self):
        ...
    def _destroy(self):
        ...
    def _dispose(self):
        ...
    def invokeOperation(self, operationName):
        ...
    def onToggleClick(self, operationName):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __autoReturnToggleSwitch(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __processReturnCrew(self):
        ...
    def onInventoryUpdate(self, invDiff):
        ...
    def __update(self):
        ...
    def __getRetrainOperationData(self, vehicle):
        ...
    def __getReturnOperationData(self, vehicle):
        ...
    def __getDropInBarrackOperationData(self, vehicle):
        ...
    def __isTopCrewForCurrentVehicle(self, vehicle):
        ...
    def __isNoCrew(self, crew):
        ...
    def __isNotEnoughSpaceInBarrack(self, crew):
        ...
    def __getInitCrewOperationObject(self, operationId, errorId=None, warningId='', operationAvailable=False):
        ...
    def __unitMgrOnUnitLeft(self, _, __):
        ...
    @staticmethod
    def __unloadCrew():
        ...
