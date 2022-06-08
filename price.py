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
    ...
    with open('data/shopA.txt', mode='r', encoding='utf-8') as f:
      lines = f.readlines()
      shop_dict = {}
      list_str = ' '.join(s for s in lines)
      list_str = list_str.split()
    
      for i in range(2,len(list_str),2):
        shop_dict[list_str[i]] = int(list_str[i+1][:-1])

    return shop_dict[item]