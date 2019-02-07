
__author__ = 'jagdishm'

import unittest
import time
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
accountname = "TestAccount12"
accteditname = "Test12345"
accountadmin = "Test@abc.comm"

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/jagdishm/Downloads/chromedriver")
        cls.driver.get('https://testsigntrace.com')
       # cls.driver.maximize_window()

    #Login for Signtrace Admin
    #@unittest.skip("Test Skipped")
    def test_1SigntraceAdmin(self):
        self.login()

       # Assert UI has Accounts and Users tab

        self.assertEquals("Accounts", self.driver.find_element_by_id("nav_account").text)
        self.assertEquals("Users", self.driver.find_element_by_id("nav_user").text)

        # Logout
        self.driver.find_element_by_xpath("/html/body/div/header/div/div[2]/div/ul/li[3]/a").click()

        #Account Creation
    #@unittest.skip("Test Skipped")
    def test_2AccountCreation(self):
        self.login()
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[2]/a").click()

        self.driver.find_element_by_id("name").send_keys(accountname)
        self.driver.find_element_by_id("submit").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[1]/a").click()
        elemaccount = self.driver.find_element_by_xpath("//*[@id='accountList']/tbody/tr[10]/td[1]/b").text
        self.assertEqual(accountname,elemaccount)

        #Edit account name
        self.driver.find_element_by_xpath("//*[@id='accountList']/tbody/tr[6]/td[2]/a[2]").click()
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys(accteditname)
        self.driver.find_element_by_id("submit").click()
        ele = self.driver.find_element_by_xpath("//*[@id='accountList']/tbody/tr[6]/td[1]/b").text
        self.assertEqual(accteditname,ele)

        self.logout()

        #Account Switching
    #@unittest.skip("Test Skipped")
    def test_3AccountSwitch(self):
        self.login()
        self.driver.find_element_by_xpath("//*[@id='accountList']/tbody/tr[2]/td[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id='header_1']/ul/li[5]/a").click()
        self.assertEqual("select", self.driver.find_element_by_xpath("//*[@id='accountList']/tbody/tr[3]/td[2]/a[1]").text)

        self.logout()

        #Account Admin Creation and assertion
    #@unittest.skip("Test skipped")
    def test_4AccountAdminCreation(self):
        self.login()
        self.driver.find_element_by_id("nav_user").click()
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[2]/a").click()
        self.driver.find_element_by_id("name").send_keys("Test user 1")
        self.driver.find_element_by_id("username").send_keys(accountadmin)
        self.driver.find_element_by_id("password").send_keys("test")
        self.driver.find_element_by_xpath("//*[@id='role']/option[2]").click()
        self.driver.implicitly_wait(100)
        
        self.driver.find_element_by_xpath("//*[@id='account_id']/option[7]").click()
        
        self.driver.find_element_by_id("submit").click()
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[1]/a").click()
        element = self.driver.find_element_by_xpath("//*[contains(text(), 'Test user 1' )]").text
        self.assertEqual('Test user 1 (test@test.test)',element)

        self.logout()

        #Account User Creation
    #@unittest.skip("Test skipped")
    def test_5AccountUserCreation(self):
        self.login()
        self.driver.find_element_by_id("nav_user").click()
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[2]/a").click()
        self.driver.find_element_by_id("name").send_keys("Test user 2")
        self.driver.find_element_by_id("username").send_keys("test12@test.test")
        self.driver.find_element_by_id("password").send_keys("test")
        self.driver.find_element_by_xpath("//*[@id='role']/option[3]").click()
        
        self.driver.find_element_by_xpath("//*[@id='account_id']/option[7]").click()
        
        self.driver.find_element_by_id("submit").click()
        self.driver.find_element_by_xpath("//*[@id='subnav']/ul/li[1]/a").click()
        element1 = self.driver.find_element_by_xpath("//*[contains(text(), 'Test user 2' )]").text
        self.assertEqual('Test user 2 (test12@test.test)', element1)

        self.logout()

    #Login for Account Admin
  #  @unittest.skip("Test Skipped")
    def test_6AccountAdmin(self):
        self.driver.find_element_by_id("username").send_keys("****")
        self.driver.find_element_by_id("password").send_keys("****")
        self.driver.find_element_by_id("submit").click()
        self.assertIn("SignTrace", self.driver.title)
        self.driver.implicitly_wait(10)

        self.logout()

    #Login for Account User
   # @unittest.skip("Test Skipped")
    def test_7User(self):
        self.driver.find_element_by_id("username").send_keys("***")
        self.driver.find_element_by_id("password").send_keys("***")
        self.driver.find_element_by_id("submit").click()
        self.assertIn("SignTrace", self.driver.title)
        self.driver.implicitly_wait(10)

        self.logout()

    #Invalid Login
    #@unittest.skip("Test Skipped")
    def test_8invalidLogin(self):
        self.driver.find_element_by_id("username").send_keys("!@#@!#")
        self.driver.find_element_by_id("password").send_keys("*****")
        self.driver.find_element_by_id("submit").click()
        ele=self.driver.find_element_by_tag_name("li")
        
        self.assertEquals("Invalid Credentials", ele.text)

    #Login
    def login(self):
        self.driver.find_element_by_id("username").send_keys("****")
        self.driver.find_element_by_id("password").send_keys("***")
        self.driver.find_element_by_id("submit").click()

    #Logout
    def logout(self):
        self.driver.find_element_by_xpath("//*[@id='header_1']/ul/li[1]/a").click()
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    HTMLTestRunner.main()
    #unittest.main()
