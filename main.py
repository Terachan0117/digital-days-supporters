from selenium import webdriver
import chromedriver_binary
import csv
import json

# Seleniumオプション設定
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")

# Chromeドライバ起動
driver = webdriver.Chrome()

# 「デジタルの日」サポーターページへアクセス
driver.get("https://digital-days.digital.go.jp/supporters/")

# 読み込み待機
driver.implicitly_wait(0)

# データ格納用
data = []

while True:

    # ページの中からサポーターに関する情報を取り出し、dataに追加していく
    supporters = driver.find_element_by_class_name("supportersList").find_elements_by_tag_name("li")
    for supporter in supporters:
        name = supporter.find_element_by_class_name("supportersName").text
        actions = ""
        if(len(supporter.find_elements_by_class_name("supportersTxt")) > 0):
            actions = supporter.find_element_by_class_name("supportersTxt").text
        data.append({"name": name, "actions": actions})

    # 次のページがある場合次のページへ
    if(driver.find_element_by_xpath("/html/body/div/article/section/div/div[1]/a[2]").get_attribute("href")):
        driver.find_element_by_xpath("/html/body/div/article/section/div/div[1]/a[2]").click()

        # 読み込み待機
        driver.implicitly_wait(0)

    # 次のページがない場合は終了
    else:
        break

# ファイルに保存
print("Saving to file")
with open('supporters.csv', 'w', encoding = 'utf-8', newline = '') as f:
    writer = csv.DictWriter(f, ['name', 'actions'])
    writer.writeheader()
    writer.writerows(data)
with open('supporters.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii = False)

# Chromeドライバ終了
driver.quit()

print("Done!!")
