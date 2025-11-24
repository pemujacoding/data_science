import pandas as pd
import joblib

def condition_input(input) :
    condition_map = {
        'butuh renovasi': 0,
        'sudah renovasi': 1,
        'bagus': 2,
        'bagus sekali': 3,
        'baru': 4
    }
    condition_val = condition_map[input.lower()]
    return  condition_val

def furnishing_input(input) :
    furnishing_map = {
        'unfurnished': 0,
        'semi furnished': 1,
        'furnished': 2,
        'fully furnished': 2
    }
    furnishing_val = furnishing_map[input.lower()]
    return furnishing_val

def facilities_input(input) :
    with open("../mlb_facilities.pkl", "rb") as f:
        mlb = joblib.load(f)

        fac_encoded = mlb.transform([input])

        fac_df = pd.DataFrame(fac_encoded, columns=mlb.classes_)
        return fac_df

def city_input(input) :
    with open('../le_city.pkl', 'rb') as f:
        city_encoder = joblib.load(f)
        return city_encoder.transform([input])

def district_input(input) :
    with open('../le_district.pkl', 'rb') as f:
        district_encoder = joblib.load(f)
        return district_encoder.transform([input])

def get_district() :
    teks = """
    'Summarecon Bekasi' 'Bekasi' 'Setu' 'Harapan Indah' 'Bekasi Kota'
    'Cibitung' 'Cibubur' 'Mustikajaya' 'Jatisampurna' 'Jatiwarna'
    'Pondok Gede' 'Jaka Setia' 'Jati Asih' 'Grand Wisata' 'Jatibening'
    'Bekasi Utara' 'Rawalumbu' 'Tambun Selatan' 'Harapan Baru' 'Pondokmelati'
    'Babelan' 'Kemang Pratama' 'Jatiraden' 'Bekasi Timur' 'Jatiwaringin'
    'Tarumajaya' 'Cikarang Selatan' 'Kebalen' 'Kayuringin Jaya' 'Bintara'
    'Jatirangga' 'Cikarang' 'Jati Mekar' 'Duta Harapan' 'Jati Sari' 'Pejuang'
    'Galaxy' 'Tanah Tinggi' 'Jaka Sampurna' 'Bekasi Barat' 'Tambun Utara'
    'Kaliabang' 'Mustikasari' 'Cimuning' 'Caman' 'Cikunir' 'Satriajaya'
    'Pondok Ungu' 'Pekayon' 'Harapan Mulya' 'Harapan Jaya' 'Perwira'
    'Jatikramat' 'Jatimurni' 'Jatimelati' 'Karang Satria' 'Kranji'
    'Margahayu' 'Serang Baru' 'Duren Jaya' 'Jati Luhur' 'Jababeka' 'Komsen'
    'Jatiranggon' 'Narogong' 'Bantar Gebang' 'Jatimakmur' 'Jati Cempaka'
    'Golden City' 'Pedurenan' 'Medan Satria' 'Pasirmulya' 'Cilendek Timur'
    'Sentul City' 'Cileungsi' 'Kemang' 'Ciomas' 'Gunung Sindur' 'Bojong Gede'
    'Kedung Halang' 'Tapos' 'Cibinong' 'Sentul' 'Sukaraja' 'Tanah Sareal'
    'Ciparigi' 'Mulyaharja' 'Katulampa' 'Bogor Barat' 'Gunung Putri'
    'Cilendek Barat' 'Tamansari' 'Kota Wisata' 'Bojongsari' 'Curug'
    'Babakan Madang' 'Bojong' 'Cimahpar' 'Tanah Baru'
    'Bogor Nirwana Residence' 'Tegallega' 'Parung Panjang' 'Cikeas' 'Parung'
    'Cilebut' 'Baranangsiang' 'Dramaga' 'Rancamaya' 'Legenda Wisata'
    'Bojong Kulur' 'Tajur Halang' 'Cipayung' 'Ciluar' 'Cipanas' 'Megamendung'
    'Limusnunggal' 'Cijeruk' 'Citeureup' 'Ciapus' 'Tajur' 'Pasir Kuda'
    'Ciawi' 'Karang Tengah' 'Bukit Sentul' 'Sindang Barang' 'Citaringgul'
    'Bantar Jati' 'Cilendek' 'Pasirlaja' 'Semplak' 'Cibuluh' 'Kedungwaringin'
    'Leuwinanggung' 'Kedungbadak' 'Sukamaju' 'Sukatani' 'Harjamukti' 'Sempur'
    'Pamoyanan' 'Pabaton' 'Ciseeng' 'Jonggol' 'Ciampea' 'Laladon'
    'Rangga Mekar' 'Tegal Gundi' 'Batutulis' 'Ciangsana' 'Puncak' 'Cisarua'
    'Cimangu' 'Kranggan' 'Taman Kencana' 'Cikaret' 'Tenjo' 'Gadog' 'Rumpin'
    'Pancoran Mas' 'Kelapa Dua' 'Cimanggis' 'Citayam' 'Cinangka'
    'Bojong Sari' 'Cilodong' 'Limo' 'Sukmajaya' 'Rangkapanjaya' 'Cinere'
    'Pangkalan Jati' 'Sawangan' 'Beji' 'Margonda' 'Depok II' 'Krukut'
    'Kukusan' 'Cisalak' 'Cilangkap' 'Tirtajaya' 'Gandul' 'Jelambar'
    'Jagakarsa' 'Bintaro' 'Kebagusan' 'Pantai Indah Kapuk' 'Green Ville'
    'Puri Indah' 'Kembangan' 'Permata Hijau' 'Meruya' 'Utan Kayu'
    'Green Lake City' 'Kalibata' 'Cakung' 'Cipete' 'Kebayoran Baru'
    'Cempaka Putih' 'Ampera' 'Jati Padang' 'Permata Buana' 'Pos Pengumben'
    'Palmerah' 'Pantai Mutiara' 'Puri Mansion' 'Tanjung Duren'
    'Taman Grisenda' 'Intercon' 'Menteng' 'Rawamangun' 'Kelapa Gading'
    'Cipinang' 'Angke' 'Gandaria' 'Pulo Gadung' 'Pondok Indah' 'Kebon Jeruk'
    'Muara Karang' 'Jatinegara' 'Pasar Rebo' 'Senopati' 'Matraman'
    'Kemayoran' 'Cikini' 'Mampang Prapatan' 'Pasar Minggu' 'Pejaten'
    'Ciganjur' 'Lebak Bulus' 'Cilandak' 'Kota Bambu Utara' 'Pluit' 'Senen'
    'Pasar Baru' 'Tomang' 'Metland Puri' 'Duren Sawit' 'Kembangan Selatan'
    'Duri Kepa' 'Metro permata' 'Citra Garden' 'Tanjung Priok' 'Sumur Batu'
    'Slipi' 'Kalideres' 'Pondok Kelapa' 'Pondok Bambu' 'Taman Palem'
    'Kebayoran Lama' 'Bendungan Hilir' 'Cawang' 'Duri Kosambi' 'Koja'
    'Lubang Buaya' 'Gatot Subroto' 'Ciracas' 'Taman Ratu' 'patra kuningan'
    'Antasari' 'Sunrise Garden' 'Tanah Kusir' 'Tebet' 'Simprug' 'Senayan'
    'Puri Media' 'Mangga Besar' 'Joglo' 'Tanjung Barat' 'Pengadegan'
    'Pancoran' 'Bangka' 'Tambora' 'Duren Tiga' 'Pulomas' 'Grogol' 'Sunter'
    'Daan Mogot' 'Kedoya Utara' 'Menteng Atas' 'Setiabudi' 'Kramat Jati'
    'TB Simatupang' 'Cengkareng' 'Kayu Putih' 'Bojong Indah' 'Fatmawati'
    'Ragunan' 'Radio Dalam' 'Raffles Hills' 'Sektor 3A-Bintaro' 'Petojo'
    'Green garden' 'Pinang Ranti' 'Taman Meruya' 'Alam Sutera'
    'Gading Serpong' 'BSD City' 'BSD The Icon' 'BSD Kencana Loka'
    'BSD Delatinos' 'Cikupa Citra Raya' 'BSD' 'Pinang' 'Ciledug' 'Rawakalong'
    'Sindang Jaya' 'Cisauk' 'Pagedangan' 'Karawaci' 'Cikokol' 'Cibodas'
    'Panongan' 'Cikupa' 'BSD De Park' 'Serua' 'Lippo Karawaci' 'Cipondoh'
    'Tangerang Kota' 'Pondok Cabe' 'Graha Raya' 'Gading Serpong IL Lago'
    'BSD Green Wich' 'BSD Giri Loka' 'BSD Eminent' 'Larangan' 'BSD Foresta'
    'Modernland' 'BSD Nusaloka' 'Poris' 'Cipadu' 'Batu Ceper' 'Pengasinan'
    'BSD Sevilla' 'Rempoa' 'Sutera Sitara Alam Sutera' 'BSD Taman Giri Loka'
    'Pasar Kemis' 'BSD Graha Raya' 'Pesanggrahan' 'Bitung'
    'Gading Serpong Pondok Hijau Golf' 'Ciater' 'Parigi' 'Tigaraksa'
    'Gading Serpong Andalucia' 'Gading Serpong The Spring' 'Banjar Wijaya'
    'Cireundeu' 'BSD Griya Loka' 'Balaraja' 'BSD Telaga Golf'
    'BSD Puspita Loka' 'Sutera Onix Alam Sutera' 'Pondok Benda' 'Bakti Jaya'
    'BSD Residence One' 'Jatake' 'Kresek' 'Kreo' 'Sepatan' 'Metro Permata'
    'Cihuni' 'Pondok Betung' 'BSD The Green' 'Gading Serpong Scientia Garden'
    'BSD Bukit Golf' 'BSD Duta Bintaro' 'BSD Green Cove' 'Duta Garden'
    'Jelupang' 'BSD Avani' 'Gading Serpong L Agricola'
    'Gading Serpong Samara Village' 'Rajeg' 'Benda' 'BSD Anggrek Loka'
    'Cimone' 'Babakan' 'Jombang' 'Lengkong Kulon' 'BSD Provance Parkland'
    'Sudimara'
    """
    import re

    # Temukan semua yang ada di dalam kutip
    matches = re.findall(r"'[^']+'", teks)

    # Gabungkan dengan koma
    result = ",".join(matches)
    return result

def tebak_harga(df_input) :
    model_rr = joblib.load('../model_rr.h5')
    y_pred = model_rr.predict(df_input)
    return y_pred