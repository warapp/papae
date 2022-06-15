from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/re_sistor")
async def re_sistor(r1,r2,r3):
    parallel = (f'Parallel = {float(r1)+float(r2)+float(r3):.2f}')
    serial = (f'serial = {1/float(r1)+1/float(r2)+1/float(r3)**-1:.2f}')
    return serial,parallel 

@app.get("/samesame")
def samakan(s,t):
    data = (f'V = {float(s)/float(t):.2f}')
    return data 

@app.get("/")
def read_root():
    return{"Hello":"world"}

@app.get("/my_name")
def my_name():
    data = "waraphon chamnongphean"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name,last_name):
    data = "{} {}".format(name,last_name)
    return data


if __name__ =="__main__":
    uvicorn.run(app,host="192.168.90.210",port=8000)

print("Hello pea")