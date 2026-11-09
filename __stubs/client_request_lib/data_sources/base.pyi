# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/client_request_lib/data_sources/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod
from py2to3.patched_future import with_metaclass as with_metaclass
__all__: tuple

# base nao representavel no stub: with_metaclass(...)
class BaseDataAccessor:
    def __init__(self):
        ...
    @abstractmethod
    def login(self, callback, account_id, spa_token, jwt):
        ...
    @abstractmethod
    def logout(self, callback):
        ...
    @abstractmethod
    def get_clans_ratings(self, callback, clan_ids, fields=None):
        ...
    @abstractmethod
    def get_accounts_names(self, callback, account_ids):
        ...
    @abstractmethod
    def get_clan_invites(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        ...
    @abstractmethod
    def get_account_invites(self, callback, fields=None, statuses=None, offset=0, limit=18):
        ...
    @abstractmethod
    def get_account_applications_count_since(self, callback, account_id, since=None):
        ...
    @abstractmethod
    def get_clan_invites_count_since(self, callback, clan_id, since=None):
        ...
    @abstractmethod
    def get_clan_applications(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        ...
    @abstractmethod
    def search_clans(self, callback, search, get_total_count=False, fields=None, offset=0, limit=18):
        ...
    @abstractmethod
    def get_clans_info(self, callback, clan_ids, fields=None):
        ...
    @abstractmethod
    def get_clan_members(self, callback, clan_id, fields=None):
        ...
    @abstractmethod
    def get_clan_favorite_attributes(self, callback, clan_id, fields=None):
        ...
    @abstractmethod
    def get_accounts_clans(self, callback, account_ids, fields=None):
        ...
    @abstractmethod
    def get_accounts_info(self, callback, account_ids, fields=None):
        ...
    @abstractmethod
    def get_clan_provinces(self, callback, clan_id, fields=None):
        ...
    @abstractmethod
    def get_clan_globalmap_stats(self, callback, clan_id, fields=None):
        ...
    @abstractmethod
    def get_fronts_info(self, callback, front_names=None, fields=None):
        ...
    @abstractmethod
    def get_stronghold_info(self, callback, clan_id=None, fields=None):
        ...
    @abstractmethod
    def get_strongholds_statistics(self, callback, clan_id, fields=None):
        ...
    @abstractmethod
    def get_strongholds_state(self, callback, clan_id, fields=None):
        ...
