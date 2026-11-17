# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTechniquePage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import PROFILE_TECHNIQUE as PROFILE_TECHNIQUE
from gui.Scaleform.daapi.view.meta.ProfileTechniquePageMeta import ProfileTechniquePageMeta as ProfileTechniquePageMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from helpers.i18n import makeString as makeString
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.prestige.prestige_helpers import isOnboardingViewed as isOnboardingViewed, showPrestigeOnboardingWindow as showPrestigeOnboardingWindow

class ProfileTechniquePage(ProfileTechniquePageMeta):
    _battlesType: Any
    _selectedData: Any
    _selectedVehicleIntCD: Any
    def _populate(self):
        ...
    def _getInitData(self, accountDossier=None, isFallout=False):
        ...
    def _getTechniqueListVehicles(self, targetData, addVehiclesThatInHangarOnly=False):
        ...
    def _getStorageId(self):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def setIsInHangarSelected(self, value):
        ...
    def requestData(self, vehicleId):
        ...
    def updateView(self, ctx):
        ...
    def invokeUpdate(self):
        ...
    def setActive(self, value):
        ...
