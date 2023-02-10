# Bağış Yardım Kontrol yazılımı

bu proje depremde bağış yapılmak istenen paralara bile ağızı sulanan yavşakların engellenebilmesi amacı ile yapılmaya başlanmıştır. Google bot`u yardım toplayan siteleri google aramalardan keyword'e göre bulup ihtiyaca göre kullanılabilmesini sağlamayı amaçlamaktadır.

Dolandırıcı sitelerin ayıklanması ve engellenmesi tamamiyle otomatize edilmesi ilgili birimlerle çalışarak sağlanılması amaçlanmaktadır. Bu projeye destek vermekten çekinmeyin GPL-3 lisansı altında başlatılmıştırher türlü fikir öneri ve pull request'e açığım eğer böyle bir proje varsada bildirin elimden gelirse desteklerim.

## Sistem Mimarisi

Proje ihtiyaca göre socket, message broker veya text olarak çıktı alınarak kullanılabilir elimden geldiğince açık olarak yapacağım zaten google arama yapıldığında keyword'e göre alınan link'i nasıl kullanacağınız fonksiyonu değiştirerek yapmanız mümkün.

en son hangi siteler alınmışsa tekrar aynı verinin gönderilmesini engellemek için en son alınan veri kaydedilecektir ve karşılaştırılacaktır. Dolandırıcı sitelerin başlangıç olarak ilk sayfada çıkması engellenmesi amaçlanmaktadır. Google bot'u her saniye kontrol edemeyeceği bir durum olursa veya aynı requestin aynı adresden tekrar tekrar gönderilmesi bir sorun oluşturması durumunda bu projenin her replikasının birbiri ile aynı orchestratrasyon yazılımında farklı ip adresleri ile çalışabilmeside beklenebilir.

## Bağımlılıklar

### Programlama Dili

 - Python3.x

### Kütüphaneler

 - BeautifulSoup4
 - Requests


