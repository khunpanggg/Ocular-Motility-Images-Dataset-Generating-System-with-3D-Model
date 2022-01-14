import requests


def download_file(id):
    url = 'https://api.polyhaven.com/files/'+id
    r = requests.get(url, allow_redirects=True, verify=False)
    # print(r.json())

    data = r.json()
    download_url = data['hdri']['4k']['hdr']['url']
    r = requests.get(download_url, allow_redirects=True, verify=False)

    open(id+'.hdr', 'wb').write(r.content)

# url = 'https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/2k/abandoned_church_2k.hdr'
# r = requests.get(url, allow_redirects=True, verify=False)

# open('pang.hdr', 'wb').write(r.content)


assets_url = 'https://api.polyhaven.com/assets?t=hdris&c=outdoor'
r = requests.get(assets_url, allow_redirects=True, verify=False)
# print(r.json())

assets_id = r.json().keys()
# print(assets_id)

# id_lst = ['abandoned_parking', 'abandoned_pathway']
for i in assets_id:
    download_file(i)
