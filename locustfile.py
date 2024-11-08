import random

from locust import HttpUser, between, task

URLs = [
    "https://www.globo.com/",
    "https://www.uol.com.br/",
    "https://news.yahoo.com/",
    "https://www.r7.com/",
    "https://www.estadao.com.br/",
    "https://www.folha.uol.com.br/",
    "https://www.terra.com.br/noticias/",
    "https://g1.globo.com/",
    "https://www.bbc.com/portuguese",
    "https://www.cnnbrasil.com.br/",
]

class LinkExtractorUser(HttpUser):
    wait_time = between(1, 2)  

    @task
    def extract_links(self):
        url = random.choice(URLs)  
        self.client.get("/", params={"url": url})