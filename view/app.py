import streamlit as st
import pandas as pd
import backend as bc

st.title('Prediksi Harga Rumah Jabodetabek')
listkota = (
    ' Bekasi',
    ' Bogor',
    ' Depok',
    ' Jakarta Barat',
    ' Jakarta Selatan',
    ' Jakarta Utara',
    ' Jakarta Timur',
    ' Jakarta Pusat',
    ' Tangerang'
    )
listcondition = (
    'butuh renovasi',
    'sudah renovasi',
    'bagus',
    'bagus sekali',
    'baru'
)
listfurnishing = (
    'unfurnished',
    'semi furnished',
    'furnished',
    'fully furnished'
)
listfacility = (
    'AC',
    'Akses Parkir',
    'Backyard luas',
    'Balkon',
    'Basement',
    'CCTV',
    'Canopy',
    'Carport',
    'Clubhouse',
    'Dapur bersih dan kotor',
    'Garasi',
    'Garden',
    'Gudang',
    'Jalur Telepon',
    'Jetpump',
    'Jogging Track',
    'Keamanan',
    'Kitchen Set',
    'Kolam Ikan',
    'Kolam Renang',
    'Kompor',
    'Kulkas',
    'Lapangan Basket',
    'Lapangan Bola',
    'Lapangan Bulu Tangkis',
    'Lapangan Tenis',
    'Lapangan Voli',
    'Lemari kayu',
    'Living room',
    'Masjid',
    'Mesin Cuci',
    'Mushola',
    'One Gate System',
    'Pagar',
    'Playground',
    'Posisi hoek',
    'Service area',
    'Servis Area',
    'Smart Home',
    'Smart lock door',
    'Smarthome',
    'Taman',
    'Tempat Gym',
    'Tempat Jemuran',
    'Tempat Laundry',
    'Toren',
    'Void',
    'Wastafel',
    'Water heater',
    'kompor'
   )
listmah = (450, 900, 1300, 2200, 3500, 4400, 5500, 7700, 11000)
listdistrict = (bc.get_district()).split(",")
listdistrict = [x.strip().strip("'") for x in bc.get_district().split(",") if x.strip().strip("'")]

city = st.selectbox("Kota : ",listkota)
district = st.multiselect(
    "Distrik :",
    listdistrict,
    max_selections=1
)
fasicilities = st.multiselect("Fasilitas : ",listfacility)
property_condition = st.selectbox("Kondisi Properti",listcondition)
furnishing = st.selectbox("Kondisi Properti",listfurnishing)
electricity = st.selectbox("Listrik (mAh) : ",listmah)
latitude = st.number_input("Latitude : ")
longitude = st.number_input("Longitude : ")
land_size = st.number_input("Ukuran lahan (m2) : ")
building_size = st.number_input("Ukuran bangunan (m2) : ")
bedrooms = st.number_input("Kamar tidur : ", min_value = 0,step=1)
bathrooms = st.number_input("Kamar mandi : ",min_value = 0,step=1)
maid_bedrooms = st.number_input("Kamar tidur pembantu : ",min_value = 0,step=1)
maid_bathrooms = st.number_input("Kamar mandi pembantu : ",min_value = 0,step=1)
carports = st.number_input("Carports : ",min_value = 0,step=1)
floors = st.number_input("Lantai : ",min_value = 0,step=1)
building_age = st.number_input("Usia rumah : ",min_value = 0,step=1)
garages = st.number_input("Garasi : ",min_value = 0 ,step=1)

if st.button("Tebak harga"):
    city_labelled = bc.city_input(city)
    district_labelled = bc.district_input(district[0]) if district else 0
    condition_labelled = bc.condition_input(property_condition)
    furnishing_labelled = bc.furnishing_input(furnishing)
    facilities_labelled = bc.facilities_input(fasicilities)

    df_input = pd.DataFrame({
        'district': district_labelled,
        'city': city_labelled,
        'lat': [latitude],
        'long': [longitude],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'land_size_m2': [land_size],
        'building_size_m2': [building_size],
        'carports': [carports],
        'electricity': [electricity],
        'maid_bedrooms': [maid_bedrooms],
        'maid_bathrooms': [maid_bathrooms],
        'floors': [floors],
        'building_age': [building_age],
        'garages': [garages],
        'property_condition_mapped': condition_labelled,
        'furnishing_status': furnishing_labelled
    }, index=[0])

    df_input = pd.concat([df_input, facilities_labelled], axis=1)
    
    # pastikan kolom sama seperti saat training
    cols_train = [
        'district', 'city', 'lat', 'long', 'bedrooms', 'bathrooms',
       'land_size_m2', 'building_size_m2', 'carports', 'electricity',
       'maid_bedrooms', 'maid_bathrooms', 'floors', 'building_age', 'garages',
       'property_condition_mapped', 'furnishing_status', 'AC', 'Akses Parkir',
       'Backyard luas', 'Balkon', 'Basement', 'CCTV', 'Canopy', 'Carport',
       'Clubhouse', 'Dapur bersih dan kotor', 'Garasi', 'Garden', 'Gudang',
       'Jalur Telepon', 'Jetpump', 'Jogging Track', 'Keamanan', 'Kitchen Set',
       'Kolam Ikan', 'Kolam Renang', 'Kompor', 'Kulkas', 'Lapangan Basket',
       'Lapangan Bola', 'Lapangan Bulu Tangkis', 'Lapangan Tenis',
       'Lapangan Voli', 'Lemari kayu', 'Living room', 'Masjid', 'Mesin Cuci',
       'Mushola', 'One Gate System', 'Pagar', 'Playground', 'Posisi hoek',
       'Service area', 'Servis Area', 'Smart Home', 'Smart lock door',
       'Smarthome', 'Taman', 'Tempat Gym', 'Tempat Jemuran', 'Tempat Laundry',
       'Toren', 'Void', 'Wastafel', 'Water heater', 'kompor'
    ]
    df_input = df_input[cols_train]
    price = bc.tebak_harga(df_input)
    st.write(f"Prediksi harga: Rp {price[0]:,.0f}")