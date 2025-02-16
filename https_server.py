import http.server
import ssl

class MeuManipulador(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <html>
        <head><title>Servidor HTTPS</title></head>
        <body><h1>Bem-vindo ao servidor seguro!</h1></body>
        </html>
        """
        self.wfile.write(html.encode())

# Configuração do endereço do servidor
server_address = ('localhost', 4443)

# Criando um servidor HTTP simples
httpd = http.server.HTTPServer(server_address, MeuManipulador)

# Criando contexto SSL seguro
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Envelopando o socket com SSL (método atualizado)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Servidor HTTPS rodando em https://localhost:4443")
httpd.serve_forever()
