import random

# --- Konfigurasi Gacha ---

# 1. Tentukan item untuk setiap rarity
#    Kuncinya adalah nama Rarity, nilainya adalah daftar (list) item
ITEM_POOL = {
    "Common": [
        "Pedang Kayu",
        "Perisai Kulit",
        "Ramuan Herbal",
        "Batu Kecil",
        "Sepatu Bot Tua",
    ],
    "Rare": [
        "Pedang Besi",
        "Perisai Baja",
        "Ramuan Ajaib",
        "Cincin Perak",
        "Jubah Petualang",
    ],
    "SSR": [
        "Pedang Legendaris Excalibur",
        "Perisai Naga Emas",
        "Mahkota Raja",
        "Staf Bintang Jatuh",
    ]
}

# 2. Tentukan probabilitas (rate) untuk setiap rarity
#    Total dari semua nilai harus 1.0 (mewakili 100%)
RARITY_RATES = {
    "Common": 0.70,  # 70%
    "Rare": 0.25,    # 25%
    "SSR": 0.05      # 5%
}

# --- Logika Inti Gacha ---

# Siapkan daftar rarity dan bobotnya untuk fungsi random.choices
# Ini hanya perlu dilakukan sekali
RARITIES = list(RARITY_RATES.keys())
WEIGHTS = list(RARITY_RATES.values())

def pull_gacha():
    """
    Melakukan satu kali pull gacha.
    Pertama, menentukan rarity, lalu memilih item dari rarity tersebut.
    """
    
    # Langkah 1: Tentukan rarity berdasarkan probabilitas (weights)
    # random.choices mengembalikan list, jadi kita ambil elemen pertama [0]
    chosen_rarity = random.choices(RARITIES, WEIGHTS, k=1)[0]
    
    # Langkah 2: Setelah dapat rarity, pilih item acak dari pool rarity tsb
    item_list_for_rarity = ITEM_POOL[chosen_rarity]
    chosen_item = random.choice(item_list_for_rarity)
    
    # Kembalikan item dan rarity-nya
    return chosen_item, chosen_rarity

def print_pull_result(item, rarity):
    """Mencetak hasil pull dengan format yang menarik."""
    
    if rarity == "SSR":
        print("\n==============================")
        print("    ✨✨✨ S S R ✨✨✨")
        print(f"  SELAMAT! ANDA MENDAPATKAN:")
        print(f"    {item}")
        print("==============================\n")
    elif rarity == "Rare":
        print("\n------------------")
        print("    ⭐! RARE !⭐")
        print(f"  Anda mendapatkan: {item}")
        print("------------------\n")
    else:
        # Untuk 'Common'
        print(f"  Anda mendapatkan: {item} ({rarity})\n")

def main():
    """Fungsi utama untuk menjalankan loop aplikasi."""
    print("🎉 Selamat Datang di Simulator Gacha Sederhana! 🎉")
    
    while True:
        print("Pilih tindakan:")
        print("  [1] Lakukan 1x Pull")
        print("  [2] Lakukan 10x Pull")
        print("  [3] Untuk berhenti")
        
        pilihan = input("Masukkan pilihan Anda: ").strip()

        if pilihan == '1':
            # --- PULL 1 KALI ---
            print("\nMemutar Gacha...")
            # Jeda sedikit untuk suspens
            # (bisa dihapus jika tidak mau)
            # import time; time.sleep(0.5) 
            
            item, rarity = pull_gacha()
            print_pull_result(item, rarity)

        elif pilihan == '2':
            # --- PULL 10 KALI ---
            print("\nMelakukan 10x Pull...\n")
            results = []
            ssr_count = 0
            
            for _ in range(10):
                item, rarity = pull_gacha()
                results.append((item, rarity))
                if rarity == "SSR":
                    ssr_count += 1
            
            # Opsi: Urutkan hasil agar yang paling langka ada di atas
            # (Ini umum di game gacha)
            results.sort(key=lambda x: ["SSR", "Rare", "Common"].index(x[1]))

            print("--- HASIL 10x PULL ---")
            for item, rarity in results:
                print(f"  [{rarity}] {item}")
            print("----------------------")
            
            if ssr_count > 0:
                print(f"✨ LUAR BIASA! Anda mendapatkan {ssr_count} item SSR! ✨")
            print("\n")

        elif pilihan.lower() == '3':
            print("Terima kasih telah bermain!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# --- Jalankan aplikasi ---
if __name__ == "__main__":
    main()