# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
import time
import datetime
import timeBar


driver = webdriver.Chrome(r'chromedriver.exe')
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
now_time = datetime.datetime.now().strftime('%Y %m %d')
driver.maximize_window()


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<全局变量<<<<<<<<<<<<<<<<<<<<<<<<
url="http://10.71.75.77/itop/web/pages/UI.php"
organization = "工单所填的公司组织或关联"
loginame = "张三"
password = "123456";  
persion = "张 "
name = "三"
morningTitle = now_time + '早上巡检'
nightTitle = now_time + '晚上巡检'
describeServer = '这里是服务台创建用户需求的描述'
serverSolutionResult = "这里是服务台解决用户需求的解决方案"
describeEvent = '这里是事件工单巡检事件问题。'
eventSolutionResult = '这里是事件工单解决方案'

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def itopLogin(user, pwd):
    driver.get()
    print("登陆")
    driver.find_element_by_id('user').clear()
    driver.find_element_by_id('user').send_keys(user)  
    driver.find_element_by_id('pwd').clear()
    driver.find_element_by_id('pwd').send_keys(pwd)  
    driver.find_element_by_class_name('btn_border').click()
    sleep(1)
    jobOder('AccordionMenu_RequestManagement', "新建用户需求", morningTitle, describeServer, "//option[@value='110']")   # 创建服务工单
    print("服务工单建立完毕，不要动，距离事件工单建立需1个半小时")
	sleep(9000)
    timeBar.zhanshi("01:30:00")
    jobOder('AccordionMenu_IncidentManagement', "新建事件", morningTitle+"设备告警信息", describeEvent, "//option[@value='222']") # 创建事件工单
    submitJobOder("开始解决事件工单", 'AccordionMenu_IncidentManagement', "分配给我的事件", eventSolutionResult) # 提交事件工单
    submitJobOder("开始解决服务请求", 'AccordionMenu_RequestManagement', "分配给我的需求", serverSolutionResult)
    driver.close()

def jobOder(singleID, singleName, title, content, subserviceValueID):     
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<新建请求<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    driver.find_element_by_id(singleID).click()
    sleep(1)
    print(singleName)
# 新建用户需求
    driver.find_element_by_link_text(singleName).click()
    sleep(2)
    print('填写表单')
# 填写巡检表单
    driver.find_element_by_id('label_2_org_id').send_keys(organization)
    sleep(2)
# [last()]/ul/li[@class="ac_item"]/strong/text()
    driver.find_element_by_xpath('//div[@class="ac_results"]').click()
    sleep(2)
    driver.find_element_by_id('label_2_caller_id').send_keys(persion)
    sleep(1)
    driver.find_element_by_xpath('//div[@class="ac_results"][last()]').click()
    sleep(2)
    driver.find_element_by_name('attr_title').send_keys(title)
# 有iframe
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)
    driver.find_element_by_css_selector('p').send_keys(content)
    driver.switch_to.default_content()
    sleep(2)
    driver.find_element_by_id("2_service_id").click()
    driver.find_element_by_xpath("//option[@value='19']").click()
    sleep(1)
    driver.find_element_by_id("2_servicesubcategory_id").click()
    sleep(2)
    driver.find_element_by_xpath(subserviceValueID).click()
    sleep(1)
    driver.find_element_by_id("2_servicesubcategory_id").click()
    sleep(5)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<关联联系人<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 关联联系人
    print('关联联系人')
    driver.find_element_by_link_text("联系人").click()
    driver.find_element_by_id("contacts_list_btnAdd").click()
    sleep(2)
    driver.find_element_by_id("dh_SearchFormToAdd_contacts_list").click()
    sleep(1)
    driver.find_element_by_xpath('//select[@name="class"][last()]').click()
    sleep(1)
    driver.find_element_by_xpath("//option[@value='Person']").click()
    sleep(3)
    driver.find_element_by_xpath('//input[@name="name"]').send_keys(persion)
    driver.find_element_by_xpath('//input[@name="first_name"]').send_keys(name)
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    sleep(2)
    driver.find_element_by_xpath('//input[@type="checkBox"]').click()
    driver.find_element_by_id("btn_ok_contacts_list").click()
	
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<关联联系人结束<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<提交<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,<<<
    sleep(3)
    print('提交')
    driver.find_element_by_xpath('//button[@type="submit"]').click()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<请求创建完毕<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<开始分配服务请求<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    sleep(1)
    print("分配给自己")
    driver.find_element_by_class_name("actions_menu").click()
    sleep(1)
    driver.find_element_by_link_text("分配").click()
    sleep(1)
    driver.find_element_by_id("att_0").click()
    driver.find_element_by_xpath("//option[@value='29']").click()
    sleep(1)
    driver.find_element_by_id("att_1").click()
    sleep(1)
    driver.find_element_by_xpath("//option[@value='88']").click()
    driver.find_element_by_id("att_1").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@type="submit" and @class="action"][1]').click()
    sleep(2)

def submitJobOder(pint,singleID,singleName,solution):
    print(pint)
    driver.find_element_by_id().click(singleID)
    driver.find_element_by_link_text(singleName).click()
    sleep(2)
    driver.find_element_by_class_name("actions_menu").click()
    driver.find_element_by_link_text("标记为已解决").click()
    sleep(1)
    driver.find_element_by_class_name("attr_solution").send_keys(solution)
    driver.find_element_by_xpath('//*[@type="submit" and @class="action"][1]').click()
    sleep(3)


if __name__ == "__main__":

    itopLogin(loginame, password)


