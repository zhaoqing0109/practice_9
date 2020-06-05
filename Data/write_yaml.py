import yaml

data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

# 将data写入到 当前目录下  ww.yml文件中
with open("./ww.yml", "a") as f:
    # 写yaml数据
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)
