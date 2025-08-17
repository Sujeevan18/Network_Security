import os
import sys
import pandas as pd

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
load_dotenv()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.model.estimator import NetworkModel

app = FastAPI(title="Network Security - Inference API")

# CORS (adjust if you want to restrict origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"status": "ok", "message": "Network Security API running"}

@app.post("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response(content="Training is successful", media_type="text/plain")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        # Read CSV upload into DataFrame
        df = pd.read_csv(file.file)

        # Load preprocessor + model (already produced by your training pipeline)
        preprocessor = load_object("final_model/preprocessor.pkl")
        model = load_object("final_model/model.pkl")

        # Wrap in your combined estimator
        network_model = NetworkModel(preprocessor=preprocessor, model=model)

        # Predict
        y_pred = network_model.predict(df)
        df["predicted_column"] = y_pred

        # Persist prediction output (optional)
        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/output.csv", index=False)

        # Render HTML table
        table_html = df.to_html(classes="table table-striped", index=False)
        return templates.TemplateResponse("table.html", {"request": request, "table": table_html})

    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
