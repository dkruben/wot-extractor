# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
import BigWorld as BigWorld
from gui.impl.dialogs.dialogs import showSkillsTrainingConfirmDialog as showSkillsTrainingConfirmDialog
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.crew.container_vews.skills_training.events import SkillsTrainingComponentViewEvents as SkillsTrainingComponentViewEvents
from gui.impl.pub.dialog_window import SingleDialogResult as SingleDialogResult
from gui.shared.event_dispatcher import showChangeCrewMember as showChangeCrewMember
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.items_actions import factory as factory
from items.components import skills_constants as skills_constants
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from wg_async import wg_async as wg_async, wg_await as wg_await

class SkillsTrainingInteractionController(InteractionController):
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @wg_async
    def onChangeTankman(self, tankmanInvID, slotIdx):
        ...
    def _onSkillHover(self, skillId):
        ...
    def _onSkillOut(self, skillId):
        ...
    def _onSkillClick(self, skillId):
        ...
    def _onTrain(self):
        ...
    def _onCancel(self):
        ...
    # decorador original: @wg_async
    def _onClose(self):
        ...
    # decorador original: @wg_async
    def __showConfirm(self):
        ...
    def __train(self):
        ...
    def __clearSelection(self):
        ...
