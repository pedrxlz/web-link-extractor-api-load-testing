import json
import os
import ssl
import sys
from urllib.parse import urljoin

import redis
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)
redis_conn = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
use_cache = os.getenv("USE_CACHE", "false").lower() == "true"

# Cria um contexto SSL que permite a renegociação legada
ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_LEGACY_SERVER_CONNECT

def extract_links(url):
    try:
        # Faz a requisição com a verificação SSL desativada
        res = requests.get(url, verify=False)  # A desativação da verificação SSL é temporária
        soup = BeautifulSoup(res.text, "html.parser")
        base = url
        # TODO: Update base if a <base> element is present with the href attribute
        links = []
        for link in soup.find_all("a"):
            links.append({
                "text": " ".join(link.text.split()) or "[IMG]",
                "href": urljoin(base, link.get("href"))
            })
        return links
    except requests.exceptions.SSLError as e:
        print(f"Erro SSL: {e}")
        return []

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<port>]/api/<url>"

@app.route("/api/<path:url>")
def api(url):
    qs = request.query_string.decode("utf-8")
    if qs != "":
        url += "?" + qs

    jsonlinks = None
    if use_cache:
        jsonlinks = redis_conn.get(url)

    if not jsonlinks:
        links = extract_links(url)
        jsonlinks = json.dumps(links, indent=2)
        if use_cache:
            redis_conn.set(url, jsonlinks)

    response = app.response_class(
        status=200,
        mimetype="application/json",
        response=jsonlinks
    )

    return response

if __name__ == "__main__":
    if len(sys.argv) == 2:
        for link in extract_links(sys.argv[-1]):
            print("[{}]({})".format(link["text"], link["href"]))
    else:
        app.run(host="0.0.0.0")
