#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def no_delay(path,driver):
    while 1:
        try:
            driver.find_element_by_xpath(path)
            return
        except:
            time.sleep(1)

def no_delay_click(path,driver):
    global id
    global code
    while 1:
        url = driver.current_url
        print(url)
        if 'iaaa' in url:
            user_name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[1]/input')
            user_name_kill = user_name.send_keys(id)

            user_code = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[2]/input')
            user_code_kill = user_code.send_keys(code)

            button = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[8]/input[3]')
            button_kill = button.click()
            time.sleep(1)
        try:
            button = driver.find_element_by_xpath(path)

            button_kill = button.click()
            # print(button.text)
            return
        except:
            time.sleep(1)



if __name__ == '__main__':

    driver = webdriver.Safari()
    driver.get('https://portal.pku.edu.cn/portal2017/#/bizCenter')

    no_delay('/html/body/div/div[2]/form/div/div[1]/input',driver)
    #填入你的学号
    id = ''
    #填入你的密码
    code = ''

    # while 1:
    #     try:
    user_name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[1]/input')
    user_name_kill = user_name.send_keys(id)

    user_code = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[2]/input')
    user_code_kill = user_code.send_keys(code)

    button = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[8]/input[3]')
    button_kill = button.click()
    print('here?')
    time.sleep(1)

    url = driver.current_url
    print(url)
    time.sleep(1)

    while 'iaaa' in url:
        try:
            user_name = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[1]/input')
            user_name_kill = user_name.send_keys(id)

            user_code = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[2]/input')
            user_code_kill = user_code.send_keys(code)

            button = driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div[8]/input[3]')
            button_kill = button.click()
            print('here?')
            print(driver.current_url)

            time.sleep(1)
        except:
            break

    known_path = '/html/body/div[1]/div[3]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a'
    no_delay_click(known_path, driver)



    print('here!')
        # break
        # except:


    # known_path = '/html/body/div[1]/div[3]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a'
    # no_delay_click(known_path,driver)

    window_before = driver.window_handles[0]
    print(window_before)

    yunzhanyi_paht = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/table/tbody/tr[1]/td/a[11]'
    no_delay_click(yunzhanyi_paht,driver)

    while 1:

        time.sleep(1)
        try:
            another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
            driver.switch_to.window(another_window)
            break
        except:
            time.sleep(1)

    print(driver.window_handles)
    # print(window_after)
    # print(driver.window_handles)

    empty_symptom = '/html/body/div[1]/div/div[2]/section/main/div[2]/div[2]/div[1]/form/div[14]/div/label[2]/span[1]/span'
    no_delay_click(empty_symptom,driver)

    sf = '/html/body/div[1]/div/div[2]/section/main/div[2]/div[2]/div[1]/form/div[15]/div/div/div/input'
    no_delay_click(sf,driver)

    choice = '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span'
    no_delay_click(choice,driver)
    no_delay_click(choice, driver)
    no_delay_click(choice, driver)


    # options = driver.find_elements_by_css_selector("body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > ul")
    #
    # for option in options:
    #     print(option)
    #     if "健康" in option.text.strip():
    #         option.click()
    time.sleep(1)
    save = '/html/body/div[1]/div/div[2]/section/main/div[2]/div[2]/div[1]/form/div[18]/div/button'
    no_delay_click(save,driver)
    time.sleep(3)
    driver.quit()














