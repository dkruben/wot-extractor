# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/skeletons/game_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from typing import Dict as Dict
from Event import Event as Event

class IBRProgressionOnTokensController(IGameController):
    progressionToken = ''
    PROGRESSION_COMPLETE_TOKEN = ''
    onProgressPointsUpdated = None
    onSettingsChanged = None
    @property
    def isEnabled(self):
        ...
    @property
    def isFinished(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def setSettings(self, settings):
        ...
    def saveCurPoints(self):
        ...
    def getPrevPoints(self):
        ...
    def getCurPoints(self):
        ...
    def getProgessionPointsData(self):
        ...
    def getProgressionData(self):
        ...
