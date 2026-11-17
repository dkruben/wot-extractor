# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/recruit_dialog_template_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_content_view_model import RecruitContentViewModel as RecruitContentViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_icon_view_model import RecruitIconViewModel as RecruitIconViewModel

class RecruitDialogTemplateViewModel(DialogTemplateViewModel):
    __slots__: tuple
    def __init__(self, properties=10, commands=2):
        ...
    @property
    def recruitContent(self):
        ...
    @staticmethod
    def getRecruitContentType():
        ...
    @property
    def iconModel(self):
        ...
    @staticmethod
    def getIconModelType():
        ...
    def getText(self):
        ...
    def setText(self, value):
        ...
    def getHasVoiceover(self):
        ...
    def setHasVoiceover(self, value):
        ...
    def _initialize(self):
        ...
