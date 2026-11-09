# Projeto: World of Tanks Source Extractor & Decompiler

## 1. Objetivo principal

Desenvolver uma ferramenta automatizada, modular e robusta para extrair, identificar, analisar, descompilar e organizar os recursos do **World of Tanks (WoT)**, destinada ao desenvolvimento, manutenção e modernização de modificações (mods).

A ferramenta deverá suportar:

- Extração de arquivos e recursos do jogo.
- Descompilação de ficheiros Python compilados (`.pyc`).
- Recuperação de código-fonte Python sempre que tecnicamente possível.
- Análise e extração de recursos XML, JSON, SWF, ActionScript, Gameface e outros formatos relevantes.
- Geração de stubs Python para integração com IDEs.
- Identificação de dependências, módulos, imports e APIs internas.
- Organização independente das versões dos clientes EU e CT.
- Atualizações incrementais quando o jogo receber novas versões.

**Requisito fundamental:** Preservar os ficheiros originais do jogo e manter uma arquitetura limpa, reproduzível e extensível.

---

## 2. Localização dos clientes

### Cliente World of Tanks EU

- Realm: `EU`
- Disco principal: `D:\`
- Localização exata: detetar automaticamente a instalação do World of Tanks.

### Cliente World of Tanks CT

- Realm: `CT`
- Disco principal: `C:\`
- Localização exata: detetar automaticamente a instalação do cliente Common Test.

A ferramenta deverá permitir configurar manualmente os caminhos caso a deteção automática falhe.

Deverá identificar automaticamente:

- Realm do cliente.
- Versão instalada.
- Diretórios `res`, `res_mods` e `mods`.
- Arquivos `.pkg` e outros contentores existentes.
- Recursos Scaleform/Flash.
- Recursos Gameface.
- Ficheiros Python compilados e recursos associados.

Nunca assumir que todos os clientes utilizam a mesma estrutura interna.

---

## 3. Arquitetura de diretórios

Criar uma estrutura independente por realm:

```text
wot_src_EU/
├── sources/
│   ├── mods/
│   ├── res_mods/
│   └── res/
│
├── sources_as/
│   ├── scripts/
│   ├── swf/
│   └── assets/
│
├── sources_gameface/
│   ├── html/
│   ├── css/
│   ├── js/
│   ├── assets/
│   └── manifests/
│
├── __stubs/
│   ├── gui/
│   ├── helpers/
│   ├── battle/
│   └── engine/
│
├── .version_name
├── manifest.json
└── extraction_report.json
```

Replicar a mesma arquitetura para `wot_src_CT`.

### Regras de organização

1. A pasta `sources` deve preservar os caminhos relativos originais de `mods`, `res_mods` e `res`.
2. Os ficheiros `.pyc` recuperados devem produzir ficheiros `.py`, quando a descompilação for possível.
3. Os ficheiros XML, JSON e outros recursos textuais devem conservar o conteúdo original.
4. Os recursos ActionScript devem ser isolados em `sources_as`.
5. Os recursos Gameface devem ser organizados em `sources_gameface`.
6. Os stubs Python devem ser centralizados em `__stubs`.
7. Não misturar recursos de diferentes realms.
8. Registar a origem exata de cada ficheiro e o seu estado de processamento.

---

## 4. Motor de extração

Implementar um sistema capaz de percorrer os diretórios de instalação e localizar os recursos relevantes.

### Formatos prioritários

| Formato | Operação |
|---|---|
| `.pyc` | Identificação da versão Python e tentativa de descompilação |
| `.py` | Preservação do código-fonte |
| `.xml` | Extração e validação |
| `.json` | Extração e validação |
| `.swf` | Extração e análise de ActionScript |
| `.html` | Extração de interfaces Gameface |
| `.css` | Extração dos estilos |
| `.js` | Extração e análise de scripts |
| `.pkg` | Identificação e extração dos recursos suportados |
| Imagens, fontes e áudio | Preservação dos recursos binários |

A ferramenta deverá permitir acrescentar novos formatos através de plugins de processamento.

### Requisitos de segurança

- Processamento exclusivamente de leitura sobre a instalação original.
- Bloqueio de escrita nos diretórios do jogo.
- Validação de caminhos contra *path traversal*.
- Proteção contra arquivos comprimidos maliciosos ou excessivamente grandes.
- Registo de erros sem interromper toda a operação.
- Nunca executar ficheiros extraídos durante o processo de análise.

---

## 5. Descompilação Python

Desenvolver um pipeline especializado para ficheiros `.pyc`, considerando as diferentes versões de bytecode utilizadas pelo World of Tanks.

### Requisitos

1. Detetar a versão de bytecode de cada `.pyc`.
2. Utilizar ferramentas compatíveis com a versão identificada.
3. Priorizar recuperação de código Python 2.7 quando a origem corresponder a Python 2.7.
4. Suportar outros formatos de bytecode através de módulos específicos.
5. Recuperar imports, classes, funções e constantes quando possível.
6. Preservar nomes de módulos e estrutura dos packages.
7. Validar sintaticamente o código recuperado com um parser compatível.
8. Identificar descompilações parciais ou inválidas.
9. Permitir tentativas alternativas sem perder os resultados anteriores.

**Importante:** Não converter indiscriminadamente bytecode moderno para Python 2.7. Quando a equivalência não for possível, produzir uma representação de análise ou um stub, identificando claramente a limitação.

### Estados de processamento

- `success`: descompilação concluída e validada.
- `partial`: recuperação parcial.
- `failed`: descompilação não conseguida.
- `unsupported`: formato ou bytecode não suportado.
- `unchanged`: ficheiro previamente processado sem alterações.
- `extracted`: ficheiro extraído sem necessidade de descompilação.

Cada falha deverá incluir uma mensagem técnica para facilitar a depuração.

---

## 6. ActionScript e Scaleform

Criar um módulo dedicado aos recursos `.swf`.

Deverá:

- Identificar e catalogar ficheiros SWF.
- Extrair recursos incorporados quando possível.
- Identificar versões ActionScript.
- Recuperar código ActionScript quando suportado.
- Preservar imagens, fontes e outros elementos incorporados.
- Manter os caminhos de origem.
- Produzir relatórios de ficheiros não recuperáveis.

A reconstrução deve distinguir código descompilado de recursos simplesmente extraídos.

---

## 7. Gameface

Desenvolver um módulo especializado na identificação e recuperação dos recursos Gameface utilizados pelo World of Tanks.

### Funcionalidades

- Localização automática de recursos Gameface.
- Recuperação de ficheiros HTML, CSS e JavaScript.
- Identificação de bundles JavaScript.
- Preservação de assets e manifests.
- Identificação de componentes de interface.
- Análise de dependências internas.
- Formatação de código JavaScript minificado, quando possível.
- Identificação das ligações entre recursos Gameface e módulos Python.

**Não tratar a formatação de JavaScript minificado como recuperação integral do código-fonte original.**

O sistema deverá documentar os módulos e interfaces identificados para apoiar o desenvolvimento de mods Gameface.

---

## 8. Geração de stubs

Implementar um gerador automático de stubs Python (`.pyi`).

### Objetivos

- Melhorar o autocompletar no VS Code e noutras IDEs.
- Identificar classes e métodos.
- Recuperar parâmetros e assinaturas quando possível.
- Mapear imports e dependências.
- Documentar APIs internas do jogo.
- Gerar representações de módulos nativos sem código-fonte disponível.

Os stubs devem ser derivados de informação verificável, sem inventar assinaturas, tipos ou comportamentos.

---

## 9. Sistema de versões e atualizações

Cada realm deverá conter um ficheiro `.version_name` com a versão do cliente.

Criar um manifesto com:

- Realm.
- Versão do jogo.
- Data da extração.
- Caminho da instalação.
- Número de ficheiros encontrados.
- Número de ficheiros processados.
- Número de sucessos e falhas.
- Hashes dos ficheiros.
- Versões das ferramentas utilizadas.

### Extração incremental

Quando existir uma atualização do jogo:

1. Verificar a versão instalada.
2. Comparar o manifesto anterior.
3. Identificar ficheiros novos, alterados e removidos.
4. Reprocessar apenas os ficheiros necessários.
5. Preservar os relatórios anteriores.
6. Atualizar a versão apenas após uma execução consistente.

Não apagar automaticamente resultados anteriores em caso de falha.

---

## 10. Interface de linha de comandos

Criar uma CLI com operações semelhantes a:

```powershell
wot-extractor detect
wot-extractor extract --realm EU
wot-extractor extract --realm CT
wot-extractor decompile --realm EU
wot-extractor gameface --realm EU
wot-extractor actionscript --realm EU
wot-extractor stubs --realm EU
wot-extractor update --realm EU
wot-extractor verify --realm EU
wot-extractor report --realm EU
```

Os comandos apresentados definem a interface pretendida e deverão ser implementados, não considerados existentes.

Adicionar opções para processamento paralelo, filtragem por extensão, execução de diagnóstico e recuperação de operações interrompidas.

---

## 11. Qualidade e validação

Implementar testes automáticos para:

- Deteção das instalações.
- Identificação das versões.
- Extração de arquivos.
- Descompilação de bytecode suportado.
- Validação de código Python recuperado.
- Preservação de caminhos relativos.
- Integridade dos recursos binários.
- Processamento incremental.
- Recuperação após falhas.
- Segurança no tratamento de ficheiros.

Produzir relatórios em JSON e um resumo legível no terminal.

Não considerar uma execução bem-sucedida apenas porque o processo terminou sem exceções. É necessário verificar os resultados efetivamente produzidos.

---

## 12. Metodologia de desenvolvimento

Antes de implementar alterações:

1. Inspecionar o projeto existente, caso esteja disponível.
2. Identificar ferramentas e scripts já implementados.
3. Reutilizar funcionalidades comprovadamente operacionais.
4. Identificar limitações dos descompiladores existentes.
5. Definir uma arquitetura modular.
6. Implementar por etapas, começando pela deteção e extração.
7. Executar testes antes de avançar para a etapa seguinte.
8. Documentar decisões técnicas, erros e limitações.

Não reescrever componentes funcionais sem justificação técnica.

### Resultado esperado

Uma solução de extração e engenharia inversa que permita manter duas árvores de fontes independentes, `wot_src_EU` e `wot_src_CT`, preparadas para análise, pesquisa de APIs, desenvolvimento de mods Python e criação de interfaces Gameface.

A solução deverá distinguir rigorosamente os ficheiros originais, os recursos extraídos, o código descompilado, os stubs e os resultados apenas parcialmente recuperados.

Ferramenta de extração py3