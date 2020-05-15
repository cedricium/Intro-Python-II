class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return True if self.name == other else False

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '%s' % self.name

    def __repr__(self):
        return '%s' % self.name

    def on_take(self):
        print('You have picked up %s' % self.name)

    def on_drop(self):
        print('You have dropped %s' % self.name)


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("It's not smart to drop your light source!")
        super().on_drop()
