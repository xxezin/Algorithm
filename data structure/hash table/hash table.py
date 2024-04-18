# 리스트 변수를 이용해 해쉬 테이블 구현해보기
hash_table = list(0 for i in range(8))

def get_key(data):
    return hash(data)

def hash_fuction(key):
    return key%8

def save_data(data,value):
    hash_address = hash_fuction(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_fuction(get_key(data))
    return hash_table[hash_address]

save_data('YJ','1212321321')
save_data('JJ','3424342524')
print(read_data('YJ'))

