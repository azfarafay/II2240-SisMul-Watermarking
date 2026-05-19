import cv2

def compress_jpeg(image, quality_factor):

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality_factor]
    
    _, encimg = cv2.imencode('.jpg', image, encode_param)
    
    decimg = cv2.imdecode(encimg, cv2.IMREAD_GRAYSCALE)
    return decimg