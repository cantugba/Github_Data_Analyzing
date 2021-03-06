from RequestToApi.GithubData import GithupApi
import json


# function to add to JSON
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


    # Her ay ayrı ayrı çekildiği için GithubData.py dosyasındaki urlyi ilgili aya göre değiştirip diğer mainlerde de aynısı yapılacak
    # # Ekim Ayı
    # filename1 = 'JsonDatas/OctoberDatas/data.json'
    # filename2 = 'JsonDatas/OctoberDatas/data1.json'

    # # Kasım Ayı
    # filename1 = 'JsonDatas/NovemberDatas/data.json'
    # filename2 = 'JsonDatas/NovemberDatas/data1.json'
if __name__ == '__main__':
    # Aralık Ayı
    filename1 = 'JsonDatas/DecemberDatas/data.json'
    filename2 = 'JsonDatas/DecemberDatas/data1.json'

    obj_list = list()
    for github_page in range(1, 11):
        githup = GithupApi(page_number=github_page)
        obj_list.append(githup.datas)

    #print(obj_list)
    write_json(obj_list,filename1)

    obj_list2 = list()
    # page_number = 11
    for github_page in range(11, 21):
        githup = GithupApi(page_number=github_page)
        obj_list2.append(githup.datas)

    #print(obj_list2)
    write_json(obj_list2,filename2)

