# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.prb_control.entities.base.pre_queue.actions_validator import InQueueValidator as InQueueValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from helpers import dependency as dependency
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController

class StoryModeStateValidator(BaseActionsValidator):
    def _validate(self):
        ...

class StoryModeActionsValidator(ActionsValidatorComposite):
    def __init__(self, entity):
        ...
