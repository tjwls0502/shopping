from pathlib import Path
from urllib.request import urlretrieve

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)

myWget("shopA.txt")

def shopping(shop_file):
    
    with open('data/shopA.txt', mode='r', encoding='utf-8') as f:
      lines = f.readlines()
      shop_dict = {}
      list_str = ' '.join(s for s in lines)
      list_str = list_str.split()
    
      for i in range(2,len(list_str),2):
        shop_dict[list_str[i]] = int(list_str[i+1][:-1])

    return shop_dict

def item_price(shop_file, item):
    
    with open('data/shopA.txt', mode='r', encoding='utf-8') as f:
      lines = f.readlines()
      shop_dict = {}
      list_str = ' '.join(s for s in lines)
      list_str = list_str.split()
    
      for i in range(2,len(list_str),2):
        shop_dict[list_str[i]] = int(list_str[i+1][:-1])

    return shop_dict[item]