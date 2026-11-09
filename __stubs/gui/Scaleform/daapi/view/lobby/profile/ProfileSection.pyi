# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSection.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from helpers import dependency as dependency, i18n as i18n
from gui.Scaleform.daapi.view.meta.ProfileSectionMeta import ProfileSectionMeta as ProfileSectionMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from stats_params import BATTLE_ROYALE_STATS_ENABLED as BATTLE_ROYALE_STATS_ENABLED
DropdownData: Any

class ProfileSection(ProfileSectionMeta):
    itemsCache: Any
    lobbyContext: Any
    __isActive: Any
    _battlesType: Any
    _userName: Any
    _userID: Any
    _databaseID: Any
    _selectedData: Any
    _data: Any
    _dossier: Any
    _battleTypeHandlers: Any
    __needUpdate: Any
    def __init__(self, *args):
        ...
    def __initHandlers(self):
        ...
    def __getData(self, battleType, obj):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def requestDossier(self, bType):
        ...
    def onSectionActivated(self):
        ...
    def onSectionDeactivated(self):
        ...
    @classmethod
    def _getTotalStatsBlock(cls, dossier):
        ...
    def __receiveDossier(self):
        ...
    def _getNecessaryStats(self, accountDossier=None):
        ...
    def _receiveFortDossier(self, accountDossier):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def setActive(self, value):
        ...
    def invokeUpdate(self):
        ...
    @property
    def isActive(self):
        ...
    def _formIconLabelInitObject(self, i18key, icon):
        ...
    @classmethod
    def _makeBattleTypesDropDown(cls, accountDossier, forVehiclesPage=False):
        ...

class BattleTypesDropDownItems(list):
    def addByKey(self, key):
        ...
    def addWithKeyAndLabel(self, key, label):
        ...
    def __addEntry(self, key, label):
        ...
