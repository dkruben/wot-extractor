# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/battle/shared/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/battle/shared/__init__.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from .clip.auto_loader_clip_presenter import AutoLoaderClipPresenter
from .clip.cassette_clip_presenter import CassetteClipPresenter
from .clip.controllable_reload_presenter import ControllableReloadPresenter
from .clip.extra_shot_clip_presenter import ExtraShotClipPresenter
from .clip.shell_calibration_clip_presenter import ShellCalibrationClipPresenter
from .clip.unlimited_clip_presenter import UnlimitedClipPresenter
from .crosshair.state_presenter import CrosshairStatePresenter
from .vehicle.gun_state_presenter import GunStatePresenter
from .vehicle_mechanics.widgets_presenter import VehicleMechanicsWidgetsPresenter

def getContextMenuHandlers():
    return ()


def getViewSettings():
    return (
     ComponentSettings(R.aliases.battle.shared.vehicle_mechanics(), VehicleMechanicsWidgetsPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.crosshair_state(), CrosshairStatePresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.gun_state(), GunStatePresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.shell_calibration(), ShellCalibrationClipPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.cassette(), CassetteClipPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.auto_loader(), AutoLoaderClipPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.extra_shot(), ExtraShotClipPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.controllable_reload(), ControllableReloadPresenter, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(R.aliases.battle.shared.clip.unlimited(), UnlimitedClipPresenter, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return ()
