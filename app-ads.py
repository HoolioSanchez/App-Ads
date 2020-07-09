#%%
import requests 
import pandas as pd
from io import StringIO

class AppAds:
    
    def getAppAds(self, url):
        r = requests.request("GET", url)

        return self.getDataFrame(r.text)

    def getDataframe(self, txt):
        return pd.read_csv(self.addStringDelimiator(txt), sep = ';', header=None, usecols=[0])

    def addStringDelimiator(self, txt):
        txt.replace("\n", ";")
        return StringIO(txt)


#%%
ads = AppAds()
link = "https://jamcity.com/app-ads.txt"

data = AppAds.getAppAds(link)

data.head()

# %%
