items = {}

print('저장 전 :', items)

items['name'] = '홍길동'
items['age']= 25

print('저장 후 :', items)
print('저장된 모든 요소 >>', items.items())
print('저장된 모든 요소 : 키만 추출>>', items.keys())
print('저장된 모든 요소 : 값만 추출>>', items.values())
print('저장된 모든 요소 : 값만 추출 --- list로 변환>>', list(items.values()))
