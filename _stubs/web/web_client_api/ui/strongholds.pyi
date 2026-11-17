# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/strongholds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.clans.clan_helpers import getStrongholdUrl as getStrongholdUrl
from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView as showClanSupplyView
from gui.shared import event_dispatcher as shared_events
from uilogging.clan_supply.constants import ClanSupplyLogKeys as ClanSupplyLogKeys
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema

class StrongholdsWebApiMixin(object):
    # decorador original: @w2c(...)
    def openStrongholds(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openClanSupply(self, cmd):
        ...
