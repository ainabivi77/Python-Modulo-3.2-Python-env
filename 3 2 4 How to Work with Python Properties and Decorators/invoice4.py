class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property #getters
    def client(self):
        return self._client

    @client.setter # anula nuestro client, google se anulará con Yahoo
    def client(self, client):
        self._client = client

    @property #getters
    def total(self):
        return self._total


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)
