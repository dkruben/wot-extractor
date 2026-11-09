# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileStrongholdsView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from helpers import dependency as dependency
from gui.clans.clan_helpers import getStrongholdClanCardUrl as getStrongholdClanCardUrl, isStrongholdsEnabled as isStrongholdsEnabled
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView as ClanProfileBaseView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.strongholds.web_handlers import createStrongholdsWebHandlers as createStrongholdsWebHandlers
from skeletons.gui.game_control import IBrowserController as IBrowserController

class ClanProfileStrongholdsView(ClanProfileBaseView):
    browserCtrl: Any
    __browserId: Any
    __size: Any
    _dummyMustBeShown: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def setClanDossier(self, clanDossier):
        ...
    def viewSize(self, width, height):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __showBrowser(self):
        ...
