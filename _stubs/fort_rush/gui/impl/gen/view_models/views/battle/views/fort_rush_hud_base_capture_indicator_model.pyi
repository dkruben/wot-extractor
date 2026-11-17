# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/battle/views/fort_rush_hud_base_capture_indicator_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class FortRushBaseCaptureTeam(Enum):
    NEUTRAL = 'neutral'
    ALLY = 'ally'
    ENEMY = 'enemy'

class FortRushBaseCaptureState(Enum):
    IDLE = 'Idle'
    CAPTURING = 'Capturing'
    CONTESTED = 'Contested'
    DECAPPING = 'Decapping'

class FortRushHudBaseCaptureIndicatorModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getLabel(self):
        ...
    def setLabel(self, value):
        ...
    def getOwnerTeam(self):
        ...
    def setOwnerTeam(self, value):
        ...
    def getCapturingTeam(self):
        ...
    def setCapturingTeam(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getCaptureProgress(self):
        ...
    def setCaptureProgress(self, value):
        ...
    def getUid(self):
        ...
    def setUid(self, value):
        ...
    def _initialize(self):
        ...
