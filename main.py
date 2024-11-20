import cv2
import pyautogui
import numpy as np
import time


#monitor_widht=1920.0 #kullanıcan alınacak
#monitor_heiht=1080.0 #kullanıcıdan alınacak

template_path = r"C:\Users\basba\Desktop\leg\file.jpg" #skala alınacak resim
template = cv2.imread(template_path, 0)
w, h = template.shape[::-1]  
def ObjectRecognition():
    i=0
    while True:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)  
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)  #hız
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7  #eşleşme oranı
        loc = np.where(res >= threshold)
    
        for pt in zip(*loc[::-1]):  # Koordinatları ters çevirdik çünkü OpenCV (x, y) formatı kullanır
            w, h = template.shape[::-1]  
            print("buldu")
            a=int(pt[0])
            b=int(pt[1])
            w=int(w*2)#Skala aldığımız resime göre genel boyut farkı ayarlama
            #Eğer skala aldığımız veri çok küçük ise veri kaybına sebep olabilir.
            h=int(h*2)
            i=i+1
            
            screenshot = pyautogui.screenshot(region=(a,b,w,h))
            screenshot.save(f"aq{i}.png")
            ##Dosya varmı yokmu kontrol edilcek
            ##Dosya dizini verilecek
            
                
            break
        time.sleep(1)#ekran değişikliğine göre ayarlanacak
            


        



    



if __name__ == '__main__':
    ObjectRecognition()