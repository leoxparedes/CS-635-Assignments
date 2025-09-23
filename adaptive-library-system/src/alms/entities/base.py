 # Simple base class that gives every entity an identifier and a to_dict helper
class BaseEntity:

    def __init__(self, identifier):
        self._identifier = str(identifier)

    def get_id(self):
        return self._identifier

    def to_dict(self):
        return {"id": self._identifier}