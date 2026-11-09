# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/crew_bundle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE, formatters as formatters
from gui.shared.tooltips.common import BlocksTooltipData as BlocksTooltipData
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from soft_exception import SoftException as SoftException
_R_TOOLTIPS_TEXT = R.strings.tooltips.crewBundle
_R_SKILLS_IMAGES = R.images.gui.maps.icons.tankmen.skills.big
_BUNDLE_PRESETS: dict
_BONUS_PRESETS: dict

class _Bonuses(CONST_CONTAINER):
    ANY_ADDITIONAL_SKILL = 'anyAdditionalSkill'
    SAME_BLOOD_ZERO_SKILL = 'sameBloodZeroSkill'

# base nao representavel no stub: namedtuple(...)
class _BonusPreset:
    def __new__(cls, imageRPath, textRPath, top=0, left=15, bottom=0, right=30):
        ...

class CrewBundleTooltipData(BlocksTooltipData):
    def __init__(self, context):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...
    @staticmethod
    def __packHeaderBlock(bundleName):
        ...
    @staticmethod
    def __packHowToGetBlock(bundleName):
        ...
    def __packInfoBlock(self, bonuses):
        ...
    @staticmethod
    def __getBonus(preset):
        ...
