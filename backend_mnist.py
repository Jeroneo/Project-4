from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import tensorflow as tf

app = FastAPI(title="MNIST Predictor API")
model = tf.keras.models.load_model('mnist_cnn.h5')

def center_and_preprocess(img_array):
    # Resize to 28x28
    img = cv2.resize(img_array, (28, 28), interpolation=cv2.INTER_AREA)
    # Normalize
    img = img / 255.0
    return img.reshape(1, 28, 28, 1)

@app.post("/predict")
async def predict_mnist(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    
    processed_img = center_and_preprocess(img)
    pred = model.predict(processed_img)
    digit = int(np.argmax(pred))
    
    return {"digit": digit, "confidence": float(np.max(pred))}

def improve_preprocess(img_array):
    # 1. Seuil pour avoir du noir et blanc pur
    _, thresh = cv2.threshold(img_array, 127, 255, cv2.THRESH_BINARY)
    
    # 2. Trouver les contours pour recadrer sur le chiffre
    coords = cv2.findNonZero(thresh)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        thresh = thresh[y:y+h, x:x+w] # On coupe le vide autour
    
    # 3. Replacer au centre d'un carré de 28x28
    # (On ajoute une petite bordure pour ressembler au vrai MNIST)
    res = cv2.resize(thresh, (20, 20)) # Le chiffre fait 20x20
    final_img = np.pad(res, ((4,4), (4,4)), mode='constant', constant_values=0)
    
    return final_img.reshape(1, 28, 28, 1) / 255.0