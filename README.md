# README - Servidor e Cliente HTTPS em Python

Este projeto demonstra a implementação de um servidor HTTPS simples em Python usando `http.server` e `ssl`, além de um cliente HTTPS para testar a conexão.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x** (Recomenda-se a versão mais recente)
- **Bibliotecas padrão do Python** (http.server, ssl, requests)
- **mkcert** (para gerar certificados SSL)

## Passo a Passo para Rodar o Projeto

### 1. Gerar Certificado SSL com mkcert

O servidor HTTPS requer um certificado SSL para operar.

Será enviado os arquivos de certificado que utilizei no código, garanta que eles estão no mesmo diretório dos arquivos do programa, caso esteja dando erro para a leitura do certificado, gere um novo.

Antes de seguir o passo a passo, é necessário ter instalado o Chocolatey, caso não tenha, acesse o site oficial e instale por lá.

&#x20;Para gerar um certificado autoassinado com `mkcert`, siga estes passos:

1. Instale o `mkcert` se ainda não o tiver:
   ```sh
   mkcert -install
   ```
2. Gere um certificado SSL para `localhost`:
   ```sh
   mkcert -key-file key.pem -cert-file cert.pem localhost 127.0.0.1
   ```

Após esse processo, dois arquivos serão gerados no diretório atual:

- `cert.pem` (Certificado SSL)
- `key.pem` (Chave privada)

### 2. Executar o Servidor HTTPS

Com o certificado gerado, podemos iniciar o servidor HTTPS:

1. No terminal, navegue até o diretório onde está o arquivo `https_server.py`.
2. Execute o seguinte comando:
   ```sh
   python https_server.py
   ```
3. O servidor será iniciado e estará disponível no endereço:
   ```
   https://localhost:4443
   ```

### 3. Executar o Cliente HTTPS

O cliente se conectará ao servidor e receberá a resposta HTML. Para rodá-lo:

1. No terminal, navegue até o diretório onde está o arquivo `https_client.py`.
2. Execute o seguinte comando:
   ```sh
   python https_client.py
   ```
3. A saída esperada será algo como:
   ```
   Resposta do servidor: <html><head><title>Servidor HTTPS</title></head><body><h1>Bem-vindo ao servidor seguro!</h1></body></html>
   ```

## Observações

- O cliente ignora a verificação do certificado (`verify=False`), pois estamos usando um certificado autoassinado. Para ambiente de produção, utilize certificados emitidos por uma Autoridade Certificadora (CA).
- O servidor usa a porta `4443`. Se desejar usar outra, modifique a variável `server_address` no `https_server.py`.

## Solução de Problemas

### 1. "ModuleNotFoundError: No module named 'requests'"

Se ocorrer esse erro ao rodar o cliente, instale a biblioteca `requests` com:

```sh
pip install requests
```

### 2. "Permission Denied" ao usar portas baixas (<1024)

Se quiser rodar o servidor em portas como `443`, pode ser necessário permissão de administrador. Execute:

```sh
sudo python https_server.py
```

---

Agora seu servidor HTTPS e cliente estão configurados e prontos para uso!

