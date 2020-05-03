import http.client
import mimetypes
# Import only b64decode function from the base64 module
from base64 import b64decode
import ast

conn = http.client.HTTPSConnection("dev-api.haulmer.com")
payload = ''
headers = {
  'apikey': '928e15a2d14d4a6292345f04960f4bd3'
}
conn.request("GET", "/v2/dte/document/98904de41159ec5987bf20b6094a5cc7b6c8188c43a3cb99acd10ed5b9cc0856/pdf", payload, headers)
res = conn.getresponse()
data = res.read()

pdf = {}
pdf = data.decode('utf-8')
mydata = ast.literal_eval(pdf)
#print()

b64 = mydata.get('pdf')
# Decode the Base64 string, making sure that it contains only valid characters
bytes = b64decode(b64, validate=True)

# Perform a basic validation to make sure that the result is a valid PDF file
# Be aware! The magic number (file signature) is not 100% reliable solution to validate PDF files
# Moreover, if you get Base64 from an untrusted source, you must sanitize the PDF contents
if bytes[0:4] != b'%PDF':
  raise ValueError('Missing the PDF file signature')

# Write the PDF contents to a local file
f = open('PDF/Prueba3.pdf', 'wb')
f.write(bytes)
f.close()