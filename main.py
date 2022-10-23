
class Gear:
    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    @property
    def chainring(self):
        return self.__chainring

    # セッターメソッドを使って不正な値を入れられないようにしている
    @chainring.setter
    def chainring(self, value):
        if value > 0:
            self.__chainring = value
        else:
            raise ValueError

    def ratio(self):
        return self.chainring / float(self.cog)


if __name__ == '__main__':
    gear = Gear(52, 11)
    gear.chainring = -30
    print(gear.ratio())
