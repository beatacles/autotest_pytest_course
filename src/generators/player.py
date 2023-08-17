from src.enums.user_enums import Statuses
from src.generators.player_localization import Player_localization


class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status = Statuses.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance = 0):
        self.result['balance'] = balance
        return self

    def set_avatar(self,
                   avatar = "https://w7.pngwing.com/pngs/340/946/png-transparent-avatar-user"
                            "-computer-icons-software-developer-avatar-child-face-heroes.png"):
        self.result['avatar'] = avatar
        return self

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if  item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result['localize'] = {
            'en': Player_localization('en_US').build(),
            'ru': Player_localization('ru_RU').build()
        }
        return self

    def build(self):
        return self.result
