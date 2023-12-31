from src.base_classes.builder import BuilderBaseClass

from faker import Faker

fake = Faker()


class ItemTypeBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_item_type(self, item_type = fake.word()):
        self.result['item_type'] = item_type
        return self

    def reset(self):
        self.set_item_type()

    def build(self):
        return self.result
