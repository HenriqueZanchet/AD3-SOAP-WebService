#!/bin/bash

echo "========================================"
echo "Executando testes SOAP - AD3"
echo "========================================"
echo ""

echo "Aguardando instalção da biblioteca zeep..."
pip install zeep -q

echo "\n================ TESTE 1 ================"
echo "Executando: ObterUFs"
echo "========================================\n"

python3 python/obter_ufs.py | tee prints/resultado_obter_ufs.txt

echo "\n\n================ TESTE 2 ================"
echo "Executando: ObterEnderecoPorCEP"
echo "========================================\n"

python3 python/obter_endereco_por_cep.py | tee prints/resultado_obter_endereco_por_cep.txt

echo "\n========================================"
echo "Testes SOAP concluídos com sucesso!"
echo "========================================"
echo ""
echo "Arquivos de resultado salvos em:"
echo "  - prints/resultado_obter_ufs.txt"
echo "  - prints/resultado_obter_endereco_por_cep.txt"
echo ""
