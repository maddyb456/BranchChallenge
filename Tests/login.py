from selenium import webdriver
import time

# setup webdriver and create browser
driver = webdriver.Chrome("../Drivers/chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)


# Login to Branch
def branch_login():
    driver.get('https://dashboard.branch.io/login')
    time.sleep(5)
    work_email = driver.find_element_by_name("email")
    work_email.send_keys('maddybr@gmail.com')
    password = driver.find_element_by_name("password")
    password.send_keys('Interview#2019#')
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    print("Successfully logged in")


# clicking Liveview and verifying the OS
def live_view_events(campaign_url):
    time.sleep(45)
    driver.find_element_by_link_text("Liveview").click()
    print("Successfully clicked Liveview")
    time.sleep(5)
    os_value = driver.find_element_by_xpath(
        "//*[@id='app']/div/div[2]/div[2]/div/div[4]/div[1]/table/tbody/tr[1]/td[3]")
    print(os_value.text)
    if os_value.text == 'ANDROID_WEB':
        goto_quick_links(campaign_url)
    else:
        print("No click was captured in the dashboard")
        return None

# clicking Quick Links and verifying the link URL and stats
def goto_quick_links(campaignurl):
    driver.find_element_by_link_text("Quick Links").click()
    print("Successfully clicked Quick Links")
    time.sleep(5)
    url_verification = driver.find_element_by_xpath(
        "//*[@id='app']/div/div[2]/div[2]/div/div[4]/div/div/div[1]/table/tbody/tr/td[3]/div/div[1]/a")
    print(url_verification.text)
    if url_verification.text == campaignurl:
        stats = driver.find_element_by_xpath(
            "//*[@id='app']/div/div[2]/div[2]/div/div[4]/div/div/div[1]/table/tbody/tr/td[4]")
        if int(stats.text) > 0:
            print(stats.text)
        else:
            print('Stats data not accurate')
    driver.quit()
