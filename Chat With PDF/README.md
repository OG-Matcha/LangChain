# NCU_Fresh_Web_ChatBot

## 使用說明

*  確保電腦有 Python 環境(這邊我沒有用 Docker 你們直接去官網裝就好)
*  在 VsCode 中建立虛擬環境 (Ctrl+Shift+P 選建立 Python 環境)
*  選取建立 venv，相依套件選擇 requirements.txt
*  請根據 .env.example 撰寫新的 .env
*  申請 OpenAI API Key

   1. 請先至[官網](https://openai.com/index/openai-api/)進行註冊帳號及登錄
   2. 登入完成後在左邊側欄找到 **API keys**
   3. 點進去後按下**Create new **secret** key**
   4. 名字隨便寫、Project 選 Default、Permission 開 All

> [!IMPORTANT]
請記得一定要複製生成的 API KEY，將他複製到你創建好的 .env 的 OPEN_API_KEY 的字串內

* 確保你現在終端機在虛擬環境下
* 在和 app.py 同路徑下終端機輸入 `streamlit run app.py` 即可看到跳出的網頁，輸入問題案查詢即可看到回答

## 問題範例
1. 圖書館甚麼時候開放
2. 我要如何請假
3. 學習護照的畢業門檻是多少
4. 我要怎麼拿密碼卡
5. 我可以如何啟動電算中心帳號
6. 宿網要多少錢
7. 自行車有甚麼規定嗎
8. 哪邊可以申請自行車證
9. 新生健檢在甚麼時候
10. 有哪些學校授權軟體可以使用
11. ideaNCU是甚麼 
