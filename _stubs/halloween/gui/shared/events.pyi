# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/shared/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.event_bus import SharedEvent as SharedEvent
from gui.shared.events import HasCtxEvent as HasCtxEvent

class HWHangarEvent(SharedEvent):
    REFRESH = 'hwHangarEvent/refresh'

class HWBattleLootEvent(HasCtxEvent):
    VEH_CAPTURING_START = 'HWBattleLootEvent/VEH_CAPTURING_START'
    VEH_CAPTURING_CANCEL = 'HWBattleLootEvent/VEH_CAPTURING_CANCEL'
    APPEAR = 'HWBattleLootEvent/APPEAR'
    CAPTURED = 'HWBattleLootEvent/CAPTURED'
