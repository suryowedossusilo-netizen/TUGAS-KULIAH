class TestPemainSepakbola {
    
    static main(args) {
        
        console.log("╔══════════════════════════════════════════════════════════════╗");
        console.log("║     SCENARIO PENGUJIAN CLASS PEMAIN SEPAKBOLA               ║");
        console.log("╚══════════════════════════════════════════════════════════════╝\n");
        console.log("═══════════════════════════════════════════════════════════════");
        console.log("  SCENARIO 1: PEMBUATAN OBJEK PEMAIN");
        console.log("═══════════════════════════════════════════════════════════════\n");

        const pemain1 = new PemainSepakbola("Lionel Messi", 10, "Penyerang", 36);

        PemainSepakbola pemain2 = new PemainSepakbola("Cristiano Ronaldo", 7, "Penyerang", 38, 85.0, 90.0);

        PemainSepakbola pemain3 = new PemainSepakbola("Erling Haaland", 9, "Penyerang", 23, 95.0, 88.0);

        pemain1.cetakInfo();
        System.out.println();
        pemain2.cetakInfo();
        System.out.println();
        pemain3.cetakInfo();

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 2: PENGGUNAAN SETTER DAN GETTER");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        System.out.println("Sebelum diubah:");
        System.out.println("  Nama Pemain 1: " + pemain1.getNama());
        System.out.println("  Nomor Punggung: " + pemain1.getNomorPunggung());
        System.out.println("  Posisi: " + pemain1.getPosisi());

        pemain1.setNama("Lionel Messi (Inter Miami)");
        pemain1.setNomorPunggung(30);
        pemain1.setPosisi("Playmaker");
        
        System.out.println("\nSetelah diubah:");
        System.out.println("  Nama Pemain 1: " + pemain1.getNama());
        System.out.println("  Nomor Punggung: " + pemain1.getNomorPunggung());
        System.out.println("  Posisi: " + pemain1.getPosisi());

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 3: SIMULASI PERTANDINGAN");
        System.out.println("═══════════════════════════════════════════════════════════════\n");

        System.out.println("--- Cek Kelayakan Main ---");
        pemain1.cekKelayakanMain();
        pemain2.cekKelayakanMain();
        pemain3.cekKelayakanMain();
        
        System.out.println("\n--- Pertandingan Dimulai ---\n");
        
        pemain1.cetakGol();
        pemain1.cetakGol();
        pemain2.cetakGol();
        pemain3.cetakGol();
        pemain3.cetakGol();
        pemain3.cetakGol();
        
        System.out.println();

        pemain1.beriAssist();
        pemain2.beriAssist();
        pemain2.beriAssist();
        
        System.out.println();

        pemain2.beriKartuKuning();
        pemain3.beriKartuKuning();
        
        System.out.println();

        System.out.println("--- Statistik Setelah Pertandingan ---\n");
        pemain1.cetakStatistik();
        System.out.println();
        pemain2.cetakStatistik();
        System.out.println();
        pemain3.cetakStatistik();

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 4: GANTI POSISI PEMAIN");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        pemain1.gantiPosisi("Gelandang Serang");
        pemain2.gantiPosisi("Penyerang Tengah");
        
        System.out.println("\nPosisi Pemain 1 sekarang: " + pemain1.getPosisi());
        System.out.println("Posisi Pemain 2 sekarang: " + pemain2.getPosisi());

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 5: LATIHAN DAN ISTIRAHAT");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        System.out.println("Stamina sebelum latihan: " + pemain1.getStamina());
        pemain1.latihan();
        pemain1.latihan();
        System.out.println("Stamina setelah latihan: " + pemain1.getStamina());
        
        System.out.println();
        pemain1.istirahat();
        System.out.println("Stamina setelah istirahat: " + pemain1.getStamina());

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 6: KARTU MERAH (PEMAIN DIKELUARKAN)");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        pemain3.beriKartuMerah();
        System.out.println("Status main Pemain 3: " + (pemain3.isStatusMain() ? "Bermain" : "Cadangan/Diskors"));

        System.out.println();
        pemain3.cekKelayakanMain();

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 7: PERBANDINGAN STATISTIK ANTAR PEMAIN");
        System.out.println("═══════════════════════════════════════════════════════════════");
        
        pemain1.bandingkanStatistik(pemain2);

        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 8: VALIDASI INPUT");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        System.out.println("Mencoba set kecepatan ke 150 (melebihi batas):");
        pemain1.setKecepatan(150);
        
        System.out.println("\nMencoba set stamina ke -10 (di bawah batas):");
        pemain1.setStamina(-10);
        
        System.out.println("\nMencoba set kecepatan ke 75 (valid):");
        pemain1.setKecepatan(75);
        System.out.println("Kecepatan sekarang: " + pemain1.getKecepatan());
        
        System.out.println("\n═══════════════════════════════════════════════════════════════");
        System.out.println("  SCENARIO 9: RINGKASAN AKHIR SEMUA PEMAIN");
        System.out.println("═══════════════════════════════════════════════════════════════\n");
        
        pemain1.cetakInfo();
        pemain1.cetakStatistik();
        System.out.println();
        
        pemain2.cetakInfo();
        pemain2.cetakStatistik();
        System.out.println();
        
        pemain3.cetakInfo();
        pemain3.cetakStatistik();
        
        System.out.println("\n╔══════════════════════════════════════════════════════════════╗");
        System.out.println("║           PENGUJIAN SELESAI - SEMUA SCENARIO BERHASIL          ║");
        System.out.println("╚══════════════════════════════════════════════════════════════╝");
    }
}