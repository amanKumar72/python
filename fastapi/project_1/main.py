from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root_handler():
    return {"status": 'healthy', "message": "Server is working fine"}
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)