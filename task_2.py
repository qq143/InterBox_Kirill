from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class EbayProductScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 0.1)

    def scrape_product_data(self):
        self.driver.get(self.url)

        try:
            # Ссылка на товар
            product_url = self.url
            print("—" * 80)
            print(f"Product URL: {product_url}")

            # Название товара
            product_title = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'title')]"))).text.strip()
            print(f"Title: {product_title}")

            # Ссылка на фото товара
            product_image_url = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'img')]"))).get_attribute('src')
            print(f"Image URL: {product_image_url}")

            # Цена товара
            product_price = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'price')]"))).text.strip()
            print(f"Price: {product_price}")

            # Продавец
            try:
                seller_name = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'mbg-nw')]"))).text.strip()
            except:
                seller_name = "Unknown"
            print(f"Seller: {seller_name}")

            # Цена доставки
            try:
                shipping_price = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(@id, 'fshippingCost')]"))).text.strip()
            except:
                shipping_price = "Not specified"
            print(f"Shipping Price: {shipping_price}")

        except Exception as e:
            print(f"Ошибка: {str(e)}")

        finally:
            self.driver.quit()


if __name__ == "__main__":
    with open('goods_urls.txt', 'r') as file:
        urls = file.read().splitlines()

    if not urls:
        print(f"В 'goods_urls.txt' не найдено ссылок.")
    else:
        for url in urls:
            scraper = EbayProductScraper(url)
            scraper.scrape_product_data()
