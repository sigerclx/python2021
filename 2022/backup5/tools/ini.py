import configparser
#读取ini方法
def read_ini(inivaluse,inikey='param'):
        config = configparser.ConfigParser()
        config.read("config.ini",encoding="utf-8-sig")
        try:
            convaluse=config.get(inikey,inivaluse)

            return convaluse
        except Exception as err:
            print(err)