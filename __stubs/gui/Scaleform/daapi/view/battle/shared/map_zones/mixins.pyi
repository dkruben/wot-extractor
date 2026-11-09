# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/map_zones/mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class MapZonesListener(object):
    _sessionProvider: Any
    def startListen(self):
        ...
    def stopListen(self):
        ...
    def _onMarkerToZoneAdded(self, zoneMarker, matrix):
        ...
    def _onMarkerFromZoneRemoved(self, zoneMarker):
        ...
    def _onMarkerProgressUpdated(self, zoneMarker):
        ...
    def _onZoneTransformed(self, zone):
        ...
    def _onTransformedZoneRemoved(self, zone):
        ...
