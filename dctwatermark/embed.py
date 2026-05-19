import cv2
import numpy as np
from .dct import apply_dct, apply_idct

def embed_watermark_dct(host_img, watermark_img, alpha=15.0):
    host_float = np.float32(host_img)

    wm_resized = cv2.resize(watermark_img, (host_img.shape[1], host_img.shape[0]))
    wm_float = np.float32(wm_resized) / 255.0 

    dct_host = apply_dct(host_float)

    dct_watermarked = dct_host + (alpha * wm_float)

    watermarked_float = apply_idct(dct_watermarked)
    watermarked_img = np.uint8(np.clip(watermarked_float, 0, 255))
    
    return watermarked_img

def extract_watermark_dct(watermarked_img, host_img, alpha=15.0):
    wm_float = np.float32(watermarked_img)
    host_float = np.float32(host_img)

    dct_wm = apply_dct(wm_float)
    dct_host = apply_dct(host_float)

    extracted = (dct_wm - dct_host) / alpha

    extracted_img = np.uint8(np.clip(extracted * 255.0, 0, 255))
    return extracted_img