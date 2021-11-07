import yaml
from config.setting_path import case_data
class Get_yaml_data():
    def __init__(self,file_path):
        self.path =file_path
    #读取yaml中所有数据，返回字典格式
    def get_all_data(self):
        with open(self.path,encoding='utf-8') as f:
            data =yaml.load(f,Loader=yaml.FullLoader)
            return data
    #获取元素
    def get_element(self,i):
        data =self.get_all_data()
        return data['testcase'][i]['element_info']
    #定位元素的方法
    def find_type(self,i):
        data = self.get_all_data()['testcase'][i]['find_type']

    #执行操作
    def operate_type(self,i):
        return self.get_all_data()['testcase'][i]['operate_type']

if __name__ =='__main__':
    a = a = Get_yaml_data(case_data + "/" + "Login_data.yaml").test_data_value("detail")
    print(a)
