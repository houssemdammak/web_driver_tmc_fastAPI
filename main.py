from fastapi import FastAPI
from webdriver_tmc import run_tmc_task
import threading

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API Talend WebDriver prête"}

@app.post("/run-tmc-task")
def lancer_task():
    thread = threading.Thread(target=run_tmc_task)
    thread.start()
    return {"status": "Tâche déclenchée dans un thread"}
