# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/twin_shoot/guns_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.parts.guns.common import IGunComponent as IGunComponent, IGunShootingEvents as IGunShootingEvents, IGunShootingListener as IGunShootingListener

class ITwinShootGunComponent(IGunComponent):
    def isDoubleBarrelMode(self):
        ...
    def getActiveGunIndexes(self):
        ...
    def getAfterShotDelay(self):
        ...
    def getNextGunIndexes(self):
        ...

class ITwinShootingEventsLogic(object):
    onActiveGunsUpdate = None
    onAnimatedGunsUpdate = None
    def processNextGunsUpdate(self, nextGunIndexes):
        ...

class ITwinShootingEvents(IGunShootingEvents, ITwinShootingEventsLogic):
    ...

class ITwinShootingListenerLogic(object):
    def onActiveGunsUpdate(self, gunIndexes):
        ...
    def onAnimatedGunsUpdate(self, gunIndexes):
        ...

class ITwinShootingListener(IGunShootingListener, ITwinShootingListenerLogic):
    ...
