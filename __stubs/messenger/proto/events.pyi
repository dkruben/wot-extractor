# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
g_messengerEvents: Any

class _ChannelsSharedEvents(object):
    __slots__: tuple
    __eventManager: Any
    onChannelInited: Any
    onPlayerEnterChannelByAction: Any
    onChannelDestroyed: Any
    onConnectingToSecureChannel: Any
    onChannelInfoUpdated: Any
    onConnectStateChanged: Any
    onMessageReceived: Any
    onHistoryReceived: Any
    onCommandReceived: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class ChannelEvents(object):
    __slots__: tuple
    __eventManager: Any
    onConnectStateChanged: Any
    onChannelInfoUpdated: Any
    onMembersListChanged: Any
    onMemberStatusChanged: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class MemberEvents(object):
    __slots__: tuple
    __eventManager: Any
    onMemberStatusChanged: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _VOIPSharedEvents(object):
    __slots__: tuple
    __eventManager: Any
    onCredentialReceived: Any
    onCredentialFailed: Any
    onChannelAvailable: Any
    onChannelLost: Any
    onChannelEntered: Any
    onChannelLeft: Any
    onVoiceChatInitSucceeded: Any
    onVoiceChatInitFailed: Any
    onPlayerSpeaking: Any
    onCaptureDeviceSetFailed: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _UsersSharedEvents(object):
    __slots__: tuple
    __eventManager: Any
    onFriendsReceived: Any
    onIgnoredReceived: Any
    onMutedReceived: Any
    onUsersListReceived: Any
    onUserActionReceived: Any
    onBattleUserActionReceived: Any
    onEmptyGroupsChanged: Any
    onUserStatusUpdated: Any
    onClanMembersListChanged: Any
    onFindUsersComplete: Any
    onFindUsersFailed: Any
    onFriendshipRequestsAdded: Any
    onFriendshipRequestsUpdated: Any
    onNotesListReceived: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _ServiceChannelEvents(object):
    __slots__: tuple
    __eventManager: Any
    onServerMessageReceived: Any
    onCustomMessageDataReceived: Any
    onClientMessageReceived: Any
    onChatMessageReceived: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _ShadowEvents(object):
    __slots__: tuple
    __eventManager: Any
    onActionDone: Any
    onActionFailed: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _MessengerEvents(object):
    __slots__: tuple
    __channels: Any
    __users: Any
    __serviceChannel: Any
    __voip: Any
    __shadow: Any
    onErrorReceived: Any
    onCustomMessage: Any
    onPluginConnected: Any
    onPluginDisconnected: Any
    onPluginConnectFailed: Any
    onLockPopUpMessages: Any
    onUnlockPopUpMessages: Any
    def __init__(self):
        ...
    @property
    def channels(self):
        ...
    @property
    def users(self):
        ...
    @property
    def serviceChannel(self):
        ...
    @property
    def voip(self):
        ...
    @property
    def shadow(self):
        ...
    def clear(self):
        ...
