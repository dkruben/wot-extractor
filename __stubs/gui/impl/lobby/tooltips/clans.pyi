# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/clans.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import View as View, ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.tooltips.clan_short_info_content_model import ClanShortInfoContentModel as ClanShortInfoContentModel
from gui.shared.view_helpers.emblems import ClanEmblemsHelper as ClanEmblemsHelper
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController

class ClanShortInfoTooltipContent(View, ClanEmblemsHelper):
    __webCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def onClanEmblem32x32Received(self, clanDbID, emblem):
        ...
