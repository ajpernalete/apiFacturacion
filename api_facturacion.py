import http.client
import mimetypes
conn = http.client.HTTPSConnection("dev-api.haulmer.com")
payload = """{
            "response":["PDF","FOLIO"],
            "dte":{"Encabezado":{
                                "IdDoc":{
                                        "TipoDTE":33,
                                        "Folio":0,
                                        "FchEmis":"2019-03-18",
                                        "TpoTranCompra":"1",
                                        "TpoTranVenta":"1",
                                        "FmaPago":"2"},
                                        "Emisor":{
                                                "RUTEmisor":"76795561-8",
                                                "RznSoc":"HAULMER SPA",
                                                "GiroEmis":"VENTA AL POR MENOR POR CORREO, POR INTERNET Y VIA TELEFONICA",
                                                "Acteco":"479100",
                                                "DirOrigen":"ARTURO PRAT 527   CURICO",
                                                "CmnaOrigen":"Curicó",
                                                "Telefono":"0 0",
                                                "CdgSIISucur":"81303347"
                                                },
                                        "Receptor":{
                                                    "RUTRecep":"76430498-5",
                                                    "RznSocRecep":"HOSTY SPA",
                                                    "GiroRecep":"ACTIVIDADES DE CONSULTORIA DE INFORMATIC",
                                                    "DirRecep":"ARTURO PRAT 527 3 pis OF 1",
                                                    "CmnaRecep":"Curicó"
                                                    },
                                        "Totales":{
                                                    "MntNeto":2000,
                                                    "TasaIVA":"19",
                                                    "IVA":380,
                                                    "MntTotal":2380,
                                                    "MontoPeriodo":2380,
                                                    "VlrPagar":2380
                                                    }
                                        },
                                "Detalle":[{
                                            "NroLinDet":1,
                                            "NmbItem":"item",
                                            "QtyItem":1,
                                            "PrcItem":2000,
                                            "MontoItem":2000
                                            }]
                    }
            }"""

headers = {
  'apikey': '928e15a2d14d4a6292345f04960f4bd3',
    "RUTEmisor":"76795561-8",
    "RznSoc":"HAULMER SPA",
    "GiroEmis":"VENTA AL POR MENOR EN EMPRESAS DE VENTA A DISTANCIA VÍA INTERNET; COMERCIO ELEC",
    "Acteco":479100,
    "DirOrigen":"ARTURO PRAT 527   CURICO",
    "CmnaOrigen":"Curicó",
    "CdgSIISucur":"81303347"
}
conn.request("POST", "/v2/dte/document", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))