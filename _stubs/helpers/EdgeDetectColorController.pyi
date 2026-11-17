# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/EdgeDetectColorController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
from PlayerEvents import g_playerEvents as g_playerEvents
from Account import PlayerAccount as PlayerAccount
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_DEFAULT_OVERLAY_COLOR: Any
_OVERLAY_SOLID_KEYS: tuple
_OVERLAY_PATTERN_KEYS: tuple
_OVERLAY_TARGET_INDEXES: dict
g_instance = None

class EdgeDetectColorController(object):
    settingsCore: Any
    __colors: Any
    def __init__(self, dataSec):
        ...
    def updateColors(self):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def __readColors(self, colors, cType, section):
        ...
    def __readOverlayColors(self, out, common, cType, overlayType, keys, section):
        ...
    def __onAccountShowGUI(self, ctx):
        ...
    def __changeColor(self, diff):
        ...
