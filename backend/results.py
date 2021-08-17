from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def getResults(query):
    # class Result:
    #     def __init__(self, title, view, link):
    #         self.title = title
    #         self.view = view
    #         self.link = link
    results = []
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
    baseurl = "http://youtube.com"
    keyword = query.replace(" ", "+")
    driver.get(f'{baseurl}/search?q={keyword}')
    # baseurl = "https://www.khanacademy.org"
    # keyword = "algebra"
    # driver.get(f'{baseurl}/search?page_search_query={keyword}')
    # print([my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='gsc-webResult gsc-result']")))])

    titles = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//yt-formatted-string[@class='style-scope ytd-video-renderer' and @aria-label]")))]
    views = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='metadata-line']/span[@class='style-scope ytd-video-meta-block'and contains(., 'views')]")))]
    links = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@id='video-title']")))]

    driver.quit()

    for i in range(len(titles)):
        results.append({
            "title": titles[i], 
            "views": views[i], 
            "links": links[i]})
    print(results)

    return results