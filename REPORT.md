# wot-extractor — CT report (2.4.2.0 Common Test)

Generated 2026-11-09T15:29:47+00:00 · install `C:\Games\World_of_Tanks_CT` (sd) · `.version_name` = 2.4.2.0 Common Test

## Folder contents

| Folder | What it is | Files | Size |
|---|---|---|---|
| `sources/` | ORIGINAL files extracted from res and res_mods (exact copy, SHA-256 in the manifest); the .py files next to the .pyc are DECOMPILED code (first line 'wot-extractor: codigo DESCOMPILADO'); processed .pyc/XML/SWF may have been removed by `clean` | 14509 | 308 MB |
| `sources_xml/` | BigWorld binary XML DECODED to text | 4713 | 211 MB |
| `sources_as/` | SWF: catalog, AS3 code DECOMPILED by FFDec (or declarations only, marked), exported assets and .asasm disassembly | 67346 | 861 MB |
| `sources_gameface/` | FORMATTED JS/CSS/HTML (not the original source code), analyses, views and PROBABLE links to Python (originals in sources/) | 4011 | 79 MB |
| `__stubs/` | .pyi stubs GENERATED only from information verified in the code (Any = unknown) | 10201 | 29 MB |

## Phases

- **Extraction** (2026-11-09T13:04:15+00:00, consistent: True): 19957 files out of 480210 found, success 19957, failures 0. Binary XML decoded: {'success': 4713}. Removed from `sources/` by `clean` (already processed; marked in the manifest): {'xml': 4713, 'python_bytecode': 11333, 'scaleform': 749}.
- **Python decompilation (.pyc 2.7)** (2026-11-09T13:04:17+00:00): {'success': 11333, 'partial': 14, 'failed': 3}. Not fully recovered: 17.
- **ActionScript/SWF** (2026-11-09T13:04:19+00:00): {'success': 723, 'extracted': 26, 'partial': 6}. Not fully recovered: 6.
- **Gameface** (2026-11-09T15:29:35+00:00): {'success': 2643}. Not fully recovered: 0. Views: 668; links to Python (probable): {'provavel': 304, 'provavel-forte': 285, 'nao-encontrada': 79}.
- **.pyi stubs** (2026-11-09T12:43:39+00:00): {'success': 10114, 'partial': 16}. Not fully recovered: 16. Classes 19815, functions 121333, modules without code 69.

## Verification

Last `verify` (2026-11-09T13:05:22+00:00): integrity OK; 19957 files checked; update needed: no.

## Not fully recovered (first ones per phase)

### Python decompilation (.pyc 2.7)

- `res/scripts/client/gui/impl/battle/postmortem_panel/postmortem_panel_view.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 55)
- `res/scripts/client/gui/impl/lobby/battle_results/states.pyc` — failed: AttributeError: 'SyntaxTree' object has no attribute 'pattr'
- `res/scripts/client/gui/impl/lobby/hangar/base/proto_states.pyc` — failed: AttributeError: 'SyntaxTree' object has no attribute 'pattr'
- `res/scripts/client/gui/impl/lobby/hangar/playlists_states.pyc` — failed: AttributeError: 'SyntaxTree' object has no attribute 'pattr'
- `res/scripts/client/gui/impl/lobby/personal_missions_30/views_helpers.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 272)
- `res/scripts/client/gui/impl/lobby/tank_setup/interactors/opt_device.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 207)
- `res/scripts/client/gui/lootbox_system/base/bonuses_packers.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 124)
- `res/scripts/client/gui/shared/utils/requesters/ItemsRequester.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 661)
- `res/scripts/client/helpers/__init__.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 174)
- `res/scripts/client/messenger/gui/Scaleform/view/lobby/antispam_message.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 15)
- `res/scripts/common/UnitRoster.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 436)
- `res/scripts/common/cgf_demo/test_movers.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 18)
- `res/scripts/common/live_crc.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 323)
- `res/scripts/common/persistent_data_cache_common/types.pyc` — partial: sintaxe: SyntaxError: invalid syntax (linha 10)
- `res/scripts/common/serializable_types/customizations/customization_outfit.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 56)
- `res/scripts/common/serialization/component_xml_deserializer.pyc` — partial: descompilador: SourceWalkerError: Deparsing stopped due to parse error; sintaxe: SyntaxError: invalid syntax (linha 31)
- `res/scripts/common/site-packages/typing-3.10.0.0/test_typing.pyc` — partial: sintaxe: SyntaxError: invalid syntax (linha 394)

### ActionScript/SWF

- `res/gui/flash/battle.swf` — partial: 2 linha(s) com fluxo nao reconstruido (§§)
- `res/gui/flash/battleVehicleMarkersApp.swf` — partial: 2 linha(s) com fluxo nao reconstruido (§§)
- `res/gui/flash/swc/gui_battle-1.0-SNAPSHOT.swc` — partial: 2 linha(s) com fluxo nao reconstruido (§§)
- `res/last_stand/gui/flash/battle.swf` — partial: 2 linha(s) com fluxo nao reconstruido (§§)
- `res/last_stand/gui/flash/lastStandBattleVehicleMarkersApp.swf` — partial: 2 linha(s) com fluxo nao reconstruido (§§)
- `res/story_mode/gui/flash/storyModeBattleVehicleMarkersApp.swf` — partial: 2 linha(s) com fluxo nao reconstruido (§§)

### .pyi stubs

- `res/scripts/client/gui/impl/battle/postmortem_panel/postmortem_panel_view.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 55))
- `res/scripts/client/gui/impl/lobby/battle_results/states.pyc` — partial: gerado do bytecode (sem codigo descompilado)
- `res/scripts/client/gui/impl/lobby/hangar/base/proto_states.pyc` — partial: gerado do bytecode (sem codigo descompilado)
- `res/scripts/client/gui/impl/lobby/hangar/playlists_states.pyc` — partial: gerado do bytecode (sem codigo descompilado)
- `res/scripts/client/gui/impl/lobby/personal_missions_30/views_helpers.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 272))
- `res/scripts/client/gui/impl/lobby/tank_setup/interactors/opt_device.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 207))
- `res/scripts/client/gui/lootbox_system/base/bonuses_packers.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 124))
- `res/scripts/client/gui/shared/utils/requesters/ItemsRequester.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 661))
- `res/scripts/client/helpers/__init__.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 174))
- `res/scripts/client/messenger/gui/Scaleform/view/lobby/antispam_message.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 15))
- `res/scripts/common/UnitRoster.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 436))
- `res/scripts/common/cgf_demo/test_movers.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 18))
- `res/scripts/common/live_crc.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 323))
- `res/scripts/common/persistent_data_cache_common/types.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 10))
- `res/scripts/common/serializable_types/customizations/customization_outfit.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 56))
- `res/scripts/common/serialization/component_xml_deserializer.pyc` — partial: gerado do bytecode (SyntaxError: invalid syntax (linha 31))

## Tool versions

```
{
 "wot_extractor": "0.1.0",
 "python": "3.14.3",
 "manifest_schema": 1,
 "validator": 2,
 "bwxml_decoder": 1,
 "decompile": [
  "uncompyle6=uncompyle6 3.9.2 / Python 2.7.18",
  "uncompyle6-py3=uncompyle6 3.9.3 / Python 3.14.3"
 ],
 "actionscript": "swf1/abc1/FFDec 26.2.1/assets=1",
 "gameface": "gf3/fmt1/node v20.19.2/format=1",
 "stubs": "d2/r1"
}
```
