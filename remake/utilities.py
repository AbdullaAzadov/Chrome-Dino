class BoxData:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        if self.name == '_l':
            return instance.__dict__['x']
        elif self.name == '_r':
            return instance.__dict__['x'] + instance.__dict__['w']
        elif self.name == '_u':
            return instance.__dict__['y']
        elif self.name == '_d':
            return instance.__dict__['y'] + instance.__dict__['h']