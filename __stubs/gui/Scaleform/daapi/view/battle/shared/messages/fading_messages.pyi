# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/fading_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from soft_exception import SoftException as SoftException
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.meta.BattleMessageListMeta import BattleMessageListMeta as BattleMessageListMeta
from gui.Scaleform.genConsts.BATTLE_MESSAGES_CONSTS import BATTLE_MESSAGES_CONSTS as BATTLE_MESSAGES_CONSTS
from gui.app_loader import sf_battle as sf_battle
from gui.doc_loaders import messages_panel_reader as messages_panel_reader
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_MESSAGES_SETTINGS_PATH = 'gui/{}'
_EXTRA_COLOR_FORMAT = '<font color="#{0:02X}{1:02X}{2:02X}">{3:>s}</font>'
_COLOR_TO_METHOD: dict

class FadingMessages(BattleMessageListMeta):
    sessionProvider: Any
    settingsCore: Any
    objs: dict
    __name: Any
    __settingsFilePath: Any
    __isColorBlind: Any
    _messages: Any
    __styles: Any
    def __init__(self, name, mFile):
        ...
    def __del__(self):
        ...
    def setSettingFile(self, mFile):
        ...
    @property
    def messages(self):
        ...
    # decorador original: @sf_battle
    def app(self):
        ...
    def clear(self):
        ...
    def showMessage(self, key, args=None, extra=None, postfix=''):
        ...
    def getStyles(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def __formatEntitiesEx(self, args, extra=None):
        ...
    def __doShowMessage(self, key, args=None, extra=None):
        ...
    def __onSettingsChanged(self, diff):
        ...
