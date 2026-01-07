from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析網址參數
        query = urlparse(self.path).query
        params = parse_qs(query)
        name = params.get('name', ['陌生人'])[0] # 如果沒傳名字，預設叫陌生人

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        response_text = f"你好 {name}！這是 Python 幫你算出的結果。"
        self.wfile.write(response_text.encode('utf-8'))
