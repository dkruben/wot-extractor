# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileGlobalMapInfoView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.clans.profile.clan_statistics_vos import FortGlobalMapStatistics as FortGlobalMapStatistics
from gui.Scaleform.daapi.view.meta.ClanProfileGlobalMapInfoViewMeta import ClanProfileGlobalMapInfoViewMeta as ClanProfileGlobalMapInfoViewMeta
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES as CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from helpers import time_utils as time_utils
from helpers.i18n import makeString as _ms

class ClanProfileGlobalMapInfoView(ClanProfileGlobalMapInfoViewMeta):
    _clanDossier: Any
    _proxy: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def setProxy(self, proxy, clanDossier):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
