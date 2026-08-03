# ==============================================================================
# HisabDo AI/ML Internship Bootcamp - Day 2 Task
# Project: Student Data Analysis with Pandas
# ==============================================================================

# 1. KÜTÜPHANENİN İÇERİ AKTARILMASI (IMPORT)
# 'import pandas as pd' komutu ile Pandas kütüphanesini kodumuza dahil ediyoruz.
# 'as pd' kısmı, kütüphaneyi her kullandığımızda uzunca 'pandas' yazmak yerine kısaca 'pd' yazmamızı sağlar.
import pandas as pd


def create_student_dataset():
    """10 öğrencilik veri setini dictionary olarak oluşturur ve Pandas DataFrame'e dönüştürür."""

    # 2. VERİ SETİNİN PYTHON DICTIONARY (SÖZLÜK) YAPISINDA OLUŞTURULMASI
    # 'Key' (Anahtar) kısımları sütun isimlerimiz (Name, Age, Course, Marks),
    # 'Value' (Değer) kısımları ise köşeli parantez [] içindeki listelerimizdir.
    student_data = {
        "Name": [
            "Alice", "Bob", "Charlie", "David", "Emma",
            "Frank", "Grace", "Hannah", "Ian", "Jack"
        ],
        "Age": [24, 22, 21, 23, 26, 22, 21, 24, 27, 23],
        "Course": [
            "AI/ML", "Data Science", "AI/ML", "Web Dev", "AI/ML",
            "Data Science", "Cyber Security", "AI/ML", "Web Dev", "Data Science"
        ],
        "Marks": [85, 62, 90, 78, 55, 95, 68, 74, 88, 59]
    }

    # 3. DICTIONARY STRUCTURE'IN PANDAS DATAFRAME'E DÖNÜŞTÜRÜLMESİ
    # pd.DataFrame() komutu düz liste/sözlük verisini alıp Excel gibi Satır ve Sütunlardan oluşan tabloya çevirir.
    df = pd.DataFrame(student_data)
    return df
# ------------------------------------------------------------------------------
# 4. VERİ ANALİZİ FONKSİYONU (DATA ANALYSIS FUNCTIONS)
# ------------------------------------------------------------------------------
def analyze_student_data(df):
    """Ödevde istenen 6 farklı analizi gerçekleştirir ve ekrana basar."""

    print("=" * 60)
    print(" 📊 HISABDO AI/ML BOOTCAMP - DAY 2 STUDENT DATA ANALYSIS")
    print("=" * 60)

    # 1️⃣ İSTENEN: Tüm Öğrencileri Ekrana Basma
    print("\n1️⃣ ALL STUDENTS DATASET:")
    # print(df) komutu tablonun tamamını düzenli bir şekilde ekrana yazar.
    print(df.to_string(index=False))  # 'index=False' sol baştaki 0,1,2 satır numaralarını gizler, temiz görünür.

    # 2️⃣ İSTENEN: Notu 70'in Üzerinde Olan Öğrenciler (Filtreleme)
    # df['Marks'] > 70 ifadesi sadece koşulu sağlayan satırları getirir.
    print("\n" + "-" * 60)
    print("2️⃣ STUDENTS WITH MARKS ABOVE 70:")
    high_scorers = df[df['Marks'] > 70]
    print(high_scorers.to_string(index=False))

    # 3️⃣ İSTENEN: Not Ortalamasını Hesaplama
    # .mean() yöntemi seçilen sütunun aritmetik ortalamasını alır.
    # :.2f yapısı virgülden sonra sadece 2 basamak gösterir (Örn: 75.30).
    average_marks = df['Marks'].mean()
    print("\n" + "-" * 60)
    print(f"3️⃣ AVERAGE MARKS OF ALL STUDENTS: {average_marks:.2f}")

    # 4️⃣ İSTENEN: En Yüksek Notu Alan Öğrenciyi Bulma
    # .idxmax() en yüksek notun hangi satırda (indekste) olduğunu bulur.
    # .loc[...] ise o satırdaki tüm bilgileri (İsim, Yaş, Kurs vb.) getirir.
    top_student = df.loc[df['Marks'].idxmax()]
    print("\n" + "-" * 60)
    print(f"4️⃣ HIGHEST SCORING STUDENT:")
    print(f"   Name: {top_student['Name']} | Mark: {top_student['Marks']} | Course: {top_student['Course']}")

    # 5️⃣ İSTENEN: En Düşük Notu Alan Öğrenciyi Bulma
    # .idxmin() en düşük notun bulunduğu satırı tespit eder.
    lowest_student = df.loc[df['Marks'].idxmin()]
    print("\n" + "-" * 60)
    print(f"5️⃣ LOWEST SCORING STUDENT:")
    print(f"   Name: {lowest_student['Name']} | Mark: {lowest_student['Marks']} | Course: {lowest_student['Course']}")

    # 6️⃣ İSTENEN: Toplam Öğrenci Sayısı
    # len(df) tablodaki toplam satır sayısını verir.
    total_students = len(df)
    print("\n" + "-" * 60)
    print(f"6️⃣ TOTAL NUMBER OF STUDENTS: {total_students}")
    print("=" * 60)


# ------------------------------------------------------------------------------
# 5. PROGRAMI ÇALIŞTIRMA NOKTASI (MAIN EXECUTION)
# ------------------------------------------------------------------------------
def main():
    # Veri setini oluşturup 'student_df' değişkenine kaydediyoruz.
    student_df = create_student_dataset()
    
    # Oluşturduğumuz tabloyu analiz fonksiyonumuza gönderiyoruz.
    analyze_student_data(student_df)


if __name__ == "__main__":
    main()