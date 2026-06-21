import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")         
options.add_argument("--no-sandbox")           
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--disable-gpu")            
options.add_argument("--window-size=1024,768")   

# Trỏ thẳng vào thư mục cài đặt Chrome của Docker
options.binary_location = "/usr/bin/google-chrome"

try:
    print("[RENDER] Khởi tạo Chrome Docker thành công!")
    driver = webdriver.Chrome(options=options)
    
    print("[RENDER] Đang kết nối tới trang web...")
    driver.get("https://gag.gg/vote/")
    time.sleep(5)
    
    # Cookie đăng nhập của bạn
    cookie_moi = {
        "name": "__Host-gag_session", 
        "value": "eyJzdWIiOiIxODA2Njg3Nzg5IiwibmFtZSI6Ik5OaGFuIiwidXNlcm5hbWUiOiJOaGFuX1ZuMiIsInBpY3R1cmUiOiJodHRwczovL3RyLnJieGNkbi5jb20vMzBEQVktQXZhdGFySGVhZHNob3QtNUFBMzY4QzIxNTZEN0FCNzM4MjUwMUQ2MTA0MDM4RTktUG5nLzE1MC8xNTAvQXZhdGFySGVhZHNob3QvUG5nL25vRmlsdGVyIiwiZXhwIjoxNzgyNjI1OTQ1fQ.Uab-ZrLp98BjWqhCbkCdAeU1982mGsXsPRIAqho9RpY",
        "path": "/",
        "secure": True
    }
    driver.delete_cookie("__Host-gag_session")
    driver.add_cookie(cookie_moi)
    print("[RENDER] Đã nạp cookie thành công.")
    
    driver.refresh()
    time.sleep(30)
    
    xpath_swipe_count = "/html/body/main/section/section/div[2]/header/div/span[21]"
    xpath_button_target = "/html/body/main/section/section/div[2]/div[2]/button[2]"
    xpath_gio = "/html/body/main/section/section/div[3]/div/div[5]/div/span[1]/b"
    xpath_phut = "/html/body/main/section/section/div[3]/div/div[5]/div/span[3]/b"
    xpath_giay = "/html/body/main/section/section/div[3]/div/div[5]/div/span[5]/b"
    xpath_nut_tro_lai = "ĐIỀN_FULL_XPATH_NÚT_TRỞ_LẠI_VÀO_ĐÂY"

    while True:
        print("\n🚀 Bắt đầu chu kỳ click mới...")
        vong_lap = 1
        
        while True:
            try:
                swipe_element = driver.find_element(By.XPATH, xpath_swipe_count)
                text_swipe = swipe_element.text.strip()
                if not text_swipe: break
                    
                print(f"[Lần {vong_lap}] Số lần swipe hiện tại: {text_swipe}")
                button_element = driver.find_element(By.XPATH, xpath_button_target)
                driver.execute_script("arguments[0].click();", button_element)
                
                vong_lap += 1
                time.sleep(2) 
            except Exception:
                break
        
        print("\n⏳ Chuyển sang chế độ theo dõi đồng hồ...")
        co_dong_ho = True
        while True:
            try:
                val_gio = driver.find_element(By.XPATH, xpath_gio).text.strip()
                val_phut = driver.find_element(By.XPATH, xpath_phut).text.strip()
                val_giay = driver.find_element(By.殘ATH, xpath_giay).text.strip()
                g, p, s = int(val_gio), int(val_phut), int(val_giay)
                print(f"\r⏰ Thời gian chờ: {g:02d}:{p:02d}:{s:02d}", end="", flush=True)
                if g == 0 and p == 0 and s == 0: break
                time.sleep(1)
            except:
                co_dong_ho = False
                break
        
        time.sleep(20)
        try:
            nut_back = driver.find_element(By.XPATH, xpath_nut_tro_lai)
            driver.execute_script("arguments[0].click();", nut_back)
        except:
            driver.refresh()
        time.sleep(5)

except Exception as e:
    print("[LỖI] Hệ thống:", e)
finally:
    try: driver.quit()
    except: pass
      
