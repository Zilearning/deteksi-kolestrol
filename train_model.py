import pandas as pd
import numpy as np
import os
from features import extract_features_lbp   # gunakan fungsi LBP
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load label dari CSV
df = pd.read_csv("data/label.csv")

X = []
y = []

for i, row in df.iterrows():
    image_path = os.path.join("data/raw", row["filename"])
    try:
        fitur = extract_features_lbp(image_path)  # GANTI ke LBP
        X.append(fitur)
        y.append(row["cholesterol"])
    except Exception as e:
        print(f"Gagal proses {row['filename']}: {e}")

X = np.array(X)
y = np.array(y)

# Latih model regresi sederhana
model = LinearRegression()
model.fit(X, y)

# Evaluasi model
y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
print(f"🩺 Mean Absolute Error (MAE): {mae:.2f}")

# Simpan model ke file
joblib.dump(model, "model.pkl")
print("✅ Model tersimpan di 'model.pkl'")
