# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/CrewAccountController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import SystemMessages as SystemMessages
from gui.shared.gui_items.processors.tankman import TankmanAutoReturn as TankmanAutoReturn
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils import decorators as decorators
from skeletons.gui.game_control import IGameController as IGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class CrewAccountController(IGameController):
    __itemsCache: Any
    __hangarSpace: Any
    __inventory: Any
    tankmanIdxSkillsUnlockAnimation: Any
    tankmanLearnedSkillsAnimanion: Any
    tankmanVeteranAnimanion: Any
    _conversionResults: Any
    autoReturnCrewData: Any
    def __init__(self, inventory):
        ...
    def getAutoReturnCrewData(self, vehicleIntCD):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def setAutoReturnCrewData(self, vehicleIntCD, skipTmanInvIDs):
        ...
    def clearTankmanAnimanions(self, tankmaninvID):
        ...
    def getTankmanVeteranAnimanion(self, tankmaninvID):
        ...
    def setTankmanVeteranAnimanionPlayed(self, tankmaninvID):
        ...
    def setLearnedSkillsAnimanion(self, tankmaninvID, learnedSkills):
        ...
    def hasLearnedSkillAnimation(self, tankmaninvID, skillName):
        ...
    def indexSkillsUnlockAnimation(self, tankmaninvID):
        ...
    def setConversionResults(self, resultsDict):
        ...
    def getSkillsCrewBooksConversion(self):
        ...
    def getSkillsCrewBoostersReplacement(self):
        ...
    def clear(self):
        ...
    def __onStartSynchronizeInventory(self, isFullSync, diff):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __returnCrew(self):
        ...
