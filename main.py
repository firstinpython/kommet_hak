import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
'''автоматически скачиваю драйвера для браузера очень эффективно если не хотите скачивать драйвера сами))'''

browser.implicitly_wait(5)
'''е формальная задержка работает если мы что то находим то есть если мы ищем какой то элемент то на сайте он может прогрузиться через какое то время и на протяжении заданного времени мы ищем этот 
элемент , но если элемент уже прогрузился то мы переходим к следующему этапу очень классная замена sleep'''
link = "ваш сайт"
browser.get(link)
time.sleep(5)
'''жду что бы сайт нормально открылся (можно и без этой задержки)'''
video_mass = browser.find_elements(By.CLASS_NAME,"video_block")
'''нахожу все элементы по книгам'''
mass_link = []
for i in range(len(video_mass)):
    mass_link.append(video_mass[i].find_element(By.TAG_NAME,"a").get_attribute("href"))
    '''в элементах нахожу ссылки к каждой книге и записываю в массив'''
for j in mass_link:
    browser.get(j)
    c = browser.find_element(By.CLASS_NAME,"comments-label")
    '''нахожу ввод'''
    browser.execute_script("return arguments[0].scrollIntoView(true);",c)
    '''спускаюсь до элемента ввод (очень удобная штука ведь мы не можем предугадать точное количество пикселей скролла потому что комментариев всегда разное колличество)'''

    text = browser.find_element(By.XPATH,"//*[@id='comment']")

    text.send_keys("интересная книга))")
    '''в поле ввода ввожу наш текст'''
    but = browser.find_element(By.CLASS_NAME,"input_submit").click()
    '''нажимаю на кнопку и все наш скрипт сделал свое дело:)'''
    time.sleep(2)
