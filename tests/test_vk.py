from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_vk_for_mobile_device(browser):
    VkForMobile = browser.find_element(By.CLASS_NAME, 'login_mobile_header')
    assert 'VK for mobile devices' in VkForMobile.text

def test_check_box_save_user(browser):
    CheckBoxSaveUser = browser.find_element(By.CLASS_NAME, 'VkIdCheckbox__checkboxOn').click()
    CheckBoxSelected = browser.find_element(By.CLASS_NAME, 'VkIdCheckbox__checkboxOn')
    assert CheckBoxSelected.is_selected() == False