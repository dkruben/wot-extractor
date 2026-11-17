# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/guns_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from vehicles.parts.guns.common import IGunComponent as IGunComponent, IGunShootingEvents as IGunShootingEvents, IGunShootingListener as IGunShootingListener

class IAutoShootDispersionState(object):
    def getCurrentDispersionFactor(self):
        ...

class IAutoShootGunComponentState(object):
    def isShooting(self):
        ...
    def isContinuousShooting(self):
        ...
    def getDefaultShotRatePerSecond(self):
        ...
    def getGroupShotInterval(self):
        ...
    def getShotRatePerSecond(self):
        ...

class IAutoShootGunComponent(IGunComponent):
    def getComponentState(self):
        ...
    def getDispersionState(self):
        ...

class IAutoShootingEventsLogic(object):
    onBurstActivation = None
    onBurstDeactivation = None
    onContinuousBurstActivation = None
    onContinuousBurstDeactivation = None
    onContinuousBurstUpdate = None
    onShotRateUpdate = None
    def updateAutoShootingState(self, componentState):
        ...

class IAutoShootingEvents(IGunShootingEvents, IAutoShootingEventsLogic):
    ...

class IAutoShootingListenerLogic(object):
    def onBurstActivation(self):
        ...
    def onBurstDeactivation(self):
        ...
    def onContinuousBurstActivation(self):
        ...
    def onContinuousBurstDeactivation(self):
        ...
    def onContinuousBurstUpdate(self):
        ...
    def onShotRateUpdate(self, rate):
        ...

class IAutoShootingListener(IGunShootingListener, IAutoShootingListenerLogic):
    ...
