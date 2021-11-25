from selenium import webdriver
from time import sleep
import random
import string


# random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# webdriver
driver = webdriver.Firefox(executable_path="/home/toor/geckodriver")
driver.get("https://randomsatoshi.win/autofaucet/")
sleep(10)


# random_letters
def main():
    rand = random.randrange(8, 13)
    em = id_generator(rand)
    largos = random.randrange(12, 15)
    pa = id_generator(largos)
    sudo = random.randrange(8, 10)
    user = id_generator(sudo)
    # the_loop
    for i in range(1):
        print("Request number : {}".format(i))
        e = ('{}@gmail.com'.format(em))
        creat_account = driver.find_element_by_xpath('//a[@class="RS-button1"]')
        sleep(2)
        # creat acc
        creat_account.click()
        sleep(3)
        # the access
        username = driver.find_element_by_xpath("//input[@name='username']")
        email = driver.find_element_by_xpath("//input[@name='email']")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password_rep = driver.find_element_by_xpath("//input[@name='password-rep']")
        # username
        username.click()
        username.send_keys(user)
        sleep(3.7)
        # email
        email.click()
        email.send_keys(e)
        sleep(2.9)
        # password
        password.click()
        password.send_keys(pa)
        sleep(4.7)
        # rep-password
        password_rep.click()
        password_rep.send_keys(pa)
        # captcha
        recapcha = driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
        recapcha.click()
        sleep(8)

        main()
    main()


main()
