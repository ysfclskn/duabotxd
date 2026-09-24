import streamlit as st
import random
from st_supabase_connection import SupabaseConnection

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(page_title="Kurumsal Manevi Destek Botu v0.4", page_icon="🤲")

# --- SUPABASE BAĞLANTISI ---
# Not: .streamlit/secrets.toml dosyanızda bağlantı bilgileriniz olmalı
conn = st.connection("supabase", type=SupabaseConnection)

def get_stats():
    """Veritabanından toplam amin sayısını çeker."""
    query = conn.table("global_stats").select("current_value").eq("stat_name", "total_amen_count").execute()
    return query.data[0]['current_value']

def update_counter():
    """Sayacı veritabanında 1 artırır."""
    current_val = get_stats()
    conn.table("global_stats").update({"current_value": current_val + 1}).eq("stat_name", "total_amen_count").execute()

prayers = [
    "Allah'ım, 'Aslında bir e-posta olabilirdi' dediğim tüm toplantıları takvimimden sil.",
    "Rabbim, Excel tablolarımı #SAYI/0! ve #BAŞV! hatalarından koru.",
    "İlahi, 'Push etmek', 'Align olmak' gibi plaza terimlerini lügatimden sonsuza dek temizle.",
    "Yarabbi, Cuma saat 17:55'te gelen 'acil' revize taleplerini gönderenin inbox'ında kaybet.",
    "Rabbim, Zoom'da kameram açık unutulunca yaptığım mimikleri yöneticimden gizle.",
    "Ya İlahi, 'Müsait olduğunda bir konuşalım mı?' mesajının arkasından zam haberi gelmesini sağla.",
    "Rabbim, beni 'Reply All' kazalarından ve yanlış kişiye giden dedikodu mesajlarından koru.",
    "Yarabbi, Slack bildirim sesini duyduğunda kalbi sıkışan kuluna ferahlık nasip eyle.",
    "Allah'ım, 'CC'ye eklenen gereksiz kalabalığın kalbine bir 'Ayrılma' isteği düşür.",
    "Ya Vedüd, sunumum esnasında internetimin kopmasına, bilgisayarımın donmasına izin verme.",
    "IT departmanına attığım taleplerin 'çözüldü' olarak dönmesini nasip et.",
    "'Kaydetmeden kapattım' dediğim dosyaların 'Otomatik Kurtarma' ile geri gelmesini sağla.",
    "Bilgisayarımın 180°C olup fan sesiyle beni sağır etmesine engel ol.",
    "Şarj kablomun kopmamasını, mouse'umun pilinin bitmemesini nasip eyle.",
    "Maaşımın bereketini artır, enflasyon canavarına karşı cüzdanımı çelikten eyle.",
    "Bana 'Seni aramızda görmekten mutluluk duyarız' diyen, maaşı dolgun bir iş teklifi gönder.",
    "Performans görüşmelerinde yöneticimin gözüne perde indir, sadece başarılarımı görmesini sağla.",
    "İstifa dilekçemi masanın üzerinde gururla bıraktığım o günü göster.",
    "Sadece çok çalışana değil, doğru kişinin 'gözüne girene' verdiğin o terfiden bana da damlat.",
    "Promosyon ödemelerinin ve ikramiyelerin yattığı günkü o huzuru daim kıl.",
    "Yemekhanede bugün 'karnabahar' değil, gerçek bir 'İskender' nasip et.",
    "Pazartesi sendromunu benim için 'Cuma neşesi' kıvamına getir.",
    "Açık ofiste durmadan konuşan o çalışma arkadaşımın çenesine 'Mute' butonu ekle.",
    "Yıllık izne çıktığımda telefonumun çekmediği ıssız koylar nasip et.",
    "Sabah alarmını duymadığım günlerde yöneticimin benden önce ofise gelmemesini sağla.",
    "Mutfaktaki ortak sütü kendi kahvesine bitirene hidayet nasip eyle.",
    "LinkedIn ana sayfamı 'Gurur duyuyorum' diyenlerden temizle.",
    "'Networking' ayağına yapılan o sıkıcı etkinliklerden beni muaf tut.",
    "Servis aracının ben durağa varmadan gitmesine izin verme.",
    "Mesaim bittiğinde 'Acaba bir şey unuttum mu?' korkusunu benden uzak eyle.",
    "Allah'ım, 'Aslında biz bir aileyiz' denilen şirketlerdeki fazla mesailerden beni koru.",
    "Rabbim, yan masada durmadan sakız çiğneyen arkadaşıma sabır, bana sükunet ver.",
    "İlahi, revize üstüne revize isteyen müşterinin bilgisayarına 'update' gönder, beni unutsun.",
    "Yarabbi, maaş zammı konuşulurken yöneticimin 'Bütçemiz kısıtlı' bahanesini dilinden düşür.",
    "Allah'ım, 'Training' adı altında hafta sonu yapılan kamplardan beni uzak eyle.",
    "Rabbim, sabah kahve makinesinin bozulduğu günlerde bana ekstra enerji ihsan eyle.",
    "Ya İlahi, bayram tatili ile hafta sonu birleştiğinde 'o gün çalışıyoruz' diyenlerden beni koru.",
    "Allah'ım, yanlışlıkla gruba attığım ekran görüntüsünü kimse görmeden 'herkesten sil'meme yardım et.",
    "Rabbim, terfi listesinde adımı en üstte, işten çıkarma listesinde en altta eyle.",
    "İlahi, emeklilik hayallerimi kurarken dolar kurunun sabit kalmasını nasip eyle.",
    "Allah'ım, toplantı esnasında 'bence' diye söze başlayıp konuyu 20 dakika uzatan kuluna hidayet ver.",
    "Rabbim, Zoom'da ekran paylaşırken arkada açık kalan özel sekmelerimi iş arkadaşlarımdan gizle.",
    "İlahi, ofis klimasının derecesini 'Erzurum soğuğu'na ayarlayanlarla beni sınama.",
    "Yarabbi, kredi kartı ekstresi gelince yaşadığım o 'Ben bu kadar ne ara harcadım?' şokunu hafiflet.",
    "Allah'ım, 'İş-yaşam dengesi' lafını sadece slaytlarda değil, hayatımda da görmeyi nasip et.",
    "Rabbim, shifre yenileme zamanı geldiğinde 'eski şifrenizle aynı olamaz' uyarısına karşı sabrımı artır.",
    "Ya İlahi, yöneticimin 'Ben bunu aslında şöyle hayal etmiştim' diyerek her şeyi sildirdiği o andan beni koru.",
    "Allah'ım, Pazartesi sabahı atılan 'Hafta sonun nasıl geçti?' sorusuna samimiyetle cevap verme gücü ver.",
    "Rabbim, tabldotta çıkan 'gizemli et yemeği'nin ne olduğunu anlamayı ve sağ salim sindirmeyi nasip eyle.",
    "İlahi, her cümlesine 'Asap' (ASAP) ekleyen kulunu tez vakitte dinginliğe ulaştır.",
    "Yarabbi, sadece 'Merhaba' yazıp yazmaya devam etmeyen kişilerin eline hız ver.",
    "Allah'ım, Cuma günü öğleden sonra gelen 'ufak bir sorumuz var' mailini spam klasörüne düşür.",
    "Rabbim, 'Deneyim kazandık' denilerek maaş zammı yapılmayan senelerden beni halas eyle.",
    "İlahi, 'Kapatıp açtınız mı?' sorusunu duymadan sorunlarımın çözüldüğü o günleri göster.",
    "Yarabbi, masamdan ödünç alınıp bir daha dönmeyen tükenmez kalemlerimin hesabını ahirete bırakma.",
    "Allah'ım, mutfakta dedikodu yaparken arkamdan yöneticimin belirmesine izin verme.",
    "Rabbim, sabah 5'te kalkıp soğuk duş alan ve bunu Linkedin'de anlatan motivasyoncuların şerrinden koru.",
    "İlahi, WFH gününde kapımın çalmasını ve kuryeyle kapıda felsefe yapmamı engelle.",
    "Yarabbi, piyangodan büyük ikramiye çıksın da 'Saygılarımla' yazan o maili 'Saygısızca' olarak göndereyim.",
    "Allah'ım, latte içerken yan masadaki arkadaşımın 'Süt köpüğü kilo yapar mı?' sorusuna sabır ver.",
    "Rabbim, hiçbir veriye dayanmayan ama 'hissiyatla' yapılan o strateji toplantılarından beni muaf tut.",
    "İlahi, logoyu 2 piksel sağa, sonra tekrar 2 piksel sola aldıran müşterinin ufkunu genişlet.",
    "Yarabbi, hafta sonu gruptan gelen 'Pazartesiye yetişir mi?' mesajını görmeme yetisi ver.",
    "Allah'ım, ütüsüz gömlekle ofise gittiğim gün 'Casual Friday' ilan edilmesini nasip et.",
    "Rabbim, asansörde sadece yöneticimle kaldığım o 30 saniyelik derin sessizliği bozacak zeka ver.",
    "İlahi, tatil fotoğraflarımın altına 'Dönünce görüşelim, işler birikti' yazan arkadaşımı uzak eyle.",
    "Yarabbi, 'High-level' konuşup aslında hiçbir şey anlatmayanların seviyesine beni indirme.",
    "Allah'ım, takvimimde üst üste binen 3 toplantıdan en az ikisinin iptal olmasını nasip eyle.",
    "Rabbim, 'Bilginize' (FYI) notuyla üzerime yıkılan işleri 'Gereği yapılamadı' olarak iade etmeyi nasip et.",
    "İlahi, yan hak olarak verilen 'Meyve Günü' yerine gerçek bir 'Özel Sağlık Sigortası' nasip eyle.",
    "Yarabbi, stajyerin fotokopi makinesini bozduğu o anki masumiyetine karşı öfkemi dindir.",
    "Allah'ım, hedeflerimin gerçekleşme oranını yöneticimin boyundan, maaş zammını kilomdan büyük eyle.",
    "Rabbim, bel fıtığı riski taşımayan, her oturduğumda 'bulutlardaymışım' hissi veren bir koltuk nasip et.",
    "İlahi, 'Ofis dışındayım' mesajı aktifken mail atanların bilgisayarına kum kaçır.",
    "Yarabbi, 'Beyin fırtınası' adı altında yapılan meltem esintilerinden bizi koru.",
    "Allah'ım, ofise gelen kişisel kargolarımın 'Acaba içinde ne var?' bakışlarından korunmasını sağla.",
    "Rabbim, servis aracında klimanın tam üzerime üflediği o kronik sinüzit sancısından beni kurtar.",
    "İlahi, yıllık iznimi onaylamayan yöneticinin tatil beldesinde yağmura yakalanmasını nasip et.",
    "Yarabbi, VLOOKUP (Düşeyara) yaparken doğru sütunu bulamayan kuluna feraset ver.",
    "Allah'ım, emekli olup sahil kasabasına yerleştiğimde bu botu silecek kadar huzur nasip et. Amin."
    "Allah'ım, 'Kısaca üzerinden geçelim' deyip 1 saat konuşan toplantıları takvimimden buharlaştır.",
    "Rabbim, staging ortamında çalışan şeylerin prod'da da çalışmasını nasip eyle.",
    "İlahi, 'Bunu canlıda bir deneyelim' diyen cesur ruhlardan beni koru.",
    "Yarabbi, deploy sonrası gelen 'Bir şeyler bozuldu galiba' mesajlarını hayra çevir.",
    "Rabbim, test ortamındaki mock dataların gerçeğe dönüşmesini sağla.",
    "Allah'ım, Jira'da bana yazılan 'Ufak bir task'ların epik çıkmamasını nasip et.",
    "Ya İlahi, sprint planlamasında story pointlerimi hafif, beklentileri düşük eyle.",
    "Rabbim, 'Bu çok basit aslında' diye başlayıp 3 gün süren işleri bana yazma.",
    "İlahi, cache temizleyince düzelen bug'ları kalıcı olarak ortadan kaldır.",
    "Yarabbi, 'Bu neden böyle olmuş?' sorusunun cevabını commit geçmişinde bulmayı nasip et.",
    "Allah'ım, production loglarını okurken gözlerime hikmet ver.",
    "Rabbim, feature flag'leri açıp kapatırken yanlış ortamı seçmekten beni muhafaza eyle.",
    "İlahi, Slack'te yazdığım mesajı silmeden önce 3 kez düşünmeyi nasip et.",
    "Yarabbi, 'Toplantı kaydı var mıydı?' sorusunu sormak zorunda kalmayayım.",
    "Allah'ım, demo günü internetimin hızını fiber, stresimi minimum eyle.",
    "Rabbim, hotfix attığım gün başka bug çıkmamasını nasip et.",
    "İlahi, test case yazarken 'Bunu da düşünmemişiz' demek zorunda kalmayayım.",
    "Yarabbi, API response'larının 200 dönüp içinin boş gelmemesini sağla.",
    "Allah'ım, flaky testleri stabilize edecek sabrı ve bilgiyi ihsan eyle.",
    "Rabbim, CI/CD pipeline'ının kırmızı değil yeşil akmasını nasip et.",
    "İlahi, kod review'da 'Bunu biraz refactor edelim' cümlesini az duyayım.",
    "Yarabbi, 'Quick call alabilir miyiz?' mesajını görmezden gelme gücü ver.",
    "Allah'ım, 15 dakikalık toplantının gerçekten 15 dakika sürmesini nasip et.",
    "Rabbim, tatildeyken gelen 'Sadece bir sorum var' mesajlarını bana göstermeden çöz.",
    "İlahi, backlog'taki eski ticket'ların bir mucizeyle kapanmasını sağla.",
    "Yarabbi, 'Bu bug user kaynaklı' diyebilme özgürlüğü ver.",
    "Allah'ım, commit mesajlarımı anlamlı, geçmişimi temiz eyle.",
    "Rabbim, rebase yaparken conflict yaşamadan merge etmeyi nasip et.",
    "İlahi, yanlış branch'e push etmeme engel ol.",
    "Yarabbi, 3 farklı ortamın config'lerini karıştırmaktan beni koru.",
    "Allah'ım, test datasını canlıdan çekme gafletine düşürme.",
    "Rabbim, 'Scope değişti' cümlesini sprint ortasında duymayayım.",
    "İlahi, müşteri demo'sunda çalışmayan feature'ı bana yaşatma.",
    "Yarabbi, 'Bir şey soracağım ama çok kısa' deyip uzun konuşanlara sabır ver.",
    "Allah'ım, sabah standup'ta söyleyecek mantıklı bir cümle bulmayı nasip et.",
    "Rabbim, 6 aylık projeyi 2 haftaya sıkıştıran planlardan bizi uzak eyle.",
    "İlahi, Excel'e manuel veri girmek zorunda kaldığım günleri azalt.",
    "Yarabbi, 'Ekran dondu' diyen kullanıcının aslında refresh yapmamış olmasını sağla.",
    "Allah'ım, rapor sunarken grafiklerimin anlamlı görünmesini nasip et.",
    "Rabbim, 17 farklı WhatsApp iş grubundan sessizce çıkabilmeyi nasip et.",
    "İlahi, maaş günü gelen banka bildiriminin yüzümü güldürmesini sağla.",
    "Yarabbi, laptop'umun güncelleme için en kritik anı seçmemesini nasip et.",
    "Allah'ım, 'Bunu bir de mobilde deneyelim' dendiğinde layout'un bozulmamasını sağla.",
    "Rabbim, password manager'ımın beni yüzüstü bırakmamasını nasip et.",
    "İlahi, 'Bu tasarım Figma'da güzel duruyordu' diyenleri affetmem için kalbimi genişlet.",
    "Yarabbi, zoom'da ismimin yanlış yazılmamasını nasip et.",
    "Allah'ım, toplantı davetindeki gereksiz 23 kişiden biri olmamayı nasip et.",
    "Rabbim, 'Şirket kültürü' adı altında yapılan anlamsız aktivitelerden beni koru.",
    "İlahi, hafta içi mesaimi verimli, hafta sonumu bildirim sessiz eyle.",
    "Yarabbi, emekli olduğum gün Slack hesabımın sonsuza dek pasif kalmasını nasip et."
    "Allah'ım, WFH gününde apartman matkabını sustur, huzuru evime indir.",
    "Rabbim, 'Evden çalışıyorsun nasılsa' diyerek verilen ekstra işleri görünmez eyle.",
    "İlahi, kameram kapalıyken attığım esnemeleri kimseye gösterme.",
    "Yarabbi, Teams'te mikrofonum kapalıyken 5 dakika konuştuğumu fark etmeyi nasip et.",
    "Allah'ım, 'Sesim geliyor mu?' sorusunu toplantıda en fazla bir kez sordurt.",
    "Rabbim, internetimin en kritik demo anında değil, gece 03:00'te kopmasını nasip eyle.",
    "İlahi, evdeki sandalyemi ergonomik, belimi sağlam eyle.",
    "Yarabbi, pijama altıyla çıktığım toplantıda ayağa kalkmamı gerektirecek durumlar yaratma.",
    "Allah'ım, kapıya gelen kuryenin zilini standup esnasında değil, molada çaldır.",
    "Rabbim, ev halkının 'Bir bakar mısın şuna?' çağrılarını sprint bitimine ertele.",
    "İlahi, Slack durumum 'Away' iken bana mention atılmamasını sağla.",
    "Yarabbi, kahve makinemin toplantı öncesi bozulmamasını nasip et.",
    "Allah'ım, ekran paylaşırken yanlış pencereyi açma gafletinden beni koru.",
    "Rabbim, arka planda çalan çamaşır makinesinin sesiyle rezil olmaktan muhafaza eyle.",
    "İlahi, 'Remote ama ofise de bekleriz' diyen yöneticilere basiret ver.",
    "Yarabbi, Zoom arka planımı gerçek sananlara hakikati göster.",
    "Allah'ım, evde çalışırken buzdolabıyla aramdaki mesafeyi irade ile uzat.",
    "Rabbim, öğle molasını gerçekten mola yapabilmeyi nasip et.",
    "İlahi, gün boyu oturmanın verdiği hantallığı benden uzaklaştır.",
    "Yarabbi, VPN bağlantımı sabit, sinirlerimi daha da sabit eyle.",
    "Allah'ım, elektrik kesintisini deploy saatine değil, tatil gününe yaz.",
    "Rabbim, ev internetimin hızını upload'da da download kadar güçlü eyle.",
    "İlahi, kamera açınca donan yüzümü HD değil, yumuşak filtreli göster.",
    "Yarabbi, 'Remote culture' deyip 7 saat toplantı yapanlardan bizi koru.",
    "Allah'ım, Slack'te yazdığım ironinin yanlış anlaşılmamasını nasip et.",
    "Rabbim, gün içinde 12 farklı platformdan gelen bildirimlere karşı kalbimi sağlamlaştır.",
    "İlahi, toplantı linkini son saniye aramak zorunda bırakma.",
    "Yarabbi, ev ofisimin kablolarını düğüm değil, düzen eyle.",
    "Allah'ım, ekran karşısında geçen saatleri verimli, gözlerimi sağlıklı eyle.",
    "Rabbim, 'Bir quick sync yapalım' denilen mesajları yarın sabaha tehir et.",
    "İlahi, remote çalışırken görünmez emeklerimin görünür olmasını sağla.",
    "Yarabbi, online performans görüşmesinde yüz ifademi nötr, maaş beklentimi net eyle.",
    "Allah'ım, Teams'te yanlış emojiye basma gafletinden beni koru.",
    "Rabbim, toplantı sırasında gelen aile WhatsApp mesajlarını yanlış ekrana yansıtmayayım.",
    "İlahi, masa başında atıştırdığım abur cuburların kalori hesabını affet.",
    "Yarabbi, sabah alarmından 5 dakika önce gelen bildirimlerle uyanmayayım.",
    "Allah'ım, remote çalışmayı bahane edip hafta sonu task atanlardan bizi muhafaza eyle.",
    "Rabbim, evdeyim diye 24 saat ulaşılabilir sanılmaktan beni kurtar.",
    "İlahi, aynı gün içinde 4 farklı 'catch-up' toplantısından en az ikisini iptal ettir.",
    "Yarabbi, ekran karşısında geçen ömrüme denge, ruhuma ferahlık ver.",
    "Allah'ım, uzaktan çalışırken kariyerimin uzaktan gitmemesini nasip et.",
    "Rabbim, ofise çağrıldığım gün trafik değil, hafif esinti nasip et.",
    "İlahi, home office masamı dağınıklıktan, zihnimi karmaşadan arındır.",
    "Yarabbi, 'Remote ama kamera açık' zorunluluğuna karşı sabır ver.",
    "Allah'ım, deploy esnasında modem resetlemek zorunda kalmayayım.",
    "Rabbim, evdeki Wi-Fi şifresini her gelen misafire tekrar anlatma sabrı ver.",
    "İlahi, remote çalışırken sosyal bağlarımı da koparmadan denge kurmayı nasip et.",
    "Yarabbi, arka plandaki kedinin klavyeme basıp mesaj göndermesini engelle.",
    "Allah'ım, online sunum yaparken 'Sesin kesildi' cümlesini duymayayım.",
    "Rabbim, remote hayatın konforunu, plaza hayatın stresine değişmeyecek bilgelik ver.",
    "Allah'ım, cuma günü 16:59'da gelen 'Pazartesiye kadar yetişir mi?' mesajını gönderenin aklına salı günü düşür.",
"Rabbim, 'Sende iki dakikalık iş' denilen görevlerin gerçekten iki dakika sürmesini nasip et.",
"İlahi, toplantıdan toplantıya koşarken arada bir bardak su içecek vakit ihsan eyle.",
"Yarabbi, 'Son bir değişiklik' sözünün ardından gerçekten son değişikliğin gelmesini sağla.",
"Allah'ım, izin dönüşü inbox'ımı üç haneli sayılarla sınama.",
"Rabbim, herkesin onayladığı tasarımın geliştirme bitince yeniden tartışılmasına engel ol.",
"İlahi, 'Bende çalışıyor' diyen arkadaşımın ekranını da görmeyi nasip et.",
"Yarabbi, bug'ı yeniden üretmek için gereken o esrarengiz adımı bana göster.",
"Allah'ım, test ortamına girdiğimde şifresi değişmiş tek kişi ben olmayayım.",
"Rabbim, otomasyon koşarken geçen testlerin sayısını artır, flaky olanların bahanesini azalt.",
"İlahi, pipeline kırıldığında sebebini son commit'te bulmayı nasip et.",
"Yarabbi, release gününde unutulmuş feature flag'leri vaktinde hatırlat.",
"Allah'ım, 'Bu bug daha önce de vardı' cümlesini kanıtlayacak ekran görüntüsünü bana buldur.",
"Rabbim, API dokümanındaki örnek response ile gerçek response'u birbirine yaklaştır.",
"İlahi, sprint sonuna bir gün kala açılan 'küçük kapsam değişikliği'nden bizi koru.",
"Yarabbi, demo sırasında dün çalışan butonun bugün de çalışmasını nasip et.",
"Allah'ım, yöneticimin 'Bir bakar mısın?' mesajının yanında biraz bağlam da göndermesini sağla.",
"Rabbim, öğle arasında başlayan toplantının gerçekten öğle arası bitmeden sona ermesini nasip et.",
"İlahi, sessize aldığım mikrofonu konuşmaya başlamadan önce açmayı aklıma getir.",
"Yarabbi, maaş zammı görüşmesinde gösterdiğim emeğin 'görünürlük' diye geçiştirilmesine izin verme."
]
# --- ÖZEL BUTON TASARIMI ---
st.markdown("""
    <style>

    /* Butonun ana stili */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); /* Şık bir mor-mavi gradyan */
        color: white !important;
        padding: 20px 40px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 50px !important; /* Tam yuvarlak köşeler */
        border: none !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }

    /* Mouse üzerine gelince (Hover) */
    .stButton > button:hover {
        transform: scale(1.05); /* Hafif büyüme efekti */
        box-shadow: 0 15px 25px rgba(118, 75, 162, 0.4) !important;
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%); /* Gradyanı ters çevir */
    }

    /* Tıklama anı */
    .stButton > button:active {
        transform: scale(0.98);
    }

    /* Standart Streamlit çerçevelerini kaldırmak için */
    .stButton > button:focus:not(:active) {
        border-color: transparent !important;
        color: white !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 50px;
        font-weight: 800;
        background: -webkit-linear-gradient(#667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 18px;
        color: #555;
        text-align: center;
        font-style: italic;
        margin-top: -20px;
    }
        .stApp {
      background-color: #0e1117;
        color: #fafafa;
    }
    </style>
    <h1 class="main-title">Kurumsal Manevi Destek Botu</h1>
    <p class="sub-title">Kurumsal dertlerine dijital merhem...</p>
""", unsafe_allow_html=True)

