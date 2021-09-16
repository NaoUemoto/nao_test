import configparser
import numpy as np
import math
import cv2
# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
# --------------------------------------------------
#元画像の仮置き
img = cv2.imread('./img.png') 
# --------------------------------------------------
#数字もらう
used_nozzles = config_ini.getint('Head','used_nozzles')
all_nozzles = config_ini.getint('Head','all_nozzles')
start_nozzle = config_ini.getint('Head','start_nozzle')
end_nozzle = config_ini.getint('Head','end_nozzle')
nozzle_resolution = config_ini.getint('Head','nozzle_resolution')

img_resolution_width = config_ini.getint('Image','img_resolution_width')
img_resolution_height = config_ini.getint('Image','img_resolution_height')

interlace = config_ini.getint('Scan','interlace')
opass = config_ini.getint('Scan','pass') #passどうした
feed_pix = config_ini.getint('Scan','feed_pix')
mask_filepath = config_ini.get('Scan','mask_filepath')
# --------------------------------------------------
#計算
ap_pix = feed_pix
feed_um = feed_pix * ( nozzle_resolution // interlace )
original_mask = np.loadtxt( mask_filepath , delimiter=',')
total_feed_num = math.ceil( img_resolution_height / feed_pix ) - 1  
original_img_size = img.shape
ap_um = ap_pix* ( nozzle_resolution // interlace)
# --------------------------------------------------
# 結果表示
print('ap_pix :', ap_pix , type(ap_pix))
print('feed_um :', feed_um , type(feed_um))
print('total_feed_num :', total_feed_num , type(total_feed_num))
print('original_img_size :', original_img_size , type(original_img_size))
print('ap_um :', ap_um , type(ap_um))
print('original_mask :\n', original_mask , type(original_mask)) #見にくいから最後