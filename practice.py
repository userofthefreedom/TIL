# import requests
# from pprint import pprint
# # url = 'https://fakestoreapi.com/carts'


# cityname = "Seul,KR"
# lat = 37.56
# lon = 126.97
# # type: ignore
# url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apkey}'
# data = requests.get(url).json()
# pprint(data)

# # type: ignore
# url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apkey}"
# jsn_resp = requests.get(url).json()
# description = jsn_resp['weather'][0]['description']
# print(f'날씨 설명 :{description}')

# ### 예 제 ###
# # 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
# from collections import defaultdict
# blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']
# """
# 실행 결과
# {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
# """


# # 1. [] 표기법을 사용한 방법
# def count_blood_types(blood_types):
#     blood_count = {}
#     for i in blood_types:
#         blood_count[i] = blood_types.count(i)
#     return blood_count


# # 2. get() 메서드를 사용한 방법
# def count_blood_types(blood_types):
#     blood_count = {}
#     for i in blood_types:
#         blood_count[i] = blood_count.get(i, 0) + 1
#     return blood_count


# # 3. defaultdict를 사용한 방법
# blood_count = defaultdict(int)


# def count_blood_types(blood_types):
#     for i in blood_types:
#         blood_count[i] += 1
#     return dict(blood_count)


# print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# # 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기


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
