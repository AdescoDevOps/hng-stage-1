from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Api is running"}

@app.get("/health")
def health():
    return {"message": "healthy"}

@app.get("/me")
def profile():
    return {
        "name": "Ojo Emmanuel",
        "email": "adescocloud@gmail.com",
        "github": "AdescoDevOps"
    }
