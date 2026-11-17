# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/managers/TextManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.framework.entities.abstract.TextManagerMeta import TextManagerMeta as TextManagerMeta
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES as _TMS
from gui.shared.formatters import text_styles as text_styles

class TextManager(TextManagerMeta):
    __styles: Any
    def __init__(self):
        ...
    def getTextStyle(self, style):
        ...
    def _dispose(self):
        ...

class TextIcons(object):
    CHECKMARK_ICON = 'checkmark'
    NUT_ICON = 'nut'
    PERCENT_ICON = 'percent'
    ALERT_ICON = 'alert'
    INFO_ICON = 'info'
    PREMIUM_IGR_SMALL = 'premiumIgrSmall'
    PREMIUM_IGR_BIG = 'premiumIgrBig'
    ORDER_IN_PROGRESS_ICON = 'order_in_progress'
    CLOCK_ICON = 'clock'
    NOT_AVAILABLE = 'notAvailable'
    LEVEL_5 = 'level5'
    LEVEL_10 = 'level10'
    SWORDS = 'swords'
    HUMANS = 'humans'
    CREDITS = 'credits'
    GOLD = 'gold'
    XP = 'xp'
    FREE_XP = 'freeXP'
    ARROW_BUTTON = 'arrowButton'
    NO_SEASON = 'noSeason'
    ICONS: tuple
