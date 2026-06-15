// Jvdroid-main: 
// Jvdroid-main: 
// ============================================================
// File: Pintu.java
// Kelas Pintu dengan respons acak saat dibuka/ditutup
// ============================================================

import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

public class Pintu {
    private boolean status;
    private Random random;
    private String[] responBuka = {
        "🚪 Pintu terbuka dengan suara berdecit...",
        "🚪 Pintu terbuka halus tanpa suara.",
        "🚪 Pintu terbuka dengan keras! BANG!",
        "🚪 Pintu terbuka perlahan dengan suara misterius...",
        "🚪 Pintu terbuka dan angin sejuk masuk.",
        "🚪 Pintu terbuka dengan bunyi 'CREEEEAK' lama.",
        "🚪 Pintu terbuka, ada seseorang di baliknya?!",
        "🚪 Pintu terbuka dengan mudah, seolah mengundang masuk."
    };
    
    private String[] responTutup = {
        "🚪 Pintu ditutup dengan lembut...",
        "🚪 Pintu ditutup dengan keras! BAM!",
        "🚪 Pintu ditutup dan terkunci otomatis.",
        "🚪 Pintu ditutup dengan suara berdecit aneh.",
        "🚪 Pintu ditutup, suasana menjadi sunyi.",
        "🚪 Pintu ditutup dengan bunyi 'THUD' berat.",
        "🚪 Pintu ditutup, tapi ada suara ketukan dari luar!",
        "🚪 Pintu ditutup rapat, aman dan nyaman."
    };
    
    public Pintu() {
        this.status = false;
        this.random = new Random();
    }
    
    public Pintu(boolean statusAwal) {
        this.status = statusAwal;
        this.random = new Random();
    }
    
    public void buka() {
        if (status) {
            System.out.println("⚠️  Pintu sudah terbuka! Tidak perlu dibuka lagi.");
        } else {
            status = true;

            int indeksAcak = random.nextInt(responBuka.length);
            System.out.println(responBuka[indeksAcak]);
            System.out.println("   Status: PINTU TERBUKA ✅\n");
        }
    }
    
    public void tutup() {
        if (!status) {
            System.out.println("⚠️  Pintu sudah tertutup! Tidak perlu ditutup lagi.");
        } else {
            status = false;

            int indeksAcak = random.nextInt(responTutup.length);
            System.out.println(responTutup[indeksAcak]);
            System.out.println("   Status: PINTU TERTUTUP ❌\n");
        }
    }
    

    public boolean isTerbuka() {
        return status;
    }
    
    public String getStatus() {
        return status ? "TERBUKA" : "TERTUTUP";
    }
    
    public void cetakInfo() {
        System.out.println("╔══════════════════════════════════════╗");
        System.out.println("║           INFORMASI PINTU            ║");
        System.out.println("╠══════════════════════════════════════╣");
        System.out.println("║ Status: " + String.format("%-27s", getStatus()) + "║");
        System.out.println("╚══════════════════════════════════════╝");
    }
}