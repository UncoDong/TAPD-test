import pytest
import json

json_file = open("test_file.json",'r',encoding='gbk')  
a = json.load(json_file)
# 读取数据
testname_list = []
for i in range(len(a)):
    testname_list.append('test{0}'.format(i))


# 进行测试
@pytest.mark.parametrize('test_name', testname_list)
def test_str2note(test_name):
    print(a[test_name])
