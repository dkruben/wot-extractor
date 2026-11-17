# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import EXTRA_CHAPTERS_VIDEO_SHOWN as EXTRA_CHAPTERS_VIDEO_SHOWN, LAST_BATTLE_PASS_EXTRA_CHAPTER_SEEN as LAST_BATTLE_PASS_EXTRA_CHAPTER_SEEN, UMG_BATTLE_PASS_EXTRA_CHAPTER_SEEN as UMG_BATTLE_PASS_EXTRA_CHAPTER_SEEN, LAST_BATTLE_PASS_HOLIDAY_CHAPTER_SEEN as LAST_BATTLE_PASS_HOLIDAY_CHAPTER_SEEN
from account_helpers.settings_core.settings_constants import BattlePassStorageKeys as BattlePassStorageKeys
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.battle_pass.battle_pass_helpers import isExtraIntroVideoEnabled as isExtraIntroVideoEnabled, isIntroVideoEnabled as isIntroVideoEnabled, isIntroEnabled as isIntroEnabled
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

# decorador original: @dependency.replace_none_kwargs(...)
def getActualBattlePassIDs(layoutID=..., chapterID=0, battlePass=None):
    ...
def showOverlayVideo(url, callbackOnClose=None, callbackOnLoad=None):
    ...
def showIntroView(callback=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isIntroVideoShown(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setIntroVideoShown(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isExtraVideoShown(battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setExtraVideoShown(battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isIntroShown(settingsCore=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setIntroShown(settingsCore=None):
    ...
def isExtraChapterSeen():
    ...
def setExtraChapterSeen():
    ...
def isUmgExtraChapterSeen():
    ...
def setUmgExtraChapterSeen():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isExtraContentResolved(battlePass=None):
    ...
def isHolidayChapterSeen():
    ...
def setHolidayChapterSeen():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getExtraChapterID(battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCurrentChapterID(battlePass=None):
    ...
