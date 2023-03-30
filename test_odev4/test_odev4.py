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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest


class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 
    
    def teardown_method(self):
        self.driver.quit()

    def test_empty_all(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_all.png") 
        assert errorMessage.text == "Epic sadface: Username is required"
    
    def test_empty_pass(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_pass.png") 
        assert errorMessage.text == "Epic sadface: Password is required"


    def test_locked_user(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce") 
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_user.png") 
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_empty_caution(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"error-button")))
        errorIcon = self.driver.find_element(By.CLASS_NAME,"error-button")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_caution.png") 
        errorIcon.click()
       

    def test_standart(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test_standart.png")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
       
    def test_product(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        numberOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test_product.png")
        assert len(numberOfProducts) == 6

    @pytest.mark.parametrize("fn,ln,pc",[("Ahmet","Dere","22100"),("Deren","Saat","23652"),("Mehmet","Dar","45896")])
    def test_checkout_success(self,fn,ln,pc):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        productBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        productBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        cartBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        cartBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstName = self.driver.find_element(By.ID,"first-name")
        lastName = self.driver.find_element(By.ID,"last-name")
        postalCode = self.driver.find_element(By.ID,"postal-code")
        continueBtn = self.driver.find_element(By.ID,"continue")
        firstName.send_keys(fn)
        lastName.send_keys(ln)
        postalCode.send_keys(pc)
        continueBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout.png")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    
    @pytest.mark.parametrize("fn,ln,pc",[("","Dere","22100"),("","Saat","23652"),("","Dar","45896")])
    def test_checkout_empty_name(self,fn,ln,pc):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        productBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        productBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        cartBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        cartBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstName = self.driver.find_element(By.ID,"first-name")
        lastName = self.driver.find_element(By.ID,"last-name")
        postalCode = self.driver.find_element(By.ID,"postal-code")
        continueBtn = self.driver.find_element(By.ID,"continue")
        firstName.send_keys(fn)
        lastName.send_keys(ln)
        postalCode.send_keys(pc)
        continueBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout_empty_name.png")
        assert errorMessage.text == "Error: First Name is required"

    @pytest.mark.parametrize("fn,ln,pc",[("Ahmet","","22100"),("Deren","","23652"),("Mehmet","","45896")])
    def test_checkout_empty_lastName(self,fn,ln,pc):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        productBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        productBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        cartBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        cartBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        firstName = self.driver.find_element(By.ID,"first-name")
        lastName = self.driver.find_element(By.ID,"last-name")
        postalCode = self.driver.find_element(By.ID,"postal-code")
        continueBtn = self.driver.find_element(By.ID,"continue")
        firstName.send_keys(fn)
        lastName.send_keys(ln)
        postalCode.send_keys(pc)
        continueBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout_empty_lastName.png")
        assert errorMessage.text == "Error: Last Name is required"