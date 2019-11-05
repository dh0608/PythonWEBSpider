from selenium import webdriver



brower = webdriver.PhantomJS()
# brower.maximize_window()
brower.get("https://blog.csdn.net/Kwoky/article/details/80285201")
brower.save_screenshot("./images/app1.png")
