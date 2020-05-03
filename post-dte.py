import http.client
import mimetypes
conn = http.client.HTTPSConnection("dev-api.haulmer.com")
payload = "{  \n   \"Page\":\"5\",\n   \"TipoDTE\":{  \n      \"eq\":\"33\"\n   },\n   \"FchEmis\":{  \n      \"lte\":\"2019-01-31\",\n      \"gte\":\"2018-12-01\"\n   }\n}"
headers = {
  'apikey': '928e15a2d14d4a6292345f04960f4bd3',
  'Content-Type': 'application/json'
}
conn.request("POST", "/v2/dte/document/issued", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))