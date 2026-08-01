# ==============================================================================
# HisabDo AI/ML Internship Bootcamp - Day 1 Task
# Project: Interactive Student Profiler
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. FONKSİYON TANIMLAMA (FUNCTIONS)
# ------------------------------------------------------------------------------
# 'def' kelimesi Python'a "Ben yeni bir komut/paket tanımlıyorum" der.
# 'display_welcome_message' bizim fonksiyona verdiğimiz İngilizce isimdir.
# Bu fonksiyonun tek görevi ekrana şık bir karşılama metni yazmaktır.
def display_welcome_message():
    # 'print()' parantez içindeki metinleri ekrana basmaya yarayan hazır Python komutudur.
    # "=" * 50 ifadesi 50 tane '=' işaretini yanyana basarak çizgi çeker.
    print("=" * 50)
    print(" 🚀 WELCOME TO HISABDO AI/ML BOOTCAMP - DAY 1 ")
    print("=" * 50)


# ------------------------------------------------------------------------------
# 2. KOŞUL MANTIĞI VE FONKSİYON (IF / ELIF / ELSE)
# ------------------------------------------------------------------------------
# Bu fonksiyon parantez içinde 'level' adında bir bilgi (parametre) bekler.
# Kullanıcının girdiği seviyeye göre ona özel bir İngilizce mesaj hazırlar.
def evaluate_experience_level(level):
    
    # '.lower()' komutu kullanıcının yazdığı metni küçük harfe çevirir. 
    # Böylece kullanıcı "BEGINNER", "Beginner" veya "beginner" yazsa da kod şaşırmaz.
    # '==' işareti "Eşit mi?" kontrolü yapar.
    
    # 'if' -> "Eğer kullanıcının seviyesi 'beginner' ise:" demektir.
    if level.lower() == "beginner":
        return "Great choice! Building a strong foundation is the key to mastering AI."
    
    # 'elif' -> "Değilse ama 'intermediate' ise:" demektir.
    elif level.lower() == "intermediate":
        return "Awesome! You are ready to dive deeper into data manipulation and algorithms."
    
    # 'elif' -> "Değilse ama 'advanced' ise:" demektir.
    elif level.lower() == "advanced":
        return "Impressive! Focus on advanced architectures and model optimization."
    
    # 'else' -> "Yukarıdakilerin hiçbiri değilse (kullanıcı başka bir şey yazdıysa):" demektir.
    else:
        return "Welcome aboard! Consistency will take you far in this journey."


# ------------------------------------------------------------------------------
# 3. ANA PROGRAM MANTIĞI (MAIN FUNCTION)
# ------------------------------------------------------------------------------
# Bütün adımları sırayla çalıştıracağımız ana merkezimiz.
def main():
    
    # Adım A: Karşılama fonksiyonumuzu çağırıp ekrana bastırıyoruz.
    display_welcome_message()

    # Adım B: Kullanıcıdan Bilgi Alma (Input) ve Değişkenlerde (Variables) Saklama
    # 'input()' komutu bilgisayarı durdurur ve kullanıcının klavyeden yazı yazıp ENTER'a basmasını bekler.
    # 'student_name' ve 'experience_level' kutucuklardır (değişken). Yazılan yazıyı hafızada tutarlar.
    student_name = input("Enter your name: ")
    experience_level = input("Enter your experience level (Beginner/Intermediate/Advanced): ")

    # Adım C: Liste (List) Oluşturma
    # Köşeli parantez [] içinde virgüllerle ayrılmış veri grubuna Liste denir.
    # Öğrenilecek konuları 'bootcamp_topics' isimli listenin içine koyduk.
    bootcamp_topics = [
        "Python Fundamentals & Logic",
        "Version Control with Git & GitHub",
        "Data Analysis (NumPy & Pandas)",
        "Machine Learning Concepts",
        "Deep Learning & Generative AI"
    ]

    # Adım D: Ekrana Profil Bilgilerini Yazdırma
    # 'f"..."' yapısı metnin içine değişkenleri kolayca gömmemizi sağlar. {student_name} yerine girilen isim basılır.
    print("\n" + "-" * 50)
    print(f"👤 Student Profile: {student_name}")
    
    # 'evaluate_experience_level' fonksiyonuna kullanıcının seviyesini yolluyoruz.
    # Fonksiyondan gelen sonucu 'feedback_message' değişkeninde saklıyoruz.
    feedback_message = evaluate_experience_level(experience_level)
    print(f"💡 Status: {feedback_message}")
    print("-" * 50)

    # Adım E: Döngü (Loop) Kullanarak Listeyi Ekrana Basma
    # 'for' komutu bir listedeki elemanları teker teker gezmeye yarar.
    # 'enumerate(..., start=1)' listenin her elemanına 1, 2, 3 diye sıra numarası verir.
    print("\n📚 Topics You Will Master in this Track:")
    for index, topic in enumerate(bootcamp_topics, start=1):
        # Her döngü turunda 'index' sira numarasini, 'topic' ise o siradaki konuyu tutar.
        print(f"   {index}. {topic}")

    # Programın başarıyla bittiğini bildiren son çıktı.
    print("\n✅ Day 1 Task execution completed successfully!")
    print("=" * 50)


# ------------------------------------------------------------------------------
# 4. PROGRAMI BAŞLATICI (ENTRY POINT)
# ------------------------------------------------------------------------------
# Bu 2 satır Python'ın standart kuralıdır. "Bu dosya çalıştırıldığında doğrudan main() fonksiyonunu başlat" der.
if __name__ == "__main__":
    main()