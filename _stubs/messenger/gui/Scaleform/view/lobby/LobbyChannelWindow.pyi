# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/LobbyChannelWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE as DATA_TYPE, TARGET_ID as TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window as stored_window
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.shared.formatters import text_styles as text_styles, icons as icons
from helpers import i18n as i18n
from messenger.ext.channel_num_gen import getClientID4Prebattle as getClientID4Prebattle
from messenger.gui.Scaleform.data.MembersDataProvider import MembersDataProvider as MembersDataProvider
from messenger.gui.Scaleform.meta.LobbyChannelWindowMeta import LobbyChannelWindowMeta as LobbyChannelWindowMeta
from messenger.gui.Scaleform.view.lobby import antispam_message as antispam_message
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE

# decorador original: @stored_window(...)
class LobbyChannelWindow(LobbyChannelWindowMeta):
    def onWarningClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...

def _tryToSetTrusted(window, storedData):
    ...
