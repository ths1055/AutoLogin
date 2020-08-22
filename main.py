import base64
id="fsr2103"
idU=id.encode("UTF-8")
idEn=base64.b64encode(idU)
idEn1=idEn.decode("utf8")
print(idEn1)
idDe=base64.b64decode(idEn1)
idUde=idDe.decode("UTF-8")
print(idUde)