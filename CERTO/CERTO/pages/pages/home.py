import time

class Home:
    
    def __init__(self,driver):
        self.URL='https://www.americanas.com.br/'
        self.driver = driver

    def go_home(self):
        self.driver.get(self.URL)

    def selecionar_moda(self):
        self.driver.implicitly_wait(1)
        element = self.driver.find_element_by_xpath('//*[@id="list-level-1"]/li[3]/a')
        element.click()
        element1 = self.driver.find_element_by_xpath('//*[@id="main-top"]/div[3]/div/div/div/div[2]/div[2]/div/div/a/div/div/picture/img')
        element1.click()
        ele = self.driver.find_element_by_xpath('//*[@id="content-top"]/div[2]/div/div/div/div[1]/div/div[3]/div/div/a')
        ele.click()
    
    def filtrar(self):
        refinar = self.driver.find_element_by_xpath('//*[@id="sort-bar"]/div/aside/div/div[3]/span/form/div/div/select')
        refinar.click()
        time.sleep(2)
        menor = self.driver.find_element_by_xpath('//*[@id="sort-bar"]/div/aside/div/div[3]/span/form/div/div/select/option[1]')
        menor.click()
       
    
    

    