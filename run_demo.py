import cv2
import matplotlib.pyplot as plt
from dctwatermark.embed import embed_watermark_dct, extract_watermark_dct
from dctwatermark.jpeg import compress_jpeg

def main():
    print("[INFO] Memuat gambar...")
    host = cv2.imread('wajah.jpg', cv2.IMREAD_GRAYSCALE)
    wm = cv2.imread('watermark.png', cv2.IMREAD_GRAYSCALE)

    if host is None or wm is None:
        print("Error: File 'wajah.jpg' atau 'watermark.png' tidak ditemukan di folder ini.")
        return

    alpha_val = 20.0 

    print("[INFO] Menyisipkan watermark menggunakan DCT...")
    watermarked = embed_watermark_dct(host, wm, alpha=alpha_val)

    cv2.imwrite('watermarked_lossless.png', watermarked)

    qf_list = [100, 90, 70, 50, 20]
    hasil_ekstraksi = []

    print("[INFO] Melakukan evaluasi kompresi JPEG...")
    for qf in qf_list:
        compressed_img = compress_jpeg(watermarked, qf)

        extracted_wm = extract_watermark_dct(compressed_img, host, alpha=alpha_val)
        hasil_ekstraksi.append((qf, extracted_wm))

        cv2.imwrite(f'eval_QF_{qf}.jpg', compressed_img)

    print("[INFO] Menampilkan hasil evaluasi...")
    plt.figure(figsize=(15, 4))
    for i, (qf, ext_wm) in enumerate(hasil_ekstraksi):
        plt.subplot(1, len(qf_list), i+1)
        plt.imshow(ext_wm, cmap='gray')
        plt.title(f'Ekstraksi QF = {qf}')
        plt.axis('off')
        
    plt.suptitle('Evaluasi Ekstraksi Watermark DCT terhadap Kompresi JPEG')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()