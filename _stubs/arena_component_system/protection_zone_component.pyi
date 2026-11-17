# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/protection_zone_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
import Event as Event

class ProtectionZoneComponent(ClientArenaComponent):
    protectionZones: Any
    __protectionZones: Any
    __isPlayerInZone: Any
    onProtectionZoneAdded: Any
    onProtectionZoneActive: Any
    onPlayerInProtectedZoneAction: Any
    def __init__(self, componentSystem):
        ...
    def addProtectionZone(self, protZone):
        ...
    def setProtectionZoneActive(self, zoneID, isActive):
        ...
    def removeProtectionZone(self, protZone):
        ...
    def getProtectionZoneById(self, zoneID):
        ...
    def getOwningTeamForZone(self, zoneID):
        ...
    def isProtectionZoneActive(self, zoneID):
        ...
    def playerInProtectedZone(self, zoneID, hasPlayerEntered):
        ...
    def isPlayerInProtectedZone(self, zoneID=None):
        ...
