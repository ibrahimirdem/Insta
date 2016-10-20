# Insta

Instagram resim indirme sınıfı.

##### NOT: 
Bu sınıfı kullanabilmek için requests modülünü yüklemelisiniz.

```sh
$ pip3 install requests
```
### Örnekler
Bir Instagram kullanıcısının bütün resimlerini indirmek için:
```py
import insta
instagram = insta.Insta()
instagram.all("username")
#'username':Resimlerinin indirilmesini istediğimiz instagram adresi
```
Bir Instagram resim linkini indirmek için:
```py
import insta
instagram = insta.Insta()
instagram.link('https://www.instagram.com/p/BLxv-xojCYu/')
```
Bir kullanıcı hakkında bilgiler almak için:
```py
import insta
instagram = insta.Insta()
instagram.info('cats_of_instagram')
#Çıktı: {'followed_by': '7003100', 'posts': '6264', 'follows': '6', 'username': 'cats_of_instagram'}
```
