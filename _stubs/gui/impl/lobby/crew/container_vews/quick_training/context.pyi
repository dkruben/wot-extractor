# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.lobby.container_views.base.context import TankmanContext as TankmanContext
from gui.impl.lobby.crew.crew_helpers.quick_training_selection_data import QuickTrainingSelectionData as QuickTrainingSelectionData
from gui.impl.lobby.crew.crew_helpers.skill_formatters import SkillLvlFormatter as SkillLvlFormatter
from gui.impl.lobby.crew.crew_helpers.skill_helpers import quickEarnTmanSkills as quickEarnTmanSkills
from gui.impl.lobby.crew.crew_helpers.stepper_calculator import FreeXpStepperCalculator as FreeXpStepperCalculator
from gui.impl.lobby.crew.utils import TRAINING_TIPS as TRAINING_TIPS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT, NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.gui_items.crew_book import sortItems as sortItems
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from items.tankmen import MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import List as List, Tuple as Tuple
from gui.shared.gui_items.crew_book import CrewBook as CrewBook
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
CREW_TIPS: dict

class TankmanAutoselector(object):
    selectedIdx = NO_SLOT
    selectedTman = None
    selectedTmanWithIssues = None
    selectedTmanWithPerkLimit = None
    def clear(self):
        ...
    def validateTankman(self, tankmanId, idx, isMaxSkillXp, isUntrained, hasMaxSkillsEfficiency):
        ...
    def getSelectedTankman(self):
        ...

class QuickTrainingViewContext(TankmanContext):
    lobbyContext: Any
    _slotIdx: Any
    _vehicleID: Any
    _vehicle: Any
    _crewBooks: Any
    _isFullCrew: Any
    _isAllCrewMaxTrained: Any
    _hasCrewMaxedTman: Any
    _hasCrewUntrainedTman: Any
    _hasCrewLowTrainedTman: Any
    _willAnyTmanBeMaxed: Any
    _willAllTmenGainMaxXp: Any
    _willAllTmenBeMaxed: Any
    _alreadyMaxedTankmanName: Any
    _willBeMaxedTankmanName: Any
    _possibleCrewSkills: Any
    _possibleCrewSkillEfficiencis: Any
    _stepper: Any
    _selectionData: Any
    _autoselector: Any
    def __init__(self, vehicleID, tankmanID):
        ...
    @property
    def vehicleID(self):
        ...
    @property
    def isMentoringLicenseEnabled(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def crew(self):
        ...
    @property
    def crewBooks(self):
        ...
    @property
    def slotIdx(self):
        ...
    @property
    def isFullCrew(self):
        ...
    @property
    def isAllCrewMaxTrained(self):
        ...
    @property
    def isCurrTmanMaxTrained(self):
        ...
    @property
    def isSingleTankman(self):
        ...
    @property
    def hasCurrTmanMaxSkillsEfficiency(self):
        ...
    @property
    def hasCrewMaxedTman(self):
        ...
    @property
    def hasCrewUntrainedTman(self):
        ...
    @property
    def hasCrewLowTrainedTman(self):
        ...
    @property
    def canCrewSelectBook(self):
        ...
    @property
    def canCrewSelectPersonalBook(self):
        ...
    @property
    def canCrewSelectFreeXp(self):
        ...
    @property
    def canCurrentTankmanUseFreeXp(self):
        ...
    @property
    def canCurrentTankmanUsePersonalBook(self):
        ...
    @property
    def canCurrentTankmanUseMorePersonalBook(self):
        ...
    @property
    def willAnyTmanBeMaxed(self):
        ...
    @property
    def willAllTmenGainMaxXp(self):
        ...
    @property
    def alreadyMaxedTankmanName(self):
        ...
    @property
    def possibleMaxedTankmanName(self):
        ...
    @property
    def stepper(self):
        ...
    @property
    def selection(self):
        ...
    @property
    def accountMaxedTankmenCount(self):
        ...
    @property
    def rewardBook(self):
        ...
    @property
    def maxPossibleXpCount(self):
        ...
    @property
    def crewTip(self):
        ...
    @property
    def postProgressionXp(self):
        ...
    @property
    def xpDefaultConversionRate(self):
        ...
    @property
    def xpDiscountConversionRate(self):
        ...
    @property
    def xpConversionDiscount(self):
        ...
    @property
    def hiddenShopItems(self):
        ...
    def update(self, tankmanID=..., slotIdx=...):
        ...
    def getAcquiringFreeXpValue(self):
        ...
    def getPossibleCrewSkillsAndEfficiencies(self):
        ...
    def updateOnFreeXpGlobalChange(self):
        ...
    def updateOnGlobalSync(self):
        ...
    def updateBooks(self):
        ...
    def updatePossibleCrewState(self):
        ...
    def __getComputableFreeXpValue(self):
        ...
    def __getCurrentVehicle(self):
        ...
    def __getCrewBooks(self):
        ...
    def __setInitialCrewProperties(self, tankmanId=...):
        ...
    def __updateWithNewTankman(self):
        ...
