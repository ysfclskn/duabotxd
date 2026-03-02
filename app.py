import streamlit as st
import random

# Sayfa Yapılandırması
st.set_page_config(page_title="Kurumsal Dua Botu v3.0", page_icon="🤲")

class KurumsalDuaMerkezi:
    def __init__(self):
        self.dualar = [
            # --- Önceki 30 Dua ---
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

            # --- YENİ EKLENEN 10 DUA ---
            "Allah'ım, 'Aslında biz bir aileyiz' denilen şirketlerdeki fazla mesailerden beni koru.",
            "Rabbim, yan masada durmadan sakız çiğneyen arkadaşıma sabır, bana sükunet ver.",
            "İlahi, revize üstüne revize isteyen müşterinin bilgisayarına 'update' gönder, beni unutsun.",
            "Yarabbi, maaş zammı konuşulurken yöneticimin 'Bütçemiz kısıtlı' bahanesini dilinden düşür.",
            "Allah'ım, 'Training' adı altında hafta sonu yapılan kamplardan beni uzak eyle.",
            "Rabbim, sabah kahve makinesinin bozulduğu günlerde bana ekstra enerji ihsan eyle.",
            "Ya İlahi, bayram tatili ile hafta sonu birleştiğinde 'o gün çalışıyoruz' diyenlerden beni koru.",
            "Allah'ım, yanlışlıkla gruba attığım ekran görüntüsünü kimse görmeden 'herkesten sil'meme yardım et.",
            "Rabbim, terfi listesinde adımı en üstte, işten çıkarma listesinde en altta eyle.",
            "İlahi, emeklilik hayallerimi kurarken dolar kurunun sabit kalmasını nasip eyle. Amin."
        ]

    def dua_ver(self):
        return random.choice(self.dualar)

# Arayüz Oluşturma
bot = KurumsalDuaMerkezi()

st.title("💼 Kurumsal Manevi Destek Botu v3.0")
st.markdown(f"**Şu an kütüphanede {len(bot.dualar)} adet profesyonel temenni bulunuyor.**")

if st.button("🤲 Bir Dua Et / Temenni Al"):
    dua = bot.dua_ver()
    st.info(dua)
    st.snow() # Kış temalı veya balonlu efekt

st.sidebar.caption("Mesai saatleri içerisinde kullanılması tavsiye edilir.")