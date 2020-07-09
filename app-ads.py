#%%
import requests 
import pandas as pd
from io import StringIO
from currentAppAds import unity_app_ads

class AppAds:
    
    def getAppAds(self, url):
        r = requests.request("GET", url)
        return self.getDataframe(r.text)

    def getDataframe(self, txt):
        return pd.read_csv(self.addStringDelimiator(txt), sep = ';', header=None, usecols=[0])

    def addStringDelimiator(self, txt):
        txt.replace("\n", ";")
        return StringIO(txt)

    def getMissingAppsAds(self, standardList, link):
        df = self.getAppAds(link)
        df1 = self.getDataframe(standardList)

        final = df1[~df1.apply(tuple,1).isin(df.apply(tuple,1))]

        return final
