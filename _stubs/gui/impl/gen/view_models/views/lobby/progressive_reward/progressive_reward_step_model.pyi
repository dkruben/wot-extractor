# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/progressive_reward/progressive_reward_step_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel

class ProgressiveRewardStepModel(ViewModel):
    __slots__: tuple
    PR_STATE_NOT_RECEIVED = 'not_received'
    PR_STATE_OPENED = 'opened'
    PR_STATE_PROB_MIN = 'prob_min'
    PR_STATE_PROB_MED = 'prob_med'
    PR_STATE_PROB_MAX = 'prob_max'
    PR_STATE_RECEIVED = 'received'
    PR_TYPE_SMALL = 'small'
    PR_TYPE_BIG = 'big'
    PR_TYPE_SMALL_HIDDEN = 'small_hidden'
    PR_TYPE_BIG_HIDDEN = 'big_hidden'
    def __init__(self, properties=3, commands=0):
        ...
    def getStepState(self):
        ...
    def setStepState(self, value):
        ...
    def getRewardType(self):
        ...
    def setRewardType(self, value):
        ...
    def getHasPreviousStep(self):
        ...
    def setHasPreviousStep(self, value):
        ...
    def _initialize(self):
        ...
