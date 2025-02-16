import requests

# Ignorar verificação SSL (apenas para testes)
response = requests.get("https://localhost:4443", verify=False)

# Exibir o conteúdo da resposta
print("Resposta do servidor:", response.text)
