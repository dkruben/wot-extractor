# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/dog_tags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from dog_tags_common.components_config import componentConfigAdapter as cca
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from dog_tags_common.number_formatter import formatComponentValue as formatComponentValue
from dog_tags_common.player_dog_tag import PlayerDogTag as PlayerDogTag
from gui.dog_tag_composer import dogTagComposer as dogTagComposer, AssetSize as AssetSize
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from helpers import getLanguageCode as getLanguageCode, dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class DogTagInfoTooltip(BlocksTooltipData):
    itemsCache: Any
    __titlePadding: Any
    __levelPadding: Any
    __imagePaddingTop = 13
    __imagePaddingBottom = 5
    __imageNegativeHeight = -120
    __descriptionPadding: Any
    def __init__(self, context):
        ...
    def _packBlocks(self, compId, userID=None):
        ...
