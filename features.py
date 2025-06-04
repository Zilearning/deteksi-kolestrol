from skimage.feature import local_binary_pattern
from PIL import Image
import numpy as np

def extract_features(image_path):
    try:
        img = Image.open(image_path).convert('L').resize((64, 64))
        fitur = np.array(img).flatten() / 255.0
        return fitur
    except Exception as e:
        raise RuntimeError(f"Error reading image {image_path}: {e}")

def extract_features_lbp(image_path):
    img = Image.open(image_path).convert('L').resize((64, 64))
    img_np = np.array(img)
    lbp = local_binary_pattern(img_np, P=8, R=1, method='uniform')
    n_bins = int(lbp.max() + 1)
    hist, _ = np.histogram(lbp.ravel(), bins=n_bins, range=(0, n_bins), density=True)
    return hist