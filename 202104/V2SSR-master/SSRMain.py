from SSR.Scrapy_SSR import SSR

if __name__ == "__main__":
    ssr = SSR()
    SSRURL = ssr.GetHtmlText()
    ssr.SaveFileSub(SSRURL)
    ssr.SaveFileLink(SSRURL)