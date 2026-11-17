# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/formatters/invites.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasSpecifiedSubMode as hasSpecifiedSubMode
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter as PrbInviteHtmlTextFormatter
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache

class FunPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter, FunAssetPacksMixin, FunSubModesWatcher):
    __itemsCache: Any
    def canAcceptInvite(self, invite):
        ...
    def getIconPath(self, invite, pathMaker=None):
        ...
    def updateTooltips(self, invite, canAccept, message):
        ...
    def _getTitle(self, invite, kwargs=None):
        ...
    def __hasAnyVehicle(self):
        ...
    # decorador original: @hasSpecifiedSubMode(...)
    def __getDetailedModeName(self, subModeID):
        ...
