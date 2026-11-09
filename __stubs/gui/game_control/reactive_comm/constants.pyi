# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/reactive_comm/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, unique as unique
MAX_CHANNEL_HISTORY = 10
CHANNEL_UNSUBSCRIPTION_DELAY = 60

# decorador original: @unique
class SubscriptionCommand(Enum):
    Subscribe = 'subscribe'
    Unsubscribe = 'unsubscribe'
    GetLast = 'get_last'

# decorador original: @unique
class SubscriptionServerStatus(Enum):
    Subscribed = 'subscribed'
    NotExists = 'not_exists'
    ChannelsLimit = 'channels_limit'
    Unsubscribed = 'unsubscribed'
    NotSubscribed = 'not_subscribed'
    ChannelDeleted = 'channel_deleted'
    UnknownCommand = 'unknown_command'
    NameNotAllowed = 'name_not_allowed'
    CachedMessage = 'cached_message'
    NoCachedMessage = 'no_cached_message'
    @classmethod
    def fromString(cls, value):
        ...

# decorador original: @unique
class SubscriptionClientStatus(Enum):
    NotExists = 'not_exists'
    Unsubscribed = 'unsubscribed'
    Subscribing = 'subscribing'
    Subscribed = 'subscribed'
    Unsubscribing = 'unsubscribing'
    Disabled = 'disabled'
    InvalidObject = 'invalid_object'
    NameNotAllowed = 'name_not_allowed'
    AlreadySubscribed = 'already_subscribed'

# decorador original: @unique
class SubscriptionCloseReason(Enum):
    Request = 'request'
    Cancel = 'cancel'
    Deleted = 'deleted'
