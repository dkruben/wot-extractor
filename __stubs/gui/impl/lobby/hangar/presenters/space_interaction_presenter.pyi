# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/space_interaction_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.space_interaction_model import SpaceInteractionModel as SpaceInteractionModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from hangar_selectable_objects.interfaces import ISelectableLogic as ISelectableLogic
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class SpaceInteractionPresenter:
    _selectableLogic: Any
    def __init__(self, selectableLogic):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def onHighlight3DEntity(self, entity):
        ...
    def onFade3DEntity(self, entity):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _highlight3DEntityAndShowTT(self, entity):
        ...
    def _fade3DEntityAndHideTT(self, entity):
        ...
    def _onMoveSpace(self, args=None):
        ...
    def _onCursorOver3DScene(self, args=None):
        ...
