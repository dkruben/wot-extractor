# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanPersonalInvitesWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.clans.clan_helpers import ClanListener as ClanListener
from gui.clans import formatters as formatters
from gui.Scaleform.daapi.view.meta.ClanPersonalInvitesWindowMeta import ClanPersonalInvitesWindowMeta as ClanPersonalInvitesWindowMeta
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.shared.formatters import text_styles as text_styles
from helpers.i18n import makeString as _ms

class ClanPersonalInvitesWindow(ClanPersonalInvitesWindowMeta, ClanListener):
    def __init__(self, *args, **kwargs):
        ...
    def onClanEnableChanged(self, enabled):
        ...
    def onAccountClanProfileChanged(self, profile):
        ...
    def onAccountInvitesReceived(self, invites):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def onWindowClose(self):
        ...
    def _updateActualInvites(self):
        ...
