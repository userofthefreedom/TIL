# # 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     pass


# # 2. get 메서드를 사용한 방법
# def dict_invert(input_dict):
#     pass


# # 3. defaultdict를 사용한 방법


# def dict_invert(input_dict):
#     pass


# print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
# print(
#     dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
# )  # {10: [1], 20: [2], 30: [3, 4]}
# print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}

class Plus_minus():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first + self.second
        return result

    def minus(self):
        result = self.first - self.second
        return result


class MoreFunction(Plus_minus):
    def __init__(self, first, second, third):
        super().__init__(first, second)
        self.third = third

    def mul(self):
        result = self.first * self.second * self.third
        return result


b = MoreFunction(3, 4, 5)
print(b.plus())
print(b.minus())
print(b.mul())
