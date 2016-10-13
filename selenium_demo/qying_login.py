from selenium import webdriver
import time
import unittest
import HTMLTestRunner


class Viqyingtest(unittest.TestCase):

    def setUp(self):
        print('start setup')
        # __browser_url = r'C:\Users\YR\AppData\Roaming\qianying\Application\qianying.exe'  ##360浏览器的地址
        # chrome_options = Options()
        # chrome_options.binary_location = __browser_url

        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # browser_url = r'C:\Users\YR\AppData\Roaming\qianying\Application\qianying.exe'
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.binary_location = browser_url
        # self.driver = webdriver.Chrome(chrome_options=chromeOptions) 实在是找不到调用其他浏览器的方法了
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://v.iqying.com/")

    def test_search(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="serFrm"]/input[1]').send_keys("纸牌屋")  # 使用chrome的开发者工具进行定位
        driver.find_element_by_xpath('//*[@id="serFrm"]/input[2]').click()
        time.sleep(3)
        print('search pass')

    def test_login(self):
        driver = self.driver
        nowhandle = driver.current_window_handle #得到当前窗口句柄
        driver.find_element_by_xpath('//*[@id="js_IndexSlider"]/div/div[1]/div[2]/div[1]/a').click()
        time.sleep(3)
        allhandles = driver.window_handles #得到所有窗口句柄
        for handle in allhandles:
            if handle != nowhandle:   # 获取新窗口句柄
                driver.switch_to.window(handle)
                driver.find_element_by_xpath('/html/body/div[6]/a[1]').click()
        print('login_pass')

    def tearDown(self):
        self.driver.quit()
        print("teat down")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Viqyingtest('test_search'))
    filename =  'F:\\result2.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()



