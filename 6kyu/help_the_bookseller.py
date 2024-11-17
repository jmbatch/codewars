# https://www.codewars.com/kata/54dc6f5a224c26032800005c/python

def stock_list(stocklist, categories):
    category_count = dict.fromkeys(categories, int(0))
    for item in stocklist:
        item_parts = item.split()
        category_code = item_parts[0][0]
        quantity = int(item_parts[1])
        
        if category_code in categories:
            category_count[category_code] += quantity
            
    if sum(category_count.values()) == 0:
        return ""
    
    return " - ".join(f"({key} : {value})" for key, value in category_count.items())


b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
c = ["A", "B", "C", "W"]

print(stock_list(b, c))

# "(A : 20) - (B : 114) - (C : 50) - (W : 0)"