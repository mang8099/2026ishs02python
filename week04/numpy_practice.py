import numpy as np

#numpy 리스트 형성-가장 큰 타입으로 통일
np_array = np.array([3,'2',1.7])
print(np_array, type(np_array))

#파이썬 리스트 형성-서로다른 타입이 들어감
list_array = [3,'2',1.7]
print(list_array, type(list_array))

array01 = np.zeros((2,3))
array02 = np.ones((2,3))
array03 = np.arange(1,11,2)
array04 = np.arange(5)
array05 = np.linspace(0,1,5)

print(array01.shape) #배열 모양(행,열)
print(array02.shape)
print(array03.ndim)#차원수
print(array04.dtype)#데이터 타입
print(array05.size)#전체 원소 개수
print(array05.size)
array01 = np.zeros((3, 4))
print(array01)
print(array01.size)
array01[2, 1] = 7.0
array01[1, 2] = 12.0
print(array01[1:,[1,2]])
print(array01[array01 <= 7])
print(array01[1:,[1]])

array01 = np.zeros((3, 4))
array02 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
array01[0,0] = 7
print(array01 + array02)
print(array01 + 0.4)
print(np.sum(array01))
print(np.min(array02))