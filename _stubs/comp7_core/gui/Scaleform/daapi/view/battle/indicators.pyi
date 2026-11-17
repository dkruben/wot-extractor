# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/indicators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7_core.gui.Scaleform.daapi.view.meta.Comp7SixthSenseIndicatorMeta import Comp7SixthSenseIndicatorMeta as Comp7SixthSenseIndicatorMeta
from constants import DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from helpers.time_utils import MS_IN_SECOND as MS_IN_SECOND
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.genConsts.COMP7_CONSTS import COMP7_CONSTS as COMP7_CONSTS
from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator as SixthSenseIndicator

class Comp7SixthSenseIndicator(Comp7SixthSenseIndicatorMeta, SixthSenseIndicator):
    def getIndicatorTogglesByType(self):
        ...
    def __toggleFlight(self, isVisible, _):
        ...
    def __isFlightEnabled(self):
        ...
    def __toggleIlluminationFlare(self, isVisible, _):
        ...
    def __isIlluminationFlareEnabled(self):
        ...
