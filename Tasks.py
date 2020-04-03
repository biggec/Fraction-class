def gcd(num1, num2):
    while num1 % num2 != 0:
        old1 = num1
        old2 = num2
        num1 = old2
        num2 = old1 % old2
    return num2


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.dem = bottom

    def __add__(self, other):
        new_num = self.num * other.dem + self.dem * other.num
        new_dem = self.dem * other.dem
        common = gcd(new_num, new_dem)
        return Fraction(new_num // common, new_dem // common)

    def __str__(self):
        return str(self.num) + '/' + str(self.dem)

    def __sub__(self, other):
        new_num = self.num * other.dem - self.dem * other.num
        new_dem = self.dem * other.dem
        common = gcd(new_num, new_dem)
        return Fraction(new_num // common, new_dem // common)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_dem = self.dem * other.dem
        common = gcd(new_num, new_dem)
        return Fraction(new_num // common, new_dem // common)

    def __truediv__(self, other):
        new_num = self.num * other.dem
        new_dem = self.dem * other.num
        common = gcd(new_num, new_dem)
        return Fraction(new_num // common, new_dem // common)

    def dec(self):
        return self.num / self.dem

    def get_num(self):
        return self.num

    def get_dem(self):
        return self.dem


f1 = Fraction(2, 4)
f2 = Fraction(1, 5)

print(f1.get_dem())
