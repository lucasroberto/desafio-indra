import time

class Home:
    
    def __init__(self,driver):
        self.URL='https://www.americanas.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def selecionar_campo(self):
        self.driver.implicitly_wait(1)
        element = self.driver.find_element_by_id('btn-expanded')
        element.click()
        time.sleep(1)
        element1=self.driver.find_element_by_xpath('//*[@id="list-level-2"]/li[13]/a')
        element1.click()
    
    def entrar_email(self):
        email = self.driver.find_element_by_id('email')
        email.send_keys('a@gmail.com')
        email2 = self.driver.find_element_by_id('mgmEmail')
        email2.send_keys('a222@gmail.com')
        
    
    def entrar(self):
        self.driver.find_element_by_xpath('//*[@id="main-top"]/div[3]/div/div/form/div/div[2]/div/div[3]/button/div').click()

    