# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/GoodieTargets.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TypeVar as TypeVar
GoodieTargetType: Any

class GoodieTarget(object):
    _targetID: Any
    _limit: Any
    def __init__(self, targetID, limit=None):
        ...
    @property
    def targetID(self):
        ...
    @property
    def limit(self):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...

class GoodieTargetAvatar(GoodieTarget):
    ...

class GoodieTargetVehicle(GoodieTarget):
    ...

class HangarTarget(GoodieTarget):
    ...

class BuyPremiumAccount(HangarTarget):
    def __init__(self, targetID, limit=None):
        ...

class BuySlot(HangarTarget):
    def __init__(self, targetID=None, limit=None):
        ...

class PostBattle(GoodieTargetVehicle):
    def __init__(self, targetID=None, limit=None):
        ...

class BuyGoldTankmen(HangarTarget):
    def __init__(self, targetID=None, limit=None):
        ...

class BuyVehicle(HangarTarget):
    def __init__(self, targetID, limit=None):
        ...

class EpicMeta(GoodieTargetAvatar):
    def __init__(self, targetID=None, limit=None):
        ...

class EpicPostBattle(PostBattle):
    ...

class DemountOptionalDevice(HangarTarget):
    ...

class DropSkill(GoodieTarget):
    ...

class XpTransfer(GoodieTarget):
    ...

class BuyPet(GoodieTarget):
    ...
