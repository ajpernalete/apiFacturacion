import http.client
import mimetypes
# Import only b64decode function from the base64 module
from base64 import b64decode
import ast

conn = http.client.HTTPSConnection("dev-api.haulmer.com")
boundary = ''
payload = ''
headers = {
  'apikey': '928e15a2d14d4a6292345f04960f4bd3',
  'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("GET", "/v2/dte/document/76423895-8/34/396/pdf", payload, headers)
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
f = open('ejemplo.pdf', 'wb')
f.write(bytes)
f.close()
