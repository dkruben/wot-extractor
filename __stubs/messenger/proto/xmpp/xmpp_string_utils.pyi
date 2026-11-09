# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_string_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from builtins import range as range
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
from messenger.proto.xmpp.errors import ClientContactError as ClientContactError, ClientIntLimitError as ClientIntLimitError, ClientChannelError as ClientChannelError
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT as CONTACT_LIMIT, CONTACT_ERROR_ID as CONTACT_ERROR_ID, LIMIT_ERROR_ID as LIMIT_ERROR_ID, CHANNEL_LIMIT as CHANNEL_LIMIT, CHANNEL_ERROR_ID as CHANNEL_ERROR_ID
from messenger.proto.xmpp.xmpp_string_grep import ResourcePrep as ResourcePrep, XmppStringPrepError as XmppStringPrepError

def validateRosterItemGroup(name):
    ...
def validateContactNote(note):
    ...
def validateUserRoomName(name):
    ...
def validateUserRoomPwd(password, isRetype=False):
    ...
def validateUserRoomPwdPair(password, retype):
    ...
