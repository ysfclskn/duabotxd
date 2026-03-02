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
