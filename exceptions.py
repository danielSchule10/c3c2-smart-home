class DBExistsException(Exception):
    # Wird aktuell nicht genutzt – Reserve für spätere DB-Init Checks
    def __init__(self, message, errors):            
        super().__init__(message)
        self.errors = errors

class DeviceTypeNotFoundException(Exception):
    # Gerätetyp-ID existiert nicht
    def __init__(self, message, errors):
        super().__init__(message)
    
class DeviceNotFoundException(Exception):
    # Gerät (Pin) nicht gefunden
    def __init__(self, message, errors):
        super().__init__(message)
    