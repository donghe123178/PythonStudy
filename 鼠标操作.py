import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
'''
鼠标操作：
    单击
    双击
    右击
    拖拽
    悬停
'''
# 百度高级搜索
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 定位设置元素
setting_elem = driver.find_element_by_id("s-usersetting-top")
# 实例化鼠标类
action = ActionChains(driver)
# 鼠标悬停
action.move_to_element(setting_elem).perform()
# 定位高级搜索元素
adv_setting_elem = driver.find_element_by_link_text("高级搜索")
# 鼠标单击
action.click(adv_setting_elem).perform()
time.sleep(3)

# 打开新网页
driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
# 切换到iframe
iframe_elem = driver.find_element_by_id("iframeResult")
driver.switch_to.frame(iframe_elem)
# 实例化鼠标类
action = ActionChains(driver)
# 鼠标拖拽
drag_elem = driver.find_element(By.XPATH, "//div[@id='draggable']")
drop_elem = driver.find_element(By.XPATH, "//div[@id='droppable']")
action.drag_and_drop(drag_elem, drop_elem).perform()
# 关闭浏览器
time.sleep(2)
driver.quit()





