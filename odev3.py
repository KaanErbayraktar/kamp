# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

# Test Caseler;

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_empty_all(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        loginBtn = driver.find_element(By.NAME,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST: {testResult}")

    def test_empty_pass(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        username = driver.find_element(By.NAME,"user-name")
        loginBtn = driver.find_element(By.NAME,"login-button")
        sleep(2)
        username.send_keys("standard_user")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST: {testResult}")

    def test_locked_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        username = driver.find_element(By.NAME,"user-name")
        password = driver.find_element(By.NAME,"password")
        loginBtn = driver.find_element(By.NAME,"login-button")
        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce") 
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST: {testResult}")

    def test_empty_caution(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        loginBtn = driver.find_element(By.NAME,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        crosses = driver.find_element(By.CLASS_NAME,"input_error form_input error")
        errorMessage_closeBtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        x = len(crosses)
        if x == 2:
            print("Error crosses checked.")
            errorMessage_closeBtn.click()
            username_cross = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg")
            password_cross = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg")
            y = len([username_cross,password_cross])
            sleep(2)
            if y == 0:
                print("Test is successful")
            else:
                print(False)
        else:
            print("Test is unsuccessful")

    def standart(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        username = driver.find_element(By.NAME,"user-name")
        password = driver.find_element(By.NAME,"password")
        loginBtn = driver.find_element(By.NAME,"login-button")
        sleep(2)
        username.send_keys("standard_user")
        password.send_keys("secret sauce")
        sleep(2)
        loginBtn.click()
        inventory = len(driver.find_element(By.CLASS_NAME,"inventory_item_name"))
        if inventory >0:
            print(True)
        else:
            print(False)



testClass = Test_Sauce()
testClass.standart()