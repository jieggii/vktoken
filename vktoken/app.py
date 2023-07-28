from dataclasses import dataclass


@dataclass
class App:
    client_id: int
    client_secret: str

    def __init__(self, client_id: int, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
