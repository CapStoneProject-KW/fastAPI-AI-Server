from fastapi import FastAPI
from time import sleep
from pydantic import BaseModel

app = FastAPI()

class Path(BaseModel) :
    path : str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/ai/video")
async def analysing_Video(path: Path):
    # path를 통해 경로를 받아오기
    body = dict(path)
    # (AI모델이 영상을 처리하는 시간이라 가정)
    sleep(60)


    '''
    앞으로 해야할 API 로직
        1) AI 모델이 분석을 마치고 body로 받은 path 경로에 det,kpt,mot 결과를 저장
        2) 근데 그 중에서 det 결과는 바로 저장 받아야함 (인물 매칭 때문에)
        etc) det,kpt,mot 결과파일 저장할 때 이름 규칙 정해서 uuid + det.json 이런 식으로 node 서버에서도 접근하게 하자.
    '''

    var = body['path']
    print(var)

    return {"message": f"AI서버로부터 분석에 성공했습니다+{var}"}
