# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/skeletons/halloween_anomalies_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from collections import OrderedDict as OrderedDict
from Event import Event as Event
from typing import List as List, Optional as Optional
from halloween.gui.game_control.halloween_anomalies_controller import AnomalyData as AnomalyData, RecipeData as RecipeData

class IHalloweenAnomaliesController(IGameController):
    onRefreshData = None
    onChangeSystemAnomaliesUnlock = None
    @property
    def anomalies(self):
        ...
    @property
    def lootAnomalies(self):
        ...
    @property
    def recipes(self):
        ...
    def getAnomalyByID(self, anomalyID):
        ...
