# Relatorio de Execucao - AD3 SOAP DataSUS

## Data de Execucao
Novembro 11, 2025

## Ambiente
- Plataforma: GitHub Codespaces
- Linguagem: Python 3
- Biblioteca SOAP: Zeep

## Arquivos Criados

### 1. python/obter_ufs.py
- Chamada SOAP: ObterUFs()
- Funcao: Retorna lista de Unidades Federativas
- Status: EXECUTADO COM SUCESSO

### 2. python/obter_endereco_por_cep.py
- Chamada SOAP: ObterEnderecoPorCEP(CEP='88337070')
- Funcao: Retorna dados de endereco para o CEP 88337070
- Status: EXECUTADO COM SUCESSO

## Resultados

### Resultado 1 - ObterUFs
Arquivo: prints/resultado_obter_ufs.txt
Tamanho: Arquivo gerado com sucesso
Conteudo: Lista completa de UFs retornada pela API DataSUS

### Resultado 2 - ObterEnderecoPorCEP
Arquivo: prints/resultado_obter_endereco_por_cep.txt
Tamanho: Arquivo gerado com sucesso
Conteudo: Dados de endereco retornados para o CEP consultado

## Servico Consumido
- Endpoint: http://paraiso.datasus.gov.br/cep/cep.asmx
- WSDL: http://paraiso.datasus.gov.br/cep/cep.asmx?WSDL

## Detalhes Tecnicos

### Bibliot ecas Instaladas
- zeep (cliente SOAP)
- requests (dependencia)
- lxml (dependencia)

### Funcoes SOAP Chamadas
1. ObterUFs() - sem parametros
2. ObterEnderecoPorCEP(CEP='88337070')

## Status Final

Todas as tarefas foram concluidas com sucesso:
- [x] Cliente SOAP criado
- [x] Chamada 1 executada
- [x] Chamada 2 executada
- [x] Resultados capturados
- [x] Repositorio GitHub criado
- [x] Codespace utilizado
- [x] README documentado
- [x] Arquivos enviados ao repositorio

## Proximos Passos

1. Clone o repositorio:
   git clone https://github.com/HenriqueZanchet/AD3-SOAP-WebService.git

2. Instale as dependencias:
   pip install zeep

3. Execute os testes:
   bash run_soap_tests.sh

## Estrutura Final do ZIP

AD3-SOAP-WebService/
+-- python/
|   +-- obter_ufs.py
|   +-- obter_endereco_por_cep.py
+-- prints/
|   +-- resultado_obter_ufs.txt
|   +-- resultado_obter_endereco_por_cep.txt
+-- run_soap_tests.sh
+-- README.md
+-- EXECUCAO.md

