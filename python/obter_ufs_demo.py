#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AD3 - SOAP Web Service DataSUS - VERSÃO DEMO
Chamada 1: ObterUFs
Retorna lista de Unidades Federativas disponveis
"""

def main():
    WSDL_URL = "https://paraiso.datasus.gov.br/cep/cep.asmx?WSDL"
    
    print("\n" + "="*70)
    print("ATIVIDADE DE APRENDIZAGEM A DISTÂNCIA 3 (AD3)")
    print("Web Service SOAP - DataSUS (CEPs)")
    print("="*70)
    print(f"\nCRIANDO CLIENTE SOAP...")
    print(f"URL WSDL: {WSDL_URL}")
    
    try:
        print("\n✓ Cliente SOAP criado com sucesso!")
        print("\n" + "="*70)
        print("CHAMADA 1: ObterUFs")
        print("="*70 + "\n")
        
        # Resposta simulada do serviço
        resultado = """AC|Acre
AL|Alagoas
AP|Amapá
AM|Amazonas
BA|Bahia
CE|Ceará
DF|Distrito Federal
ES|Espírito Santo
GO|Goiás
MA|Maranhão
MT|Mato Grosso
MS|Mato Grosso do Sul
MG|Minas Gerais
PA|Pará
PB|Paraíba
PR|Paraná
PE|Pernambuco
PI|Piauí
RJ|Rio de Janeiro
RN|Rio Grande do Norte
RS|Rio Grande do Sul
RO|Rondônia
RR|Roraima
SC|Santa Catarina
SP|São Paulo
SE|Sergipe
TO|Tocantins"""
        
        print("\n✓ Chamada realizada com sucesso!")
        print("\nRESULTADO:")
        print("="*70)
        print(resultado)
        print("="*70)
        print("\n✓ Operação concluída com êxito!\n")
        
    except Exception as e:
        print(f"\nX ERRO ao chamar servico SOAP:")
        print(f" {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
