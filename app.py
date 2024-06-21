# df = {
#     "Medicines": [
#         {
#             "Name": None,
#             "Company": None,
#             "Year": None,
#             "Month": None,
#             "Pieces": None,
#             "MRP": None,
#         }
#     ]
# }

import streamlit as st 
import json 

company_names = ['ASTHANG', 'SHASHVI REMEDIES', 'ATRIMED', 'PUNARVASU', 'DIVINE',
       'NECTAR INDIA', 'VAIDYARAJ AUSHADHALAYA', 'SKM', 'LAMAR', 'JRK',
       'DHOOTPAPESHWAR', 'DHANVANTRI', 'AIMIL', 'KERALA AYURVEDA',
       'PHARMACON', 'HEALTH RY PHARMACEUTICALS', 'NISARG', 'DISHANT',
       'SHREE URJA', 'VESCA(AARAMBH)', 'SHREYAS', 'SHIVED', 'ADVAIT',
       'AUSHADI BHAVAN', 'CHAITANYA', 'SHAIVYA', 'NRIGHT',
       'GREEN REMEDIES', 'SOMETIC', 'AVN', 'NAGARJUNA', 'General', 'R&B']

medicine_names = ['Laxadi Guggul Tab.', 'Kutaj Ghanvati Tab.', 'Shanth Vati Tab.',
       'Sutshekhar Ras Tab.', 'Bhungaraj Ghanvati Tab.',
       'Sanjeevani Vati Tab.', 'Haridra Tab.', 'Skin All Tab.',
       'Trishila Tab.', 'Artho Oil', 'Anu Tailan', 'Indigo Powder',
       'Shatavari Tab.', 'ASHT BEAL Avaleh', 'Isabgol Churna (small)',
       'Isabgol Churna (big)', 'Lovanbhaskar Churna', 'Dhatri Rasayan',
       'Hingvashtak Churna', 'Ashwagandha Churna', 'Shatavari Churna',
       'Kouchbej Churna', 'Punarnava Churna', 'Safed Musali Churna',
       'Erandel Tailam', 'Phal Ghritam', 'Aragwadhadi Kashay',
       'Ashtprash Chyawanovleha', 'Bharangyadi Kashay',
       'Yograj Guggul Tab.', 'Sarpogandha Ghanvati Tab.',
       'Kanchanar Guggul Tab.', 'Probhakar Vati Tab.',
       'Mrityunjoya Rasa Tab.', 'Ekangoveer Rasa Tab.',
       'Sonva Manjishthadi Ghan Tab.', 'Kirathktadi Yog Tab.',
       'Daily Calm Tab.', 'Gandhak Rasayan Tab.', 'Trifala Guggul Tab.',
       'Laxmivilas Ras Tab.', 'Shashvi night ointment', 'Stressni cap.',
       'Raw honey', 'Madhur Virechan Vati Tab.', 'Parcid Tab.',
       'Chemo - X', 'Lukor X - SF syrup', 'Multivit Syrup',
       'Malish ointment', 'Motapa Nashak Tab.', 'Atrisor Cap.',
       'Viscovas cap.', 'Atrivit cap.', 'Rhinarm cap.', 'Spazex cap.',
       'M Creoz cap.', 'Ostygen cap.', 'Prunilol cap.', 'Rilanx cap.',
       'Acilars cap.', 'Retrive cap.', 'Ferberry Cap.', 'Vyvuz cap.',
       'Atrisor Ointment', 'Aclear ointment', 'Prunilol ointment',
       'Anti Hyperpigmentation Cream', 'Atrisor Soop',
       'Manjishtadi choornam', 'Rasnerantadi choornam',
       'Prasaranyadi choornam', 'rosnasapthakam chornam', 'Atrifem Syrup',
       'Kottomchukkadi choornam', 'Kalakulalradi choornam',
       'Triphala cap', 'Atrisor shampoo', 'Atrisor Moisturizer',
       'Super cap.', 'Liver carz', 'Glukostat cap.', 'Femicalm cap.',
       'Makardhwaj Rasa Tab.', 'Brahmi vati', 'Arjunchhal Ghanvati tab.',
       'Punarnavadi mandoor vati tab.', 'Swaskuthar rasa tab.',
       'Avipattikar tab.', 'Gandharva haritaki tab.',
       'Sutshekhar rasa tab.', 'Chandraprabha vati tab.',
       'Arogyavardhini Gutika tab.', 'Kaishar guggulu tab.',
       'Divortho tab.', 'Divarsha tab.', 'TKB tab.', 'Divaacid syrup',
       'Vivtorch tab.', 'Spondigen tab,', 'Ovalar cap.', 'DivPCOS tab.',
       'Nectar LIV cap', 'Cyclonec cap', 'Agasthya Rasoyanam',
       'Balajeerakadi Kashayam', 'Varanadhi kashayam', 'Kalyana Gulam',
       'Psorasiddh cream', 'Mahatikta Ghritam cap.', 'Pinda tailam',
       'Phalasorpis saptavarti cap.', 'Ksheerabala cap.',
       'Psorasiddh soap', 'Manasmitra Vatakam cap.', 'Bonita syrup',
       'Phyt fluz syrup', 'Amlahoory tab.', 'Galcure tab.', 'Zyquil tab.',
       'X piles ointment', 'Femtonic syrup', 'Angen grow serum',
       'Psorolin B ointment', 'Anti fungal cream', 'Lippu ointment',
       'Lumina shampoo', 'Eve fresh cream', 'Psorolin soap',
       'Peau moist lotion', 'Yelathi tab.', 'Nilavembu Kudineer tab.',
       'Pesin tab.', 'Verdura Cream', 'Raktastumbak tab',
       'Puhpadhanwa rasa tab.', 'Abhraloha tab', 'Chandrakala ras tab',
       'Kutaja Panpati vati', 'Pittashekhar rasa tab.',
       'Stree Vyadhihari rasa tab.', 'Beejpushti rasa tab.',
       'Tapyadi loha tab.', 'Abhragarbha pottali', 'Debaskin oil',
       'Rumom oil', 'Gunjadi taila', 'Rumom cap.',
       'Jawahar Mohra Ras tab.', 'Vasant Kusumakar rus tab.',
       'Garbhdharini vati tab.', 'Glyoherb granules', 'Gynarim tab.',
       'Yaad granules', 'rimzyme syrup', 'Goji syrup',
       'Panchatikta Ghrita guggulu tab.',
       'Maha Manjisthadi ghanvati tab.', 'Troyodshang guggulu tab.',
       'Keshvardhini tab.', 'Smrutisagar ras tab.', 'Sukesha hair oil',
       'Debaskin cap.', 'Cidity syrup', 'Chandraprabhavati tab.',
       'Kamdudha ras tab.', 'Athigon syrup', 'Purodil ointment',
       'Neeri KFT syrup', 'Winsoria oil', 'Sinactil oil', 'KM lepam',
       'Renoget tab.', 'neelibrigadi keram oil', 'Evakulp tab.',
       'I Cleur 10D tab.', 'Cervigest cap.', 'GT capsules',
       'Hamsapadadi kwath', 'Promoctil cap.', 'Ostoact tab',
       'Mcnovin tab.', 'Remogest tab.', 'Aknol skin cream',
       'Paci-5 syrup', 'Kumkumadi lepam', 'Naser nasal drops',
       'Rumarub ointment', 'Healit ointment', 'Sclerobrium liquid',
       'Kumkumadi thailam', 'Urary cap', 'Pilory cap', 'Ry Multi tab',
       'Ovalory tab', 'Fermy syrup', 'Nartana massage oii',
       'Redusone cap', 'Livosone cap', 'Menodim cap', 'Boneade cap',
       'Urge cap', 'Soruzema massage oil', 'Nurosmart yrup',
       'Respirode tab', 'Sonolax tab.', 'Tulsi tab.', 'Amla tab',
       'Haridra tab.', 'Yahtimadhu tab.', 'Ahwagandha tab.',
       'Inflasone tab.', 'Curcuma plus cap.', 'Vidarikand churna',
       'Swadiht virechan tab.', 'Yashtivadhu Ghanvati peels',
       'Hair pack powder', 'Niramay powder ', 'Shalavari churna',
       'Gokshur churna', 'chyawanrash avleh', 'Sitopaladi tab',
       'Mahayograj guggulu', 'Dahsmool kwath', 'Bhunimbadi kwath',
       'Amalaki Tab.', 'Saptamrut Loh Tab.', 'Haridrakhand Granule',
       'Amalaki Capsule', 'Pochak urja churna', 'Urja sutra tab.',
       'Med urja tab.', 'Thyro urja tab.', 'Urja suddhi cream',
       'Urja saar syrup', 'Urja nerve syrup', 'Ashmatak syrup',
       'Thyro urja kwath', 'Melatonin cap.', 'Vitamin D3 cap',
       'Glutathion cap', 'Multivitamin for women cap.', 'Biotin cap',
       'Calcium citrate', 'Uricg ON tab.', 'Glo ON tab.', 'Flow ON tab.',
       'Merudand vati tab.', 'Coryz ON tab.', 'Vericon oil',
       'Allergon oil', 'Keshya oil', 'Cal ON tab.', 'Thirosat tab.',
       'Dermal ON tab.', 'Tend ON tab.', 'Rumurup oil', 'Pilomrit tab.',
       'Oberap cap.', 'Misnna tab.', 'Jaswand oil',
       'Nagarjunabhra Ras tab.', 'Hemofine tab.', 'Thyronull tab.',
       'Kuberaksha vati tab.', 'Eladi vati tab.', 'Kankayan vati tab.',
       'Shatavari Ghan vati tab.', 'Kombadrakhi guggul vati tab.',
       'Kanchanar ghan vati tab.', 'Auna tab.', 'Jatyadi tab.',
       'Panchendriya Nasal drops', 'Nirgundi ghana tab.',
       'Krumileuthar ras tab.', 'Paktapachak ghana tab.',
       'Kanchanar guggul tab.', 'Majjasthi pachak ghana tab.',
       'Maharasnadikashay ghana tab.', 'Raspochak ghan tab.',
       'Punarnava ghan tab.', 'Manspachak ghan tab.', 'Rumaset cap',
       'Bescumin cap', 'Septowin cap', 'Rumaset gold cap.',
       'Bescumin fork syrup', 'PH Flsh cap', 'Zingmax cap', 'Bormheal',
       'Enarvin tab.', 'Migreast tab.', 'Enarvin oil', 'Ogestirn lehyam',
       'Eastacad tab.', 'Coswas choornam', 'Grab cap.', 'Nuro XT cap',
       'Spiner tab.', 'Zincosule cap', 'My D3 cap', 'My D3 Magnesium',
       'Primogest 9 Tab.', 'Shaddharana DS tab', 'Gokshuradigulugulu DS',
       'Arthorab liniment', 'Kokiluksham Kashayam tab.',
       'Maharajaprasarini tailam cap.', 'Gandha tailam cap.',
       'Dhanvantaram (101) cap', 'Kaisharaguggulu DS tab',
       'Amavatari tab', 'Painflavem tab.', 'Burcalvin cap',
       'Amrutagulgulu DS tab.', 'Guluchyadi kashayam tab.',
       'Potolakaturohiniyadi kashayam tab.', 'Manjisthadi Kashayam tab.',
       'Zeotone plus cap', 'Varandi kashayam tab', 'Amrutotaram tab.',
       'Cardastab tab.', 'Siva gutika', 'Rheumat',
       'Bruhat vatchintamani Ras tab.', 'Abhyarishta',
       'Vriddhiwadhika vati tab.', 'Trimas tab.', 'Ashtamas tab',
       'Navmas tab.', 'Amla t shikakai', 'Neem lotion', 'Multinova cap',
       'Easycally churna', 'Tulsi drop', 'Ovarhythm', 'Duimas tab',
       'Pramas tab.', 'Orthocare cap', 'Triphala guggul (R&B)',
       'Rakt Pachak (R&B)', 'Pigmentation cream', 'Sahacharadi tailam',
       'Vathar oil', 'Shikakai oil', 'Straightening hair oil',
       'Conditioner shampoo', 'Shyam sunder kesh tel', 'Special hair oil',
       'Alovera D shampoo', 'Hair oil', 'Abhyong tel',
       'Prakash cough cold syrup', 'Arbonil Tab.', 'Migraina Tab.',
       'Bavasir Tab.', 'Manohar Tab.', 'Bavasir Oil', 'Palsimed Cap.',
       'Gritivat Churan']

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

