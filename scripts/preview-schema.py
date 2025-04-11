#!/bin/uv run
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "PyYAML",
# ]
# ///
import http.server
import socketserver
import json
import yaml
from pathlib import Path
import urllib.parse
from typing import Any


class OpenAPIHandler(http.server.SimpleHTTPRequestHandler):
    # HTML 模板
    BASE_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{ font-family: system-ui, -apple-system, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; }}
            .nav {{ display: flex; gap: 1rem; margin: 2rem 0; }}
            .nav a {{
                padding: 0.5rem 1rem;
                text-decoration: none;
                color: #333;
                border: 1px solid #ddd;
                border-radius: 4px;
                transition: all 0.2s;
            }}
            .nav a:hover {{ background: #f5f5f5; }}
            {extra_styles}
        </style>
        {extra_head}
    </head>
    <body>
        {body}
    </body>
    </html>
    """

    API_ROUTES: dict[str, dict[str, str]] = {}

    for p in Path("schema").glob("*.yaml"):
        schema_name = p.stem
        cat, lang = schema_name.split(".")
        API_ROUTES[f"/{cat}/{lang}"] = {"title": f"Dify {cat} API ({lang})", "spec_path": str(p), "api_path": f"/{lang}/{cat}-api"}

    def send_html_response(self, content: str) -> None:
        """发送 HTML 响应"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

    def send_json_response(self, data: dict[str, Any]) -> None:
        """发送 JSON 响应"""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def load_yaml_spec(self, file_path: str) -> dict[str, Any] | None:
        """加载 YAML 规范文件"""
        try:
            return yaml.safe_load(Path(file_path).read_text(encoding="utf-8"))
        except Exception as e:
            self.send_error(500, str(e))
            return None

    def render_home_page(self) -> None:
        """渲染首页"""
        nav_links = "\n".join(f'<a href="{path}">{route["title"]}</a>' for path, route in self.API_ROUTES.items())

        content = self.BASE_TEMPLATE.format(
            title="Dify API 文档",
            extra_styles="",
            extra_head="",
            body=f"""
                <h1>Dify API 文档</h1>
                <div class="nav">
                    {nav_links}
                </div>
            """,
        )
        self.send_html_response(content)

    def render_api_page(self, route_info: dict[str, str]) -> None:
        """渲染 API 文档页面"""
        content = self.BASE_TEMPLATE.format(
            title=route_info["title"],
            extra_styles="""
                .topbar { display: none; }
                .nav { padding: 1rem; background: #f5f5f5; }
                .nav a { margin-right: 1rem; }
                .nav a:hover { text-decoration: underline; }
            """,
            extra_head="""
                <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
                <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
            """,
            body=f"""
                <div class="nav">
                    <a href="/">← 返回首页</a>
                </div>
                <div id="swagger-ui"></div>
                <script>
                    window.onload = function() {{
                        SwaggerUIBundle({{
                            url: "{route_info["api_path"]}",
                            dom_id: '#swagger-ui',
                            presets: [
                                SwaggerUIBundle.presets.apis,
                                SwaggerUIBundle.SwaggerUIStandalonePreset
                            ],
                        }})
                    }}
                </script>
            """,
        )
        self.send_html_response(content)

    def do_GET(self):
        """处理 GET 请求"""
        path = urllib.parse.urlparse(self.path).path

        if path == "/":
            self.render_home_page()
            return

        # 处理 API 页面请求
        if path in self.API_ROUTES:
            self.render_api_page(self.API_ROUTES[path])
            return

        # 处理 API 规范请求
        for route_info in self.API_ROUTES.values():
            if path == route_info["api_path"]:
                spec = self.load_yaml_spec(route_info["spec_path"])
                if spec:
                    self.send_json_response(spec)
                return

        # 处理其他静态文件
        super().do_GET()


def main():
    PORT = 8124
    print(f"服务启动在 http://localhost:{PORT}")
    print(f"- 首页: http://localhost:{PORT}/")
    for path, route in OpenAPIHandler.API_ROUTES.items():
        print(f"- {route['title']}: http://localhost:{PORT}{path}")

    with socketserver.TCPServer(("", PORT), OpenAPIHandler) as httpd:
        try:
            print("按 Ctrl+C 停止服务器...")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n正在关闭服务器...")
            httpd.shutdown()
            print("服务器已关闭")


if __name__ == "__main__":
    main()
