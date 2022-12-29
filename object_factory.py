
class ObjectFactory:
    def __init__(self):
        self.m_builders = {}

    def register(self, key: str, builder):
        self.m_builders[key] = builder

    def create(self, key: str, **kwargs):
        builder = self.m_builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

