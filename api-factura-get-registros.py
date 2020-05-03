import http.client
import mimetypes
conn = http.client.HTTPSConnection("dev-api.haulmer.com")
boundary = ''
payload = ''
headers = {
  'apikey': '928e15a2d14d4a6292345f04960f4bd3',
  'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("GET", "/v2/dte/registry/purchase/2020/05/03?status=pending,registered", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))