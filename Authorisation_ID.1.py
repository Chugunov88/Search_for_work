import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\python_selenium\\chromedriver.exe')
base_url = 'http://u920152e.beget.tech/'
driver.get(base_url)

login_standard_user = "gogen@gmail.com"
password_all = "Goga2829123"


def authorisation():
    user_name = driver.find_element(By.XPATH, "//input[@type='email']")
    user_name.send_keys(login_standard_user)
    print("Input login")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys(password_all)
    print("Input Password")
    button_login = driver.find_element(By.XPATH, "//button[@class='form_auth_button']")
    button_login.click()
    print("Click Login Button")

def choose_age():
    question = driver.find_element(By.XPATH, "/html/body/form/p")
    value_text_question = question.text
    print(value_text_question)
    assert value_text_question == "Сколько Вам лет?"
    print("GOOD")
    url = "http://u920152e.beget.tech/page1.html?auth_email=gogen%40gmail.com&auth_pass=Goga2829123&form_auth_submit="
    get_url = driver.current_url
    print(get_url)
    assert url == get_url
    print("Good url")
    age_18 = driver.find_element(By.XPATH, "//input[@value='18']")
    button_age = driver.find_element(By.XPATH, "//input[@type='submit']")
    age_18.click()
    button_age.click()

def finish_page():
    question = driver.find_element(By.XPATH, "/html/body/p")
    value_text_question = question.text
    print(value_text_question)
    assert value_text_question == "Никоторые считают что человек взраслеит в каком нибудь оприделённом возрасте например, к 18 лет , когда он становиться совершенно летним. Но есть люди, которые и в более старшем возрасте остаются детьми. Что же значит быть взрослым? Взрослость озночает самостоятельность, то есть умение обходится без чьей-либо помощи опеки. Человек обладающий этим качеством всё делает сам, и не ждёт поддержки от других. Он понимает, что свои трудности должен преодалевать сам. Конечно бывают ситуации, когда человеку одному не справится. Понимая это, ему приходиться просить помощи у друзей, родственников, и знакомых. Однако в целом самостоятельному, взрослому человеку не свойственно надеяться на других. Есть такое выражение: руке следует ждать помощи только от плеча. Самостоятельный человек умеет отвечать за себя свои дела и поступки. Он сам планирует свою жизнь, и оценивает себя не пологаясь на чьё-то мнение. Он понимает, что многое в жизни зависет от него самого. Быть взрослым - значит отвечать за кого-то ещё. Но для этого тоже надо стать самостоятельным, уметь принимать решения. Взрослость зависет не от возраста, а от жизненного опыта от стремления прожить жизнь без нянек."
    print("GOOD")
    url = "http://u920152e.beget.tech/page2.html"
    get_url = driver.current_url
    print(get_url)
    assert url == get_url
    print("Good url")


    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = 'screenshot' + now_date + '.png'
    time.sleep(5)
    time.sleep(5)
    driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\python_selenium\\screen\\' + name_screenshot)
    print(f"Создан скриншот {name_screenshot}")

authorisation()
choose_age()
finish_page()
print("Все этапы тестирования пройдены согласно тест кейсу: ID.1")