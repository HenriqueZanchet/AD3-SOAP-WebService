#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AD3 - SOAP Web Service DataSUS
Chamada 2: ObterEnderecoPorCEP
Retorna dados de endereço para um CEP específíco
"""

from zeep import Client

def main():
    WSDL_URL = "http://paraiso.datasus.gov.br/cep/cep.asmx?WSDL"
    CEP = "88337070"
    
    print("\n" + "="*70)
    print("ATIVIDADE DE APRENDIZAGEM A DISTÂNCIA 3 (AD3)")
    print("Web Service SOAP - DataSUS (CEPs)")
    print("="*70)
    print(f"\nCRIANDO CLIENTE SOAP...")
    print(f"URL WSDL: {WSDL_URL}")
    
    try:
        client = Client(wsdl=WSDL_URL)
        
        print("\n✓ Cliente SOAP criado com sucesso!")
        print("\n" + "-"*70)
        print(f"CHAMADA 2: ObterEnderecoPorCEP(CEP='{CEP}')")
        print("-"*70)
        
        resultado = client.service.ObterEnderecoPorCEP(CEP=CEP)
        
        print("\n✓ Chamada realizada com sucesso!")
        print("\nRESULTADO:")
        print("-"*70)
        print(resultado)
        print("-"*70)
        
    except Exception as e:
        print(f"\n✗ ERRO ao chamar serviço SOAP:")
        print(f"  {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
