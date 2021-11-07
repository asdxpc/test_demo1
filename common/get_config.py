import configparser
from config import setting_path

class Get_config():
    def __init__(self):
        self.path = setting_path.conf_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.path)

    #读取配置文件
    def read_config(self,option,section):
        data = self.conf.get(option,section)
        return data

    # 写入配置
    def write_config(self,section,option,value):
        self.conf.add_section(section)
        self.conf.set(section,option,value)
        # 修改文件后需要写入保存
        self.conf.write(open(self.path,"w"))

    def remove_config(self,section):
        self.conf.remove_section(section)
        # 修改文件后需要写入保存
        self.conf.write(open(self.path, "w"))


if __name__ == "__main__":
    print(setting_path.conf_path)
    a = Get_config().read_config("URL","test_url")
    print(a)