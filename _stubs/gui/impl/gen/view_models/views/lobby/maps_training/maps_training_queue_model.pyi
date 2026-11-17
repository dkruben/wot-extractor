# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/maps_training/maps_training_queue_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R

class MapsTrainingQueueModel(ViewModel):
    __slots__: tuple
    DELAY_DEFAULT = ''
    DELAY_NORMAL = 'normal'
    DELAY_LONG = 'long'
    onQuit: Any
    onMenu: Any
    onShowPrevTip: Any
    onShowNextTip: Any
    onMoveSpace: Any
    onMouseOver3dScene: Any
    def __init__(self, properties=4, commands=6):
        ...
    def getTime(self):
        ...
    def setTime(self, value):
        ...
    def getDescrTip(self):
        ...
    def setDescrTip(self, value):
        ...
    def getIsDelay(self):
        ...
    def setIsDelay(self, value):
        ...
    def getDelayStatus(self):
        ...
    def setDelayStatus(self, value):
        ...
    def _initialize(self):
        ...
