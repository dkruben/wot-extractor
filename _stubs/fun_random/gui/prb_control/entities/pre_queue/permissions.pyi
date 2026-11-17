# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/permissions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions as PreQueuePermissions

class FunRandomPermissions(PreQueuePermissions, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def canCreateSquad(self):
        ...
