# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/connection_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from Event import Event as Event

class DisconnectReason(object):
    UNDEFINED = 0
    REQUEST = 1
    EVENT = 2
    KICK = 3
    ERROR = 4

class IConnectionManager(object):
    onLoggedOn = None
    onConnected = None
    onRejected = None
    onDisconnected = None
    onKickedFromServer = None
    onKickWhileLoginReceived = None
    onQueued = None
    onPeripheryRoutingGroupUpdated = None
    @property
    def serverUserName(self):
        ...
    @property
    def serverUserNameShort(self):
        ...
    @property
    def peripheryID(self):
        ...
    @property
    def areaID(self):
        ...
    @property
    def url(self):
        ...
    @property
    def loginName(self):
        ...
    @property
    def lastLoginName(self):
        ...
    @property
    def databaseID(self):
        ...
    @property
    def connectionMethod(self):
        ...
    @property
    def peripheryRoutingGroup(self):
        ...
    @property
    def availableHosts(self):
        ...
    def isAvailablePeriphery(self, peripheryID=None):
        ...
    def initiateConnection(self, params, password, serverName):
        ...
    def stopRetryConnection(self):
        ...
    def disconnect(self):
        ...
    def setKickedFromServer(self, reason, kickReasonType, expiryTime):
        ...
    def isDisconnected(self):
        ...
    def isStandalone(self):
        ...
    def isConnected(self):
        ...
    def checkClientServerVersions(self, clientVersion, serverVersion):
        ...
    def setLastLogin(self, email):
        ...
    def setPeripheryRoutingGroup(self, routingGroup, availableHosts):
        ...
