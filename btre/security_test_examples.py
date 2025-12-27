"""
TEST DOSYASI - SUNUM İÇİN ÖRNEK GÜVENLİK SORUNLARI
Bu dosya sadece Bandit analiz testi için oluşturulmuştur.
Gerçek projede kullanılmamalıdır.
"""

# TEST 1: Hardcoded API Key (B106)
# Bandit bu tür hardcoded API key'leri tespit eder
# NOT: GitHub secret scanning'i tetiklememek için gerçek API key formatı kullanılmadı
API_KEY = "test_api_key_1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD = "my_super_secret_password_12345"

# TEST 2: eval() kullanımı (B307)
# eval() kullanımı güvenlik riski oluşturur çünkü kullanıcı girdisini çalıştırabilir
def calculate_expression(expression):
    """
    UYARI: Bu fonksiyon sadece test amaçlıdır!
    Gerçek projede eval() kullanılmamalıdır.
    """
    # Bandit bu satırı güvenlik riski olarak işaretleyecek
    result = eval(expression)  # noqa: B307
    return result

# TEST 3: Shell injection riski (B602) - Bonus olarak ekledim
# subprocess ile shell=True kullanımı güvenlik riski oluşturur
import subprocess

def run_command(user_input):
    """
    UYARI: Bu fonksiyon sadece test amaçlıdır!
    Gerçek projede shell=True kullanılmamalıdır.
    """
    # Bandit bu satırı güvenlik riski olarak işaretleyecek
    subprocess.call(user_input, shell=True)  # noqa: B602

