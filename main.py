import http.server
import socketserver

# Номер порта, на котором будет работать сервер
PORT = 8000


# Создаем класс обработчика запросов, наследуясь от SimpleHTTPRequestHandler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Отправляем ответ с кодом 200 (успешно)
        self.send_response(200)
        # Устанавливаем заголовок Content-type
        self.send_header('Content-type', 'text/plain')
        # Завершаем отправку заголовков
        self.end_headers()
        # Отправляем текстовое сообщение
        self.wfile.write(b'Hello, World wide web!')


def start_server(port):
    try:
        with socketserver.TCPServer(("", port), MyHandler) as httpd:
            print("serving at port", port)
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")
        print("Адрес уже используется или произошла другая ошибка. Проверьте номер порта и повторите попытку.")


if __name__ == "__main__":
    start_server(PORT)

# Проверка
# http://localhost:8000/
