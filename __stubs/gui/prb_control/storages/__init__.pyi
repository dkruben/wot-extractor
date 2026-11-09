# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/storages/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as _P_TYPE
from constants import QUEUE_TYPE as _Q_TYPE
from constants import PREBATTLE_TYPE_NAMES as _P_NAMES
from constants import QUEUE_TYPE_NAMES as _Q_NAMES
from gui.prb_control.storages.winback_storage import WinbackStorage as WinbackStorage
from gui.shared.system_factory import registerPrbStorage as registerPrbStorage, collectPrbStorage as collectPrbStorage, collectAllStorages as collectAllStorages
from gui.prb_control.settings import CTRL_ENTITY_TYPE as _C_TYPE
from gui.prb_control.settings import CTRL_ENTITY_TYPE_NAMES as _C_NAMES
from gui.prb_control.storages.local_storage import LocalStorage as LocalStorage, RecentPrbStorage as RecentPrbStorage
from gui.prb_control.storages.maps_training_storage import MapsTrainingStorage as MapsTrainingStorage
from gui.prb_control.storages.prb_storage import TrainingStorage as TrainingStorage
from gui.prb_control.storages.ranked_storage import RankedStorage as RankedStorage
from gui.prb_control.storages.event_battles_storage import EventBattlesStorage as EventBattlesStorage
from gui.prb_control.storages.stronghold_storage import StrongholdStorage as StrongholdStorage
from gui.prb_control.storages.tournament_storage import TournamentStorage as TournamentStorage
from gui.prb_control.storages.mapbox_storage import MapboxStorage as MapboxStorage
from soft_exception import SoftException as SoftException
__all__: tuple
RECENT_PRB_STORAGE = 'recentPrbStorage'

class storage_getter(object):
    __name: Any
    def __init__(self, name):
        ...
    def __call__(self, *args):
        ...

class legacy_storage_getter(storage_getter):
    def __init__(self, legacyType):
        ...

class prequeue_storage_getter(storage_getter):
    def __init__(self, queueType):
        ...

class PrbStorageDecorator(LocalStorage):
    __storages: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def swap(self):
        ...
    def clear(self):
        ...
    def onAvatarBecomePlayer(self):
        ...

def _makeUniqueName(ctrlName, entityName):
    ...
def _makeLegacyName(legacyType):
    ...
def makeQueueName(queueType):
    ...
