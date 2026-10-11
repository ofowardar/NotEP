from fastapi import FastAPI 


app = FastAPI()

@app.get("/")
def root_check():
    return {"message":"Root Check Worked!"}
