from src.domain.validatorException import ValidatorException
from src.domain.client import Client


class ClientValidator:
    def __init__(self):
        self._errors = ""

    def client_validator(self, client):
        if not isinstance(client, Client):
            raise TypeError("Can only validate Client objects")

        self._errors = []
        if client.client_id is None:
            self._errors.append("Client must have an id")
        if client.name is None:
            self._errors.append("Client must have a name")

        if len(self._errors) > 0:
            raise ValidatorException(self._errors)
        return True
