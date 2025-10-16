import time
from playwright.sync_api import Page, expect, sync_playwright
import re
import os
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
ADMIN_LINK = os.getenv("ADMIN_LINK")
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(ADMIN_LINK)
    time.sleep(10)
    username = page.locator("xpath=/html/body/app-root/div/wgc-login/div/div/div[1]/div/div/div/div[2]/form/div[1]/input")
    username.fill(USERNAME)
    time.sleep(5)
    password= password_entry= page.locator("xpath=/html/body/app-root/div/wgc-login/div/div/div[1]/div/div/div/div[2]/form/div[2]/input")
    password.fill(PASSWORD)
    signin_button = page.locator("xpath=/html/body/app-root/div/wgc-login/div/div/div[1]/div/div/div/div[2]/form/div[3]/button")
    signin_button.click()
    time.sleep(5)
    page.locator('xpath=//*[@id="m_ver_menu"]/ul/li[41]/a').scroll_into_view_if_needed()
    shop_link= page.locator('xpath=//*[@id="m_ver_menu"]/ul/li[41]/a')
    shop_link.click()
    time.sleep(5)
    page.locator('xpath=/html/body/app-root/div/div/div/div[2]/app-game-sales-shop/div/div/div[1]/div[2]/ul/li[2]/div/a').hover()
    time.sleep(3)
    with page.expect_download() as download_info:
        page.locator(
            'xpath= /html/body/app-root/div/div/div/div[2]/app-game-sales-shop/div/div/div[1]/div[2]/ul/li[2]/div[1]/div/div/div/div/ul/li[2]/a').click(
            force=True)
    download = download_info.value
    download.save_as(rf"C:\Users\WGG\Documents\BOTFILES\shop_export.xlsx")
    time.sleep(10)
    page.locator('xpath=//*[@id="m_ver_menu"]/ul/li[39]/a').scroll_into_view_if_needed()
    shop_link=  page.locator('xpath=//*[@id="m_ver_menu"]/ul/li[39]/a')
    shop_link.click()
    time.sleep(5)
    page.locator('xpath=/html/body/app-root/div/div/div/div[2]/app-game-sales-branch/div/div/div[1]/div[2]/ul/li[2]/div/a').hover(
    )
    time.sleep(3)
    with page.expect_download() as download_info:
        page.locator(
            'xpath=/html/body/app-root/div/div/div/div[2]/app-game-sales-branch/div/div/div[1]/div[2]/ul/li[2]/div[1]/div/div/div/div/ul/li[2]/a').click(
            force=True)
    download = download_info.value
    download.save_as(rf"C:\Users\WGG\Documents\BOTFILES\branch_export.xlsx")
    input("Press enter to continue...")