st.divider()
st.markdown(f"Şu an kütüphanede {len(prayers)} adet profesyonel temenni bulunuyor.")
if st.button("🤲 Amin De ve Dua Al"):
    try:
        update_counter()
        selected_prayer = random.choice(prayers)

        # Şık bir HTML kartı
        st.markdown(f"""
                <div style="
                    background-color: #f0f2f6; 
                    padding: 30px; 
                    border-radius: 15px; 
                    border-left: 10px solid #4CAF50;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    margin: 20px 0;">
                    <h4 style="color: #1f77b4; margin-top: 0;">✨ Günün Temennisi</h4>
                    <p style="font-size: 20px; font-style: italic; color: #31333F; line-height: 1.6;">
                        "{selected_prayer}"
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.balloons()
    except:
        st.error("Bir hata oluştu ama aminlerin kalbimizde!")

st.divider() # Araya ince bir çizgi çeker

try:
    total_count = get_stats()
    st.info(f"☁️ Şu ana kadar tam **{total_count:,}** adet dua edildi. Kurumsal dertler derya, aminler imdat oldu...")
except:
    st.caption("🚨 Maneviyat sunucularımıza şu an ulaşılamıyor ama dualarınızın hala geçerliliği var. Sabredin...")

st.caption("v0.4 | Mesai bitimine daha çok var, sakin ol.")

with st.popover("ℹ️ Bilgi"):
    st.markdown("### Kurumsal Manevi Destek")
    st.info("Mesai saatleri içerisinde kullanılması tavsiye edilir. ( Tamamen mizah amaçlıdır ) :)")
    st.write("Sürüm: v0.4")
