# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/filters/carousel_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
import BattleReplay as BattleReplay
import constants as constants
import nations as nations
from account_helpers.AccountSettings import AccountSettings as AccountSettings, CAROUSEL_FILTER_1 as CAROUSEL_FILTER_1, CAROUSEL_FILTER_2 as CAROUSEL_FILTER_2, CAROUSEL_FILTER_3 as CAROUSEL_FILTER_3, CAROUSEL_FILTER_CLIENT_1 as CAROUSEL_FILTER_CLIENT_1
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.shared.utils import makeSearchableString as makeSearchableString
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria
from gui.shared.gui_items.Vehicle import VEHICLE_ROLES_LABELS as VEHICLE_ROLES_LABELS, VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from typing import Dict as Dict, Union as Union

class FILTER_KEYS(object):
    ELITE = 'elite'
    PREMIUM = 'premium'
    IGR = 'igr'
    RENTED = 'rented'
    CLAN_RENTED = 'clanRented'
    BONUS = 'bonus'
    FAVORITE = 'favorite'
    CRYSTALS = 'crystals'
    SEARCH_NAME_VEHICLE = 'searchNameVehicle'
    EVENT = 'event'
    BATTLE_ROYALE = 'battleRoyale'
    RANKED = 'ranked'
    OWN_3D_STYLE = 'own3DStyle'
    CAN_INSTALL_ATTACHMENTS = 'canInstallAttachments'

class _CarouselFilter(object):
    _filters: Any
    _serverSections: Any
    _clientSections: Any
    _criteriesGroups: Any
    _disabledUpdateCriteries: Any
    _filterDefaults: Any
    def __init__(self):
        ...
    @property
    def criteria(self):
        ...
    @property
    def filterDefaults(self):
        ...
    def setDisabledUpdateCriteries(self, disabled):
        ...
    def apply(self, vehicle):
        ...
    def getFilters(self, keys=None):
        ...
    def get(self, key):
        ...
    def isDefault(self, keys=None):
        ...
    def reset(self, keys=None, exceptions=None, save=True):
        ...
    def switch(self, key, save=True):
        ...
    def clear(self, save=True):
        ...
    def update(self, params, save=True):
        ...
    def save(self):
        ...
    def load(self):
        ...
    def _updateCriteriesGroups(self):
        ...

class CriteriesGroup(object):
    _criteria: Any
    def __init__(self):
        ...
    @property
    def criteria(self):
        ...
    def apply(self, vehicle):
        ...
    def update(self, filters):
        ...
    @staticmethod
    def isApplicableFor(vehicle):
        ...

class CarouselFilter(_CarouselFilter):
    settingsCore: Any
    _serverSections: Any
    _clientSections: Any
    _filters: Any
    _criteriesGroups: Any
    def __init__(self):
        ...
    def save(self):
        ...
    def load(self):
        ...
    def switch(self, key, save=True):
        ...
    def _setCriteriaGroups(self):
        ...
    def _getFromServerStorage(self, defaultFilters):
        ...
    def _saveToServer(self):
        ...
    def __getCurrentVehicleClasses(self, updateDict):
        ...
    @staticmethod
    def __resetRoles():
        ...

class SessionCarouselFilter(_CarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    _filters: Any
    _filterDefaults: Any
    def __init__(self, criteries=None):
        ...
    @property
    def filterDefaults(self):
        ...
    def load(self):
        ...
    def save(self):
        ...
    def isDefault(self, keys=None):
        ...
    def reset(self, keys=None, exceptions=None, save=True):
        ...

class BasicCriteriesGroup(CriteriesGroup):
    _criteria: Any
    @staticmethod
    def isApplicableFor(vehicle):
        ...
    def update(self, filters):
        ...
    def _setNationsCriteria(self, filters):
        ...
    def _setClassesCriteria(self, filters):
        ...
    def _setLevelsCriteria(self, filters):
        ...
    def _setEliteAndPremiumCriteria(self, filters):
        ...
    def _setRentedCriteria(self, filters):
        ...
    def _setIGRCriteria(self, filters):
        ...
    def _setXPBonusCriteria(self, filters):
        ...
    def _setFavoriteVehicleCriteria(self, filters):
        ...
    def _setEarnCrystalsCriteria(self, filters):
        ...
    def _setVehicleNameCriteria(self, filters):
        ...

class RoleCriteriesGroup(BasicCriteriesGroup):
    _criteria: Any
    def update(self, filters):
        ...
    def _setRolesCriteria(self, filters):
        ...

class EventCriteriesGroup(CriteriesGroup):
    _criteria: Any
    def update(self, filters):
        ...
    @staticmethod
    def isApplicableFor(vehicle):
        ...

class CustomizationCriteriesGroup(RoleCriteriesGroup):
    _criteria: Any
    def update(self, filters):
        ...
    def _setOwn3DStyleCriteria(self, filters):
        ...
    def _setCanInstallAttachmentsCriteria(self, filters):
        ...

def _filterDict(dictionary, keys):
    ...
