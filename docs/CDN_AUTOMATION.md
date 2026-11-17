# Automacao de fontes a partir do CDN

Analise de 2026-11-17. Este documento e uma proposta; nao instala nem ativa automacao.

## Evidencia recolhida

- O projeto ja usa `wgus>=0.0.12` para consultar as versoes instaladas.
- Uma consulta real ao WGUS EU com os componentes em `0` devolveu a versao
  `2.4.1.5514`, um arquivo base dividido em volumes e patches incrementais.
- A cadeia `client` foi `0 -> 2.4.1.24080 -> 2.4.1.24087 -> 2.4.1.24091
  -> 2.4.1.24108 -> 2.4.1.24120`. A cadeia `sdcontent` tinha os seus proprios saltos.
  Nao se pode usar a versao visivel do jogo como versao de todos os componentes.
- Um pedido CDN `Range: bytes=0-31` ao arquivo de idioma retornou HTTP 206,
  `Content-Range` correto e a assinatura 7z `377abcaf271c`.
- A resposta XML inclui `parts_info` e `delay_preload=False`. O modelo da biblioteca
  local ignora esses campos e tambem nao preserva `version_from`.
  Isto nao basta para definir a semantica de pre-descarga ou de ativacao.
- O codigo publico de `unicum-gg/wot.build` implementa arquivos 7z divididos,
  leitura por intervalos, selecao de pacotes e aplicacao de `.xdiff`/`.rdiff`.
  Essa implementacao foi lida, mas nao executada nesta analise.

## Arquitetura recomendada

Adicionar um modo CDN independente do modo de instalacao local atual.
O jogo instalado permanece apenas como possivel origem de uma base inicial.

1. **Descobrir**: consultar metadados e cadeias por regiao, com timeout, repeticao
   limitada e suporte a redirecionamentos. Guardar XML original e um manifesto
   normalizado com host, GUID, idioma, componentes, versoes de origem/destino,
   URLs e tamanhos. Separar a versao candidata da versao ativa.
2. **Planear**: enumerar os arquivos remotos atraves do cabecalho 7z; identificar
   os blocos necessarios. Mostrar bytes a transferir antes de grandes descargas.
   Nao assumir que todos os arquivos sao nao solidos: verificar essa propriedade
   e calcular o custo por bloco de compressao, que pode conter varios ficheiros.
3. **Preparar**: descarregar os blocos selecionados e reconstruir os pacotes numa
   cache por regiao/componente/versao. Uma copia local so serve como base quando
   a sua versao e integridade correspondem ao patch. Aplicar deltas em ordem;
   uma substituicao integral elimina a necessidade dos deltas anteriores.
4. **Processar**: alimentar o extrator existente com uma arvore minima de
   recursos, incluindo os XML necessarios a detecao. Reutilizar os resultados
   apenas quando o hash de entrada e a versao/configuracao das ferramentas
   coincidirem. Remover resultados de ficheiros eliminados no novo cliente.
5. **Validar e publicar**: validar integridade e resultados antes de promover
   a arvore preparada. Escrever o marcador de versao apenas no fim. Commit
   identificado por versao e regiao; push sem force e com repeticao independente
   da extracao. Falhar o push nao pode impedir a tentativa seguinte.

## Pre-descargas e CT

A pre-descarga permite preparar e descompilar antecipadamente, numa arvore
separada. Disponibilidade de bytes nao prova que a versao ja esteja ativa.
No momento da ativacao, comparar novamente os manifestos e reconstruir apenas
os blocos alterados entre a pre-descarga e a versao final.

Falta observar uma resposta real com pre-descarga ativa para identificar a
representacao exata da cadeia candidata e o sinal de ativacao. Nao inventar
parametros como `preload=true` nem tratar `delay_preload` como data de lancamento.
Enquanto esse protocolo nao estiver validado, automatizar a versao corrente
anunciada pelo servico e manter candidatos sem promocao automatica.

Para CT, usar o mesmo motor de cadeias e downloads, sem exigir fase de
pre-descarga. Seguir o servidor indicado pelos metadados; nao fixar o host antigo.

## Selecao e custos

Para Python/AS3/Gameface, comecar pelos pacotes de scripts, GUI e modos de jogo.
Um espelho com XML de veiculos e outros dados tambem necessita de pacotes de
`sdcontent`. Nao reduzir a selecao a `scripts.pkg`: existem scripts nos modos.
Inventariar a cobertura do perfil atual antes de prometer equivalencia.

HTTP Range evita o download completo do volume de instalacao, mas nao garante
acesso individual a cada ficheiro dentro de um `.pkg` comprimido no arquivo
exterior. O custo minimo pode ser o pacote/bloco inteiro.

## Execucao

Recomenda-se inicialmente uma tarefa Windows com cache persistente, a cada
5 minutos, usando os decompiladores ja configurados. Um unico processo por
regiao, bloqueio atomico, recuperacao apos interrupcao e instalacao isolada das
dependencias. O PC tem de estar ligado; para disponibilidade permanente,
migrar depois para um servidor ou runner persistente.

O script atual verifica de hora a hora e o `auto` depende da instalacao local.
Os comentarios indicam ausencia de push, mas o codigo executa push. Corrigir
essa divergencia e separar preparacao, commit e envio antes de o reutilizar.

## Ordem de implementacao e criterios de aceitacao

1. Descoberta e planeamento sem downloads de grandes volumes; fixtures de XML
   real para cadeia integral/incremental, CT, redirecionamento e indisponibilidade.
2. Prova de conceito: reconstruir um pacote pequeno do CDN e comparar SHA-256
   com a mesma versao instalada; validar HTTP 206 e o intervalo/tamanho recebido.
3. Cache incremental e alimentacao da pipeline existente; uma segunda execucao
   nao deve voltar a descarregar/processar o que nao mudou.
4. Publicacao recuperavel e agendamento. Repetir apos falha de push sem nova
   extracao; nao publicar uma arvore parcial.
5. Pre-descarga, apos captura de uma janela real, incluindo mudanca do candidato
   antes do lancamento e confirmacao da ativacao por regiao.

## Fontes

- https://github.com/izeberg/wgus/blob/master/wgus/patches_chains.py
- https://github.com/unicum-gg/wot.build/blob/main/lib/wgus.ts
- https://github.com/unicum-gg/wot.build/blob/main/lib/archive.ts
- https://github.com/unicum-gg/wot.build/blob/main/lib/patched.ts
- https://github.com/unicum-gg/wot.build/blob/main/lib/delta.ts
- https://github.com/OpenKorabli/gc-download
- https://worldoftanks.eu/en/content/guide/account-and-game-settings/preloading-guide/

As fontes alternativas demonstram tecnicas; nao demonstram o funcionamento
interno do bot de izeberg. Verificar licencas antes de reutilizar codigo.
