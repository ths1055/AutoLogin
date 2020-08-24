import base64
class b64ed:
    def b64Encode(self, bfEnString1):
        bfEnString2=bfEnString1.encode("UTF-8")
        afEnString1=base64.b64encode(bfEnString2)
        afEnString2=afEnString1.decode("UTF-8")
        return afEnString2

    def b64Decode(self,bfDeString1):
        bfDeString2=bfDeString1.encode("UTF-8")
        afDeString1=base64.b64decode(bfDeString2)
        afDeString2=afDeString1.decode("UTF-8")
        return afDeString2

