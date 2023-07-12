import pyautogui as pg
import time
pg.press('enter')
time.sleep(1)
pg.leftClick(1088,325,1,1)
time.sleep(1)

for i in range(100):
    pg.typewrite('xin lỗi')
    time.sleep(1)
    pg.press('enter')
print('done')
 











