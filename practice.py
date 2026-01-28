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


# class PlusMinus:
#     # def data(self, first, second):
#     #     self.first = first
#     #     self.second = second
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def plus(self):
#         return self.first + self.second

#     def minus(self):
#         return self.first - self.second


# a = PlusMinus(5, 3)

# b = PlusMinus(7, 1)

# print(a.first, b.second)


# print(a.plus())
# print(b.minus())


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        result = self.price + other.price
        return result

    def __str__(self):
        return f'{self.name}의 가격은 {self.price}입니다.'


kia = Car('k8', 300)
bmw = Car('m5', 500)
print(kia + bmw)
print(kia)
