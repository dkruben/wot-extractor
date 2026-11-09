# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/customization/attachments_preview/attachments_preview_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachment_bonus_model import AttachmentBonusModel as AttachmentBonusModel

class AttachmentsPreviewFeature(Enum):
    CHALLENGES = 'challenges'
    OPEN_BUNDLE = 'open_bundle'
    BATTLE_PASS = 'battle_pass'

class AttachmentsPreviewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getAttachmentSetID(self):
        ...
    def setAttachmentSetID(self, value):
        ...
    def getFeature(self):
        ...
    def setFeature(self, value):
        ...
    def getAttachments(self):
        ...
    def setAttachments(self, value):
        ...
    @staticmethod
    def getAttachmentsType():
        ...
    def _initialize(self):
        ...
