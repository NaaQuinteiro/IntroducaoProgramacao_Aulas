import requests 

def get_infoByCEP(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    response = requests.get(url)

    dados = response.json()

    return f"{dados.get("logradouro")}, {dados.get("bairro")}, {dados.get("localidade")}, {dados.get("uf")}"


cep = int(input("Informe o seu cep: "))

print(f"Seu endereço é {get_infoByCEP(cep)}")