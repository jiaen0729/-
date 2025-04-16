"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GXaVkz2ZDL1s5nmUYe25eszEulJPeZZM
"""

# -*- coding: utf-8 -*-
"""113-2期中.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J0Vtmrb-oms378mTeicvAZL6hEPUKZyL
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def scrape_professors_expertise(base_url="https://csie.asia.edu.tw/zh_tw/associate_professors_2", max_pages=5, add_special_cases=False):
    all_professors = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    for page in range(1, max_pages + 1):
        if page == 1:
            current_url = base_url
        else:
            current_url = f"{base_url}?page_no={page}"

        try:
            req = Request(current_url, headers=headers)
            html = urlopen(req)
            soup = BeautifulSoup(html, 'html.parser')

            text = soup.get_text()

            pattern = r'姓名[\s\:：]+([\w\(\)\-\,\. ]+)\s*\n+\s*職稱[\s\:：]+([^\n]+)\s*\n+[\s\S]*?研究領域[\s\:：]+([\s\S]*?)(?=\s*Office hour|網站|分機)'
            matches = re.findall(pattern, text)

            if not matches and page > 1:
                break

            for match in matches:
                name, title, expertise = match
                name = name.strip()
                expertise = expertise.strip().replace('\n', ' ')

                expertise = expertise.replace(', ', '、').replace('，', '、').replace(' ,', '、')
                expertise = expertise.replace(',、', '、')

                all_professors.append({
                    '姓名': name,
                    '專長': expertise
                })

                print(f"教授: {name}, 專長: {expertise[:50]}...")

        except Exception as e:
            break

    if add_special_cases:
        special_cases = [
            {"姓名": "Tadao Murata", "專長": "分散式通訊軟體、網路協議、邏輯與規則基礎AI系統、製造系統、平行計算系統和具有模糊延遲的系統的Petri網應用"},
            {"姓名": "曾憲章(Zeng Xianzhang)", "專長": "計算機科學"},
            {"姓名": "李錦輝(Chin-Hui Lee)", "專長": "語音訊號處理、機器學習"},
            {"姓名": "黃光彩", "專長": "電機工程"},
            {"姓名": "林一平(Jason Yi-Bing Lin)", "專長": "個人通信網路、行動計算、系統模擬"},
            {"姓名": "張嘉淵(Zhang Jiayuan)", "專長": "雲端運算、大數據分析、演算法、社群媒體、人工智慧物聯網、人本創新應用"},
            {"姓名": "許健(Gene Sheu)", "專長": "電子電路、微電子、產品研發、積體電路"},
            {"姓名": "梁文隆(Wen-Lung Liang)", "專長": "物聯網技術、嵌入式系統、智慧家庭"},
            {"姓名": "林詠章(Lin Yongzhang)", "專長": "資訊安全、區塊鏈應用、精準健康、智慧醫療、工控安全"}
        ]

        for case in special_cases:
            all_professors.append(case)
            print(f"教授: {case['姓名']}, 專長: {case['專長'][:50]}...")

    return all_professors

def save_simple_output(professors_data, filename="professors_expertise_simple.txt"):
    with open(filename, 'w', encoding='utf-8') as txtfile:
        for professor in professors_data:
            txtfile.write(f"教授: {professor['姓名']}, 專長: {professor['專長']}\n")

    print(f"資料已保存至 {filename}")

def main():
    associate_professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/associate_professors_2")
    assistant_professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/assistant_professors_2")
    lecturers = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/senior_lecturer")
    professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/all_professors_1")

    all_professors = associate_professors + assistant_professors + lecturers + professors

    special_cases = [
        {"姓名": "Tadao Murata", "專長": "分散式通訊軟體、網路協議、邏輯與規則基礎AI系統、製造系統、平行計算系統和具有模糊延遲的系統的Petri網應用"},
        {"姓名": "曾憲章(Zeng Xianzhang)", "專長": "計算機科學"},
        {"姓名": "李錦輝(Chin-Hui Lee)", "專長": "語音訊號處理、機器學習"},
        {"姓名": "黃光彩", "專長": "電機工程"},
        {"姓名": "林一平(Jason Yi-Bing Lin)", "專長": "個人通信網路、行動計算、系統模擬"},
        {"姓名": "張嘉淵(Zhang Jiayuan)", "專長": "雲端運算、大數據分析、演算法、社群媒體、人工智慧物聯網、人本創新應用"},
        {"姓名": "許健(Gene Sheu)", "專長": "電子電路、微電子、產品研發、積體電路"},
        {"姓名": "梁文隆(Wen-Lung Liang)", "專長": "物聯網技術、嵌入式系統、智慧家庭"},
        {"姓名": "林詠章(Lin Yongzhang)", "專長": "資訊安全、區塊鏈應用、精準健康、智慧醫療、工控安全"}
    ]

    for case in special_cases:
        all_professors.append(case)
        print(f"教授: {case['姓名']}, 專長: {case['專長'][:50]}...")

    unique_professors = []
    seen_names = set()
    for professor in all_professors:
        if professor['姓名'] not in seen_names:
            unique_professors.append(professor)
            seen_names.add(professor['姓名'])

    save_simple_output(unique_professors)

if __name__ == "__main__":
    main()

def save_to_file(data_list, filename="output.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"資料已成功保存到 {filename}")
    except Exception as e:
        print(f"保存文件時發生錯誤: {e}")

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def scrape_professors_expertise(base_url="https://csie.asia.edu.tw/zh_tw/associate_professors_2", max_pages=5):
    all_professors = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    for page in range(1, max_pages + 1):
        if page == 1:
            current_url = base_url
        else:
            current_url = f"{base_url}?page_no={page}"

        try:
            req = Request(current_url, headers=headers)
            html = urlopen(req)
            soup = BeautifulSoup(html, 'html.parser')

            # 移除分頁導覽元素
            for pagination in soup.find_all('div', class_='pagination'):
                pagination.decompose()

            # 移除頁尾資訊
            for footer in soup.find_all('div', class_='footer'):
                footer.decompose()

            # 移除社交分享按鈕
            for share in soup.find_all('div', class_='share'):
                share.decompose()

            # 找到所有教授區塊
            professor_blocks = soup.find_all('div', class_='teacher-list')

            if not professor_blocks and page > 1:
                break

            # 如果找不到具體的教授區塊，使用舊的方法
            if not professor_blocks:
                text = soup.get_text()

                # 清理網頁底部的分頁和頁腳資訊
                text = re.sub(r'最前\s*\d+\s*\d+\s*[上下]一頁\s*最後.*$', '', text, flags=re.DOTALL)
                text = re.sub(r'Share\s*Tweet\s*Print this page.*$', '', text, flags=re.DOTALL)

                pattern = r'姓名[\s\:：]+([\w\(\)\-\,\. ]+)\s*\n+\s*職稱[\s\:：]+([^\n]+)\s*\n+[\s\S]*?研究領域[\s\:：]+([\s\S]*?)(?=\s*Office hour|網站|分機|\s*姓名[\s\:：]+|\s*$)'
                matches = re.findall(pattern, text)

                for match in matches:
                    name, title, expertise = match
                    name = name.strip()
                    expertise = expertise.strip().replace('\n', ' ')

                    expertise = expertise.replace(', ', '、').replace('，', '、').replace(' ,', '、')
                    expertise = expertise.replace(',、', '、')

                    all_professors.append({
                        '姓名': name,
                        '專長': expertise
                    })
                    print(f"教授: {name}, 專長: {expertise[:50]}...")
            else:
                # 使用更結構化的方式提取資訊
                for block in professor_blocks:
                    try:
                        # 提取姓名
                        name_element = block.find('div', class_='teacher-list-name')
                        if not name_element:
                            continue

                        name = name_element.get_text(strip=True)

                        # 提取資訊
                        info_elements = block.find_all('div', class_='teacher-list-info')
                        expertise = ""

                        for info in info_elements:
                            info_text = info.get_text(strip=True)
                            if '研究領域' in info_text:
                                expertise = info_text.split('研究領域：')[-1].strip()
                                break

                        if not expertise:
                            # 嘗試使用另一種方式提取研究領域
                            text = block.get_text()
                            match = re.search(r'研究領域[：:]\s*([\s\S]*?)(?=Office hour|網站|分機|$)', text)
                            if match:
                                expertise = match.group(1).strip()

                        # 處理專長格式
                        expertise = expertise.replace('\n', ' ').strip()
                        expertise = expertise.replace(', ', '、').replace('，', '、').replace(' ,', '、')
                        expertise = expertise.replace(',、', '、')

                        if name and expertise:
                            all_professors.append({
                                '姓名': name,
                                '專長': expertise
                            })
                            print(f"教授: {name}, 專長: {expertise[:50]}...")

                    except Exception as e:
                        print(f"處理教授區塊時出錯: {e}")
                        continue

        except Exception as e:
            print(f"爬取頁面時出錯: {e}")
            break

    return all_professors

def save_simple_output(professors_data, filename="professors_expertise_simple.txt"):
    with open(filename, 'w', encoding='utf-8') as txtfile:
        for professor in professors_data:
            name = professor['姓名'].strip()
            # 清理專長文字，移除多餘的內容
            expertise = professor['專長'].strip()
            # 移除任何包含'Share'、'Tweet'、'亞洲大學'等頁尾內容的部分
            expertise = re.sub(r'Share.*$', '', expertise, flags=re.DOTALL)
            expertise = re.sub(r'Print this page.*$', '', expertise, flags=re.DOTALL)
            expertise = re.sub(r'亞洲大學.*$', '', expertise, flags=re.DOTALL)
            expertise = re.sub(r'\d+\s*\d+\s*[上下]一頁.*$', '', expertise, flags=re.DOTALL)
            expertise = re.sub(r'最[前後].*$', '', expertise, flags=re.DOTALL)

            txtfile.write(f"教授: {name}, 專長: {expertise}\n")

    print(f"資料已保存至 {filename}")
    return filename  # 返回檔案名稱以供後續使用

def main():
    # 爬取各種類型的教授
    associate_professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/associate_professors_2")
    assistant_professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/assistant_professors_2")
    lecturers = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/senior_lecturer")
    professors = scrape_professors_expertise("https://csie.asia.edu.tw/zh_tw/all_professors_1")

    # 合併所有爬取的教授資訊
    all_professors = associate_professors + assistant_professors + lecturers + professors

    # 添加特殊案例（只添加一次）
    special_cases = [
        {"姓名": "Tadao Murata", "專長": "分散式通訊軟體、網路協議、邏輯與規則基礎AI系統、製造系統、平行計算系統和具有模糊延遲的系統的Petri網應用"},
        {"姓名": "曾憲章(Zeng Xianzhang)", "專長": "計算機科學"},
        {"姓名": "李錦輝(Chin-Hui Lee)", "專長": "語音訊號處理、機器學習"},
        {"姓名": "黃光彩", "專長": "電機工程"},
        {"姓名": "林一平(Jason Yi-Bing Lin)", "專長": "個人通信網路、行動計算、系統模擬"},
        {"姓名": "張嘉淵(Zhang Jiayuan)", "專長": "雲端運算、大數據分析、演算法、社群媒體、人工智慧物聯網、人本創新應用"},
        {"姓名": "許健(Gene Sheu)", "專長": "電子電路、微電子、產品研發、積體電路"},
        {"姓名": "梁文隆(Wen-Lung Liang)", "專長": "物聯網技術、嵌入式系統、智慧家庭"},
        {"姓名": "林詠章(Lin Yongzhang)", "專長": "資訊安全、區塊鏈應用、精準健康、智慧醫療、工控安全"}
    ]

    # 建立一個查詢集來避免重複
    seen_names = set()
    unique_professors = []

    # 先加入已爬取的教授
    for professor in all_professors:
        name = professor['姓名'].strip()
        # 忽略空的專長欄位的教授
        if name and professor['專長'].strip() and name not in seen_names:
            unique_professors.append(professor)
            seen_names.add(name)



    saved_file = save_simple_output(unique_professors)

    # 在Colab環境中提供下載選項
    try:
        from google.colab import files
        files.download(saved_file)
        print(f"\n檔案 {saved_file} 已準備好下載，請檢查瀏覽器下載提示。")
    except ImportError:
        print(f"\n程式執行完成！")
        print(f"檔案已儲存在當前目錄: {saved_file}")
        print(f"如果您在Colab中運行，請在左側文件瀏覽器找到並下載此檔案。")

if __name__ == "__main__":
    main()