years = ['2024','2025','2026']

# Enter medcine name, month, year, get info
def show_med_data(med_name, month, year):
    with open('data.json','r') as f:
        df = json.load(f)
        for med in df['Medicines']:
            if med['Name'] == med_name and med['Month'] == month and med['Year'] == year:
                return med['Pieces'], med['MRP'], med['Company']

# Edit medicine pieces, mrp
def edit_med_data(med_name, month, year, new_pieces, new_mrp):
    with open('data.json','r') as read_file:
        df = json.load(read_file)
        for med in df['Medicines']:
            if med['Name'] == med_name and med['Month'] == month and med['Year'] == year:
                med['Pieces'] = str(new_pieces)
                med['MRP'] = str(new_mrp)
        with open('data.json','w') as write_file:
            json.dump(df, write_file)

# Website
st.title(":blue[Medicine Database]")
st.markdown("## Password verification")
val = st.text_input("Enter password")
col1, col2 = st.columns(2)
password = "abcd"
if val==password:
    # Medicine detatils
    with col1:
        st.markdown("## Get medicine details")
        med_name = st.selectbox("Medicine name", medicine_names)
        month = st.selectbox("Month",months)
        year = st.selectbox("Year", years)
        show = st.button("Submit")
        if show:
            pieces, mrp, company = show_med_data(med_name,month,year)
            st.write(f"Pieces: {pieces}")
            st.write(f"MRP: {mrp}")
            st.write(f"Company: {company}")

    # Edit medicine details
    with col2:
        st.markdown("## Edit medicine details")
        med_name_ed = st.selectbox("Medicine name ", medicine_names)
        month_ed = st.selectbox("Month ",months)
        year_ed = st.selectbox("Year ", years)
        new_Pieces = st.number_input("Pieces ", step=1)
        new_MRP = st.number_input("MRP ", step=1)
        edit = st.button("Edit")
        if edit:
            edit_med_data(med_name_ed,month_ed,year_ed,new_Pieces,new_MRP)
    
    # Generate prescription
