# wot-extractor — relatório CT (2.4.2.0 Common Test)

Gerado em 2026-11-09T12:47:25+00:00 · instalação `C:\Games\World_of_Tanks_CT` (sd) · `.version_name` = 2.4.2.0 Common Test

## Conteúdo das pastas

| Pasta | O que é | Ficheiros | Tamanho |
|---|---|---|---|
| `sources/` | ORIGINAIS extraidos de res, res_mods e mods (copia exata, SHA-256 no manifesto); os .py ao lado dos .pyc sao codigo DESCOMPILADO (1.a linha 'wot-extractor: codigo DESCOMPILADO') | 31304 | 861 MB |
| `sources_xml/` | XML binarios do BigWorld DESCODIFICADOS para texto (o original continua em sources/) | 4713 | 211 MB |
| `sources_as/` | SWF: catalogo, codigo AS3 DESCOMPILADO pelo FFDec (ou so declaracoes, marcadas) e recursos exportados (o SWF original continua em sources/) | 67346 | 861 MB |
| `sources_gameface/` | JS/CSS/HTML FORMATADOS (nao sao o codigo-fonte original), analises, views e ligacoes PROVAVEIS ao Python (originais em sources/) | 4011 | 79 MB |
| `__stubs/` | stubs .pyi GERADOS so com informacao verificada no codigo (Any = desconhecido) | 10201 | 29 MB |

## Fases

- **Extração** (2026-11-09T12:35:26+00:00, consistente: True): 19957 ficheiros de 480210 encontrados, sucesso 19957, falhas 0. XML binários descodificados: {'success': 4713}.
- **Descompilação Python (.pyc 2.7)** (2026-11-09T12:35:28+00:00): {'success': 11333, 'partial': 14, 'failed': 3}. Não totalmente recuperados: 17.
- **ActionScript/SWF** (2026-11-09T12:35:31+00:00): {'success': 723, 'extracted': 26, 'partial': 6}. Não totalmente recuperados: 6.
- **Gameface** (2026-11-09T12:42:08+00:00): {'success': 2643}. Não totalmente recuperados: 0. Views: 668; ligações ao Python (prováveis): {'provavel': 304, 'provavel-forte': 285, 'nao-encontrada': 79}.
- **Stubs .pyi** (2026-11-09T12:43:39+00:00): {'success': 10114, 'partial': 16}. Não totalmente recuperados: 16. Classes 19815, funções 121333, módulos sem código 69.

## Verificação

Última `verify` (2026-11-09T12:46:25+00:00): integridade OK; 19957 ficheiros verificados; atualização necessária: não.

## Não totalmente recuperados (primeiros por fase)

### Descompilação Python (.pyc 2.7)

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

### Stubs .pyi

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

## Versões das ferramentas

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
