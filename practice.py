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

class Person:
    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value >= 0:
            self.__age = value


p = Person()
p.set_age(25)
print(p.get_age())  # 출력: 25
