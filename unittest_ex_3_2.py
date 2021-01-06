from selenium import webdriver
import time
import unittest

class TestClass(unittest.TestCase):

    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input_first = browser.find_element_by_css_selector(".first_block> :nth-child(1)>input")
            input_first.send_keys('Ivan')

            input_first = browser.find_element_by_css_selector(".first_block> :nth-child(2)>input")
            input_first.send_keys('Ivanov')

            input_mail = browser.find_element_by_css_selector(".first_block> :nth-child(3)>input")
            input_mail.send_keys('Ivanov@gmail.com')

            input_phone = browser.find_element_by_css_selector(".second_block> :nth-child(1)>input")
            input_phone.send_keys('89990009990')

            input_addres = browser.find_element_by_css_selector(".second_block> :nth-child(2)>input")
            input_addres.send_keys('Moscow')

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)

        finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
        # закрываем браузер после всех манипуляций
            browser.quit()


    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input_first = browser.find_element_by_css_selector(".first_block> :nth-child(1)>input")
            input_first.send_keys('Ivan')

            input_first = browser.find_element_by_css_selector(".first_block> :nth-child(2)>input")
            input_first.send_keys('Ivanov')

            input_mail = browser.find_element_by_css_selector(".first_block> :nth-child(3)>input")
            input_mail.send_keys('Ivanov@gmail.com')

            input_phone = browser.find_element_by_css_selector(".second_block> :nth-child(1)>input")
            input_phone.send_keys('89990009990')

            input_addres = browser.find_element_by_css_selector(".second_block> :nth-child(2)>input")
            input_addres.send_keys('Moscow')

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!" , welcome_text)

        finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(2)
        # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()