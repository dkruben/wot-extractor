# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/shared/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.event_bus import SharedEvent as SharedEvent

class CapturePointEvent(SharedEvent):
    INIT_CAPTURABLE_POINT = 'fortRush/initCapturablePoint'
    CAPTURABLE_POINT_UPDATE = 'fortRush/capturableBaseUpdate'
    capturablePointName: Any
    totalInvaders: Any
    invadersTeam: Any
    ownersTeam: Any
    isContested: Any
    captureProgressPercent: Any
    state: Any
    transform: Any
    numberOfAttackers: Any
    isNeutralizing: Any
    uid: Any
    def __init__(self, eventType, capturablePointName=None, totalInvaders=None, invadersTeam=None, ownersTeam=None, isContested=None, captureProgressPercent=None, state=None, transform=None, numberOfAttackers=None, isNeutralizing=None, uid=-1):
        ...

class CaptureInvaderEvent(SharedEvent):
    INVADER_ADDED = 'fortRush/captureInvaderAdded'
    INVADER_REMOVED = 'fortRush/captureInvaderRemoved'
    vehicleID: Any
    baseName: Any
    def __init__(self, eventType, vehicleID, baseName=''):
        ...

class RespawnCtrlEvent(SharedEvent):
    SHOW_SPAWN_POINTS = 'game/showSpawnPoints'
    HIDE_SPAWN_POINTS = 'game/hideSpawnPoints'
