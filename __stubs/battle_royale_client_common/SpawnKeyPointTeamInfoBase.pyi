# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/common/battle_royale_client_common/SpawnKeyPointTeamInfoBase.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event

class SpawnKeyPointTeamInfoBase(object):
    __placed: Any
    __em: Any
    onReceiveAvailableSpawnKeyPoints: Any
    onReceiveTeamSpawnKeyPoints: Any
    onReceiveSpawnKeyPointsCloseTime: Any
    onCloseChooseSpawnKeyPointsWindow: Any
    def __init__(self):
        ...
    def _avatar(self):
        ...
    def onDestroy(self):
        ...
    def _doLog(self, msg):
        ...
    def set_availableSpawnKeyPoints(self, prev):
        ...
    def set_teamSpawnKeyPoints(self, prev):
        ...
    def set_spawnKeyPointsCloseTime(self, prev):
        ...
    @property
    def placed(self):
        ...
    def isVehiclePlaced(self):
        ...
