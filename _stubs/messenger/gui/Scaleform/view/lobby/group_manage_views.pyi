# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/group_manage_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from helpers import i18n as i18n
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta as BaseManageContactViewMeta
from messenger import normalizeGroupId as normalizeGroupId
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT as CONTACT_LIMIT
from messenger.proto.xmpp.xmpp_string_utils import validateRosterItemGroup as validateRosterItemGroup
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.ext import passCensor as passCensor

class GroupManageView(BaseManageContactViewMeta):
    usersStorage: Any
    _currentName: Any
    def __init__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def checkText(self, txt):
        ...
    def _getDefaultInitData(self, mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip):
        ...

class GroupCreateView(GroupManageView):
    def onOk(self, data):
        ...
    def _getInitDataObject(self):
        ...

class GroupRenameView(GroupManageView):
    __isInited: Any
    def __init__(self):
        ...
    def onOk(self, data):
        ...
    def _getInitDataObject(self):
        ...
    def as_setLabelS(self, msg):
        ...
