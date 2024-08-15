import bs4
import requests as rq
from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get('/test')
def request() :
    web = rq.get('https://www.goldtraders.or.th/UpdatePriceList.aspx')
    soup = bs4.BeautifulSoup(web.text , "html.parser")
    table = soup.find('table',{'id':'DetailPlace_MainGridView'})
    tr = table.find_all('tr')
    array_name = ['เวลา','ครั้งที่','ทองแท่งรับซื้อ (บาท)','ทองแท่งขายออก (บาท)','ทองรูปพรรณรับซื้อ (บาท)','ทองรูปพรรณขายออก (บาท)','Gold Spot','Baht / US$	','ขึ้น / ลง']
    output = {}
    count = 1
    for data in tr[2:] :
        count_value = 0
        data_output_dict = {}
        for value in data.find_all('td') :
            data_output_dict[array_name[count_value]] = value.text
            count_value = count_value + 1
        output[count] = data_output_dict
        count = count + 1
    return output

if __name__ == "__main__" :
    uvicorn.run(app,host="185.199.111.153",port=3456)
