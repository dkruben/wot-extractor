# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/recruit_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.recruit_dialog_template_view_model import RecruitDialogTemplateViewModel as RecruitDialogTemplateViewModel
from gui.impl.lobby.crew.crew_sounds import SOUNDS as CREW_SOUNDS
from gui.impl.lobby.crew.dialogs.base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.lobby.crew.dialogs.recruit_window.recruit_content import NO_DATA_VALUE as NO_DATA_VALUE, RecruitContent as RecruitContent
from gui.impl.lobby.crew.dialogs.recruit_window.recruit_dialog_utils import getIcon as getIcon, getTitle as getTitle, getIconBackground as getIconBackground, getIconName as getIconName, getTitleFromTokenData as getTitleFromTokenData
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.server_events import recruit_helper as recruit_helper
from gui.server_events.pm_constants import SOUNDS as SOUNDS, PERSONAL_MISSIONS_SILENT_SOUND_SPACE as PERSONAL_MISSIONS_SILENT_SOUND_SPACE
from gui.shared.event_dispatcher import showRecruitConfirmIrrelevantConversionDialog as showRecruitConfirmIrrelevantConversionDialog
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.processors.quests import PMGetTankwomanReward as PMGetTankwomanReward
from gui.shared.gui_items.processors.tankman import TankmanTokenRecruit as TankmanTokenRecruit, TankmanUnload as TankmanUnload, TankmanEquip as TankmanEquip
from gui.shared.utils import decorators as decorators
from gui.sounds.filters import States as States, StatesGroup as StatesGroup
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from wg_async import wg_await as wg_await, wg_async as wg_async, await_callback as await_callback

class BaseRecruitDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    _eventsCache: Any
    LAYOUT_ID: Any
    VIEW_MODEL = RecruitDialogTemplateViewModel
    _selectedNation: Any
    _selectedVehType: Any
    _selectedVehicle: Any
    _selectedSpecialization: Any
    _recruitContent: Any
    _isSlotChanged: Any
    def __init__(self, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _addButtons(self):
        ...
    def _onRecruitContentChanged(self, nation, vehType, vehicle, specialization, isSlotChanged):
        ...

class TokenRecruitDialog(BaseRecruitDialog):
    __slots__: tuple
    _itemsCache: Any
    _specialSounds: Any
    __SOUND_SETTINGS: Any
    _COMMON_SOUND_SPACE = __SOUND_SETTINGS
    __tokenName: Any
    __tokenData: Any
    __vehicleSlotToUnpack: Any
    __vehicle: Any
    _recruitContent: Any
    def __init__(self, ctx=None, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _hasIrrelevantSkils(self, vehicle):
        ...
    # decorador original: @wg_async
    def _setResult(self, result):
        ...
    # decorador original: @adisp_process
    def _submit(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _unpackTokenRecruit(self, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _unloadOldTankman(self, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _equipTankman(self, newTankman, callback=None):
        ...

class QuestRecruitDialog(BaseRecruitDialog):
    __slots__: tuple
    _itemsCache: Any
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SILENT_SOUND_SPACE
    __mission: Any
    __isFemale: Any
    __vehicleSlotToUnpack: Any
    __vehicle: Any
    _recruitContent: Any
    def __init__(self, ctx=None, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @wg_async
    def _setResult(self, result):
        ...
    # decorador original: @adisp_process
    def _submit(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _unpackQuestRecruit(self, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _equipTankman(self, newTankman, callback=None):
        ...
