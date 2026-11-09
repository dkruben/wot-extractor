# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/gamma_wizard.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.common.settings.mixins import LayerVisibilityMixin as LayerVisibilityMixin
from gui.Scaleform.daapi.view.meta.GammaWizardViewMeta import GammaWizardViewMeta as GammaWizardViewMeta
from gui.Scaleform.locale.SETTINGS import SETTINGS as SETTINGS
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip

class GammaWizardView(LayerVisibilityMixin, GammaWizardViewMeta):
    MIN_VALUE = 0
    MAX_VALUE = 1
    DEFAULT_VALUE = 0.5
    _gammaWizard: Any
    _currentGammaValue: Any
    _changeGammaValue: Any
    _savedBackgroundAlpha: Any
    def __init__(self, ctx=None):
        ...
    def updateTexture(self, x, y, size):
        ...
    def onApply(self):
        ...
    def onChangeGamma(self, value):
        ...
    def onReset(self):
        ...
    def onClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onExternalBackgroundAlphaChange(self, event):
        ...
