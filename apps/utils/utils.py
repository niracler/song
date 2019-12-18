class CurrentUserDefault:
    def set_context(self, serializer_field):
        self.username = serializer_field.context['request'].myuser.username

    def __call__(self):
        return self.username

    def __repr__(self):
        return '%s()' % self.__class__.__name__
