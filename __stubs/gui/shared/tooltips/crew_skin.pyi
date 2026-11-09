# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/crew_skin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.impl.gen import R as R
from gui.impl import backport as backport
from helpers import dependency as dependency
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from gui.shared.gui_items.Tankman import getCrewSkinIconBig as getCrewSkinIconBig
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName, Rarity as Rarity
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from items.components.crew_skins_constants import TANKMAN_SEX as TANKMAN_SEX
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_MAX_USERS_DISPLAYED = 10

class CrewSkinTooltipDataBlock(BlocksTooltipData):
    lobbyContext: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def __stripUnsupportedFlashTags(text):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _skinUsersRoleAndVehicleText(fstring, item, itemsCache=None):
    ...
def _longStringListEllipsisCutoff(fstring, strings, allowedLen):
    ...
