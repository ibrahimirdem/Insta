import requests, re
class Insta:
    def link(self, url):
        #veri ='<meta property="og\:image" content="(.*?)" />'
        data = requests.get(url)
        try:
            img_download_link = re.findall('<meta property="og\:image" content="(.*?)" />',data.text)[0]
            img_download_name = re.findall('<meta property\="al\:android\:url" content\="https://www\.instagram\.com/p/(.*?)/" />',data.text)[0]
        except IndexError as hata:
            print('Image not found: ',hata)

        with open(str(img_download_name) + '.jpg', 'wb') as f:
            f.write(requests.get(img_download_link).content)

    def info(self, name):
        link = "https://www.instagram.com/"+name.replace(" ","")+"/"
        data = requests.get(link)
        veri = data.text
        sonucJson = re.findall('<script type="text/javascript">window._sharedData = (.*?)</script>',veri)
        username = re.findall('\[\{"user": \{"username": "(.*?)"',sonucJson[0])[0]
        posts = re.findall('media": \{"count": (.*?)\,',sonucJson[0])[0]
        follows = re.findall('follows": \{"count": (.*?)\}\,',sonucJson[0])[0]
        followed_by = re.findall('followed_by": \{"count": (.*?)\}\,',sonucJson[0])[0]
        #profile_pic_url = re.findall('"profile_pic_url_hd": "(.*?)"\,',sonucJson[0])[0]

        sozluk = {
            "username":username,
            "posts":posts,
            "follows":follows,
            "followed_by":followed_by,
        #    "profile_pic_url":profile_pic_url
        }

        return sozluk

    def all(self,name):
        url = "https://www.instagram.com/"+name+"/"
        link = url
        saydir=0
        while True:
            data = requests.get(link)
            data = data.text
            sonuc = re.findall('"is_video"\: (.*?)\, "id"\: "(.*?)"\, "display_src"\: "(.*?)"',data)
            next_link = "https://www.instagram.com/"+name+"/?max_id="+re.findall('"end_cursor"\: "(.*?)"',data)[0]
            for item in sonuc:
                img_download_link = item[2]
                img_download_name = item[1]
                with open(str(img_download_name) + '.jpg', 'wb') as f:
                    f.write(requests.get(img_download_link).content)
                saydir=saydir+1
                print(saydir)

            link = next_link
            if len(sonuc)<12:
                break
