# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/recruit_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import Event as Event
import constants as constants
from gui import GUI_NATIONS as GUI_NATIONS
from gui.impl.lobby.crew.dialogs.recruit_window.recruit_dialog_utils import getSortedItems as getSortedItems
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.drop_down_item_view_model import DropDownItemViewModel as DropDownItemViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_content_view_model import RecruitContentViewModel as RecruitContentViewModel, DropDownState as DropDownState
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.vehicle_item_view_model import VehicleItemViewModel as VehicleItemViewModel
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore, capitalizeText as capitalizeText
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.skills_constants import ORDERED_ROLES as ORDERED_ROLES
from nations import INDICES as INDICES
from skeletons.gui.shared import IItemsCache as IItemsCache
NO_DATA_VALUE = '-1'
FIRST_ELEMENT = 0
_logger: Any

class RecruitContent(object):
    __slots__: tuple
    _itemsCache: Any
    __viewModel: Any
    __selectedNation: Any
    __selectedNationID: Any
    __selectedVehType: Any
    __selectedVehicle: Any
    __selectedSpecialization: Any
    onRecruitContentChanged: Any
    __isFemale: Any
    __predefinedNations: Any
    __predefinedRoles: Any
    __vehIntCD: Any
    __slotSpecialization: Any
    __isSlotChanged: Any
    def __init__(self, predefinedData, model=None):
        ...
    @property
    def viewModel(self):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def onLoading(self):
        ...
    def __fillModel(self):
        ...
    def __processPredefinedData(self, predefinedData):
        ...
    def __fillNations(self):
        ...
    def __getNationsList(self):
        ...
    def __fillVehTypes(self):
        ...
    def __getVehTypeList(self):
        ...
    def __fillVehicles(self):
        ...
    def __getVehicleList(self):
        ...
    def __fillRoles(self):
        ...
    def __getRolesList(self):
        ...
    def __updateModelAndFireCahangedEvent(self):
        ...
    def __onNationChange(self, args):
        ...
    def __onVehTypeChange(self, args):
        ...
    def __onVehicleChange(self, args):
        ...
    def __onSpecializationChange(self, args):
        ...
    def __getIdFromArgs(self, args=None):
        ...
    def __getDropDownState(self, isPredefined, isPrevSelected):
        ...
    def __updateDropDownsStates(self):
        ...
    def __updateSelectedValues(self):
        ...
    def __isSingleValue(self, lst):
        ...
    def __choosePredefined(self, predefinedList, defaultValue):
        ...
    def __getNationsCriteria(self):
        ...
    def __getClassesCriteria(self, nationID):
        ...
    def __getVehicleTypeCriteria(self, nationID, vclass):
        ...
    def __getRoleCriteria(self, nationID, vclass, typeID):
        ...
