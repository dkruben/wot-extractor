# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/skeletons/halloween_bestiary_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from typing import Tuple as Tuple, Optional as Optional
from Event import Event as Event
from halloween_common.configs.halloween_bestiary import BestiaryModel as BestiaryModel, EnemyModel as EnemyModel
from halloween.gui.game_control.halloween_bestiary_controller import EnemyData as EnemyData

class IHalloweenBestiaryController(IGameController):
    onSettingsUpdate = None
    def _getConfig(self):
        ...
    def getEnemyByIntCD(self, intCD):
        ...
    def getEnemyByToken(self, token):
        ...
    def getTokenIdxByEnemy(self, enemy):
        ...
    @property
    def enemies(self):
        ...
    def hasEnemy(self, token):
        ...
    def getFirstNewEnemy(self):
        ...
    @property
    def hasUnlockedEnemies(self):
        ...
    @property
    def isBestiaryPostponed(self):
        ...
    @isBestiaryPostponed.setter
    def isBestiaryPostponed(self, value):
        ...
