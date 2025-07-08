from fastapi import FastAPI

## 1. FastAPI 앱 객체 생성
app = FastAPI()

## 2. get 요청 : index page
@app.get('/')
def index():
    return 'welcome'

## key : message
## value : hello
## json
## 3. get 요청
@app.get('/info')
def info():
    return {"message" : "hello"}

## 4. get 요청 : URL 경로 매개변수 사용
@app.get('/products/{id}')  ##id가 받은 값
def info_production(id: int): ##같아야함
    return f'상품번호 : {id}'

@app.get('/products/1')
def info_production():
    return f'상품번호 1입니다.'

@app.get('/products/2')
def info_production():
    return f'상품번호 2🍖입니다.'

## /hello/이름          응답:json    ##사용자가 요청한 URL기준
##                      key: name
##                      value: Hello,이름!
## 5. get 요청 : URL 경로 매개변수 사용
@app.get('/hello/{name}')
def greet_user_name(name: str):
    return {'name': f'Hello ,{name}!'}

## post 방식 - 서버 data 변경시
## http://127.0.0.1:8000/docs

## 6.post 요청 : JSON 데이터 받기
## get방식으로 요청하면 핸들러가 없어서 {"detail":"Method Not Allowed"}
## key : value
## 이름 : 홍길동
## 나이 : 25
from pydantic import BaseModel

# ## BaseModel : Json 데이터 받을 때 구조 정의
# class User(BaseModel): ## ()는 상속
#     userName : str
#     age : int

# @app.post('/user')
# def create_user(user : User): ## 클래스를 통해서 자동으로 객체 생성
#     # return '[post method] response'
#     print('user :', user)
#     print('userName :', user.userName)
#     print('age :', user.age)
#     return '[post method] response'

## post   /user         응답: json
##                      message : '사용자 정보가 등록되었습니다.
##                      user_info: 사용자 정보    
#                     
class User(BaseModel): ## ()는 상속
    userName : str
    age : int

@app.post('/user')
def create_user(user : User): ## 클래스를 통해서 자동으로 객체 생성
    # return '[post method] response'
    print('user :', user)
    print('userName :', user.userName)
    print('age :', user.age)
    return {
        'message':'사용자 정보가 등록되었습니다',
        'user_info': user
    }

## 상품 정보 저장
items = {}
## 사용자 모델 정의 #############################
## 상품 정보 : 상품 번호(itemID), 삼풍명(itemName), 가격(price)
## 

## Route : API
## 요청 URL: /item
## 요청 method: post

class Item(BaseModel):
    itemID : int ##변수
    itemName : str
    price : int

@app.post('/item')
def create_item(item : Item):
    print('[상품 등록 전]item >>',items)
    items[item.itemID]=item.model_dump()
    print('[상품 등록 후]item >>',items)
    # items[item.itemName]
    # items[item.price]
    # items = item.itemName
    # item.price
    
    # print('itemID',  item.itemID)
    # print('itemName', item.itemName)
    # print('price',  item.price)
    return {
        '[post] item 처리됨'
    }

## 전체 데이터 조회 ##############################
## 저장된 모든 상품의 정보를 리턴 : type list
## 요청 URL : /items
## 요청 method: get

@app.get('/items')
def det_items():
    return list(items.values())
    

    




#### www.naver.com/search?query=도메인
#### www.naver.com <- IP
#### 도메인
#### URL로 요청 get방식