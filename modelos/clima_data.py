class ClimaData:
    """
    Clase para almacenar datos meteorológicos encriptados.
    """
    def __init__(self, encrypted_data):
        if not isinstance(encrypted_data, str):
            raise ValueError("encrypted_data debe ser una cadena.")
        self._encrypted_data = encrypted_data
        self._next = None

    @property
    def encrypted_data(self):
        return self._encrypted_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if not isinstance(value, ClimaData) and value is not None:
            raise ValueError("next debe ser una instancia de ClimaData o None.")
        self._next = value
