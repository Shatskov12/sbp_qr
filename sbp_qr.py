import requests
import qrcode  # pip3 install pillow qrcode

url = "qr.nspk.ru"
path_api_function = "/payment/v1/qrc-data"
data = {
    "agentId": "",  # "A00000000001",
    "memberId": "",  # "100000000001",
    "account": "",  # "40702810100010000001",
    "merchantId": "",  # "MF0000000001",
    "templateVersion": "",  # "01",
    "qrcType": "",  # "02",
    "amount": "",  # "100000",
    "currency": "",  # "RUB",
    "qrTtl": "",  # "60"время жизни ссылки
    "paymentPurpose": "",  # "Капучино 300 мл 1 шт., булочка 1 шт.",
    "subscriptionPurpose": "",  # "Оплата завтраков в Кофейне у Артема",
    "fraudScore": "",  # "0000000000000000",
    "redirectUrl": "",  # "https://exampletsp.io/qwertyui"
}

try:
    resp = requests.post(url + path_api_function, data=data)
    qr_url = resp.json()["data"]["payload"]
except Exeption:
    print(Exeption)

# имя конечного файла
filename = "sbp.png"
# генерируем qr-код
img = qrcode.make(qr_url)
# сохраняем img в файл
img.save(filename)