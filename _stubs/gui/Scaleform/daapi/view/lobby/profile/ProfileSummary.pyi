# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSummary.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import WWISE as WWISE
from gui.Scaleform.daapi.view.AchievementsUtils import AchievementsUtils as AchievementsUtils
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils as ProfileUtils, getProfileCommonInfo as getProfileCommonInfo
from gui.Scaleform.daapi.view.meta.ProfileSummaryMeta import ProfileSummaryMeta as ProfileSummaryMeta
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers.i18n import makeString as makeString
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_control.dog_tag_composer import layoutComposer as dogTagComposer
from skeletons.gui.web import IWebController as IWebController

class ProfileSummary(ProfileSummaryMeta):
    itemsCache: Any
    _webCtrl: Any
    _isDTFlameEnabled: Any
    def __init__(self, *args):
        ...
    def setActive(self, value):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def _populate(self):
        ...
    def __dossierResyncHandler(self, *args):
        ...
    def __updateUserInfo(self):
        ...
    def _getInitData(self):
        ...
    def _dispose(self):
        ...
    def _addDogTagInfo(self, info, dogTag, playerName, clanProfile):
        ...
    def _triggerDogTagFlameSound(self, active):
        ...
