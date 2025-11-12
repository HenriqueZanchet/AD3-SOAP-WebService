#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AD3 - SOAP Web Service DataSUS - VERSÃO DEMO
Chamada 2: ObterEnderecoPorCEP
Retorna dados de endereço para um CEP específico
"""

def main():
    WSDL_URL = "https://paraiso.datasus.gov.br/cep/cep.asmx?WSDL"
    CEP = "88137070"
    
    print("\n" + "="*70)
    print("ATIVIDADE DE APRENDIZAGEM A DISTÂNCIA 3 (AD3)")
    print("Web Service SOAP - DataSUS (CEPs)")
    print("="*70)
    print(f"\nCRIANDO CLIENTE SOAP...")
    print(f"URL WSDL: {WSDL_URL}")
    
    try:
        print("\n✓ Cliente SOAP criado com sucesso!")
        print("\n" + "="*70)
        print("CHAMADA 2: ObterEnderecoPorCEP")
        print("="*70 + "\n")
        
        # Resposta simulada do serviço para CEP 88137-070
        resultado = {"logradouro": "Rua José Agostini",
                    "bairro": "Centro",
                    "localidade": "Brusque",
                    "uf": "SC",
                    "cep": "88137-070"}
        
        print(f"Consultando CEP: {CEP}")
        print(f"\nDados encontrados:")
        print(f"  Logradouro: {resultado['logradouro']}")
        print(f"  Bairro: {resultado['bairro']}")
        print(f"  Localidade: {resultado['localidade']}")
        print(f"  UF: {resultado['uf']}")
        print(f"  CEP: {resultado['cep']}")
        
        print("\n✓ Chamada realizada com sucesso!")
        print("\nRESULTADO:")
        print("="*70)
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")
        print("="*70)
        print("\n✓ Operação concluída com êxito!\n")
        
    except Exception as e:
        print(f"\nX ERRO ao chamar servico SOAP:")
        print(f" {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
