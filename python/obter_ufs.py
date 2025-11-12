#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AD3 - SOAP Web Service DataSUS
Chamada 1: ObterUFs
Retorna lista de Unidades Federativas disponíveis
"""

from zeep import Client
from zeep.transports import Transport
from requests import Session

def main():
    WSDL_URL = "http://paraiso.datasus.gov.br/cep/cep.asmx?WSDL"
    
    print("\n" + "="*70)
    print("ATIVIDADE DE APRENDIZAGEM A DISTÂNCIA 3 (AD3)")
    print("Web Service SOAP - DataSUS (CEPs)")
    print("="*70)
    print("\nCRIANDO CLIENTE SOAP...")
    print(f"URL WSDL: {WSDL_URL}")
    
    try:
        # Criar sessão com timeout
                        session = Session()
                                session.timeout = 30
                                                        transport = Transport(session=session)
                                                                client = Client(wsdl=WSDL_URL, transport=transport)
        
        print("\n✓ Cliente SOAP criado com sucesso!")
        print("\n" + "-"*70)
        print("CHAMADA 1: ObterUFs()")
        print("-"*70)
        
        resultado = client.service.ObterUFs()
        
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
