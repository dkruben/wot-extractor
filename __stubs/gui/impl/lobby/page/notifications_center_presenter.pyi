# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/notifications_center_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.page.footer.notifications_center_model import NotificationsCenterModel as NotificationsCenterModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from notification import NotificationMVC as NotificationMVC

# base nao representavel no stub: ViewComponent[...]
class NotificationsCenterPresenter:
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __updateNotifiedMessagesCount(self):
        ...
    def __onNotifiedMessagesCountChange(self, _):
        ...
    def __onNotificationReceived(self, notification):
        ...
