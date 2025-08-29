import streamlit as st
import numpy as np
import colorsys
import random
import json
import pickle
import matplotlib.pyplot as plt
from itertools import islice


# Load JSON files
with open('other_jsons/sanskrit_dict.json', 'r', encoding='utf-8') as f:
    sanskrit_dict = json.load(f)

with open('other_jsons/word_freq.json', 'r') as json_file:
    count_lookup = json.load(json_file)

with open('other_jsons/time.json', 'r') as json_file:
    time_lookup = json.load(json_file)

word_list=[]
for key,value in count_lookup.items():
    if len(value)!=0:
        word_list.append(key)
book_list=['Abhidharmakośa',
 'Abhidharmakośabhāṣya',
 'Abhidhānacintāmaṇi',
 'Abhinavacintāmaṇi',
 'Acintyastava',
 'Agastīyaratnaparīkṣā',
 'Agnipurāṇa',
 'Aitareya-Āraṇyaka',
 'Aitareyabrāhmaṇa',
 'Aitareyopaniṣad',
 'Amarakośa',
 'Amaraughaśāsana',
 'Amaruśataka',
 'Amṛtabindūpaniṣat',
 'Antagaḍadasāo',
 'Arthaśāstra',
 'Atharvaprāyaścittāni',
 'Atharvaveda (Paippalāda)',
 'Atharvaveda (Śaunaka)',
 'Atharvavedapariśiṣṭa',
 'Avadānaśataka',
 'Ayurvedarasāyana',
 'Aṣṭasāhasrikā',
 'Aṣṭādhyāyī',
 'Aṣṭāvakragīta',
 'Aṣṭāṅgahṛdayasaṃhitā',
 'Aṣṭāṅganighaṇṭu',
 'Aṣṭāṅgasaṃgraha',
 'Baudhāyanadharmasūtra',
 'Baudhāyanagṛhyasūtra',
 'Baudhāyanaśrautasūtra',
 'Bhadrabāhucarita',
 'Bhairavastava',
 'Bhallaṭaśataka',
 'Bhramarāṣṭaka',
 'Bhāgavatapurāṇa',
 'Bhāradvājagṛhyasūtra',
 'Bhāradvājaśrautasūtra',
 'Bhāratamañjarī',
 'Bhāvaprakāśa',
 'Bodhicaryāvatāra',
 'Brahmabindūpaniṣat',
 'Buddhacarita',
 'Bījanighaṇṭu',
 'Bṛhadāraṇyakopaniṣad',
 'Bṛhatkathāślokasaṃgraha',
 'Cakra (?) on Suśr',
 'Carakasaṃhitā',
 'Carakatattvapradīpikā',
 'Caurapañcaśikā',
 'Chāndogyopaniṣad',
 'Comm. on the Kāvyālaṃkāravṛtti',
 'Commentary on Amaraughaśāsana',
 'Commentary on the Kādambarīsvīkaraṇasūtramañjarī',
 'Daśakumāracarita',
 'Devīkālottarāgama',
 'Devīmāhātmya',
 'Dhanurveda',
 'Dhanvantarinighaṇṭu',
 'Divyāvadāna',
 'Drāhyāyaṇaśrautasūtra',
 'Ekākṣarakoṣa',
 'Garbhopaniṣat',
 'Garuḍapurāṇa',
 'Gautamadharmasūtra',
 'Gaṇakārikā',
 'Gheraṇḍasaṃhitā',
 'Gobhilagṛhyasūtra',
 'Gokarṇapurāṇasāraḥ',
 'Gopathabrāhmaṇa',
 'Gorakṣaśataka',
 'Gītagovinda',
 'Gūḍhārthadīpikā',
 'Gṛhastharatnākara',
 'G\ufff8ḍhārthaprakāśaka',
 'Haribhaktivilāsa',
 'Harivaṃśa',
 'Harṣacarita',
 'Haṃsadūta',
 'Haṃsasaṃdeśa',
 'Haṭhayogapradīpikā',
 'Hiraṇyakeśigṛhyasūtra',
 'Hitopadeśa',
 'Hārāṇacandara on Suśr',
 'Indu (ad AHS)',
 'Jaiminigṛhyasūtra',
 'Jaiminīya-Upaniṣad-Brāhmaṇa',
 'Jaiminīyabrāhmaṇa',
 'Jaiminīyaśrautasūtra',
 'Janmamaraṇavicāra',
 'Kaiyadevanighaṇṭu',
 'Kathāsaritsāgara',
 'Kaulāvalīnirṇaya',
 'Kauśikasūtra',
 'Kauśikasūtradārilabhāṣya',
 'Kauśikasūtrakeśavapaddhati',
 'Kauṣītakagṛhyasūtra',
 'Kauṣītakibrāhmaṇa',
 'Kauṣītakyupaniṣad',
 'Kaṭhopaniṣad',
 'Kaṭhāraṇyaka',
 'Khādiragṛhyasūtra',
 'Khādiragṛhyasūtrarudraskandavyākhyā',
 'Kirātārjunīya',
 'Kokilasaṃdeśa',
 'Kumārasaṃbhava',
 'Kādambarīsvīkaraṇasūtramañjarī',
 'Kālikāpurāṇa',
 'Kāmasūtra',
 'Kātyāyanasmṛti',
 'Kātyāyanaśrautasūtra',
 'Kāvyasaṃgraha',
 'Kāvyādarśa',
 'Kāvyālaṃkāra',
 'Kāvyālaṃkāravṛtti',
 'Kāśikāvṛtti',
 'Kāṭhakagṛhyasūtra',
 'Kāṭhakasaṃhitā',
 'Kūrmapurāṇa',
 'Kṛṣiparāśara',
 'Kṛṣṇāmṛtamahārṇava',
 'Lalitavistara',
 'Laṅkāvatārasūtra',
 'Liṅgapurāṇa',
 'Madanapālanighaṇṭu',
 'Mahābhārata',
 'Mahācīnatantra',
 'Maitrāyaṇīsaṃhitā',
 'Manusmṛti',
 'Matsyapurāṇa',
 'Maṇimāhātmya',
 'Meghadūta',
 'Mugdhāvabodhinī',
 'Mukundamālā',
 'Muṇḍakopaniṣad',
 'Mānavagṛhyasūtra',
 'Mātṛkābhedatantra',
 'Mūlamadhyamakārikāḥ',
 'Mṛgendratantra',
 'Mṛgendraṭīkā',
 'Narasiṃhapurāṇa',
 'Narmamālā',
 'Nibandhasaṃgraha',
 'Nighaṇṭuśeṣa',
 'Nirukta',
 'Nyāyabhāṣya',
 'Nyāyabindu',
 'Nyāyacandrikāpaṇjikā',
 'Nyāyasūtra',
 'Nādabindūpaniṣat',
 'Nāradasmṛti',
 'Nāḍīparīkṣā',
 'Nāḍīvijñāna',
 'Nāṭyaśāstra',
 'Nāṭyaśāstravivṛti',
 'Padārthacandrikā',
 'Paramānandīyanāmamālā',
 'Paraśurāmakalpasūtra',
 'Parāśaradharmasaṃhitā',
 'Parāśarasmṛtiṭīkā',
 'Pavanadūta',
 'Pañcaviṃśabrāhmaṇa',
 'Pañcārthabhāṣya',
 'Paṃcasuttaṃ',
 'Prasannapadā',
 'Pāraskaragṛhyasūtra',
 'Pāśupatasūtra',
 'Rasahṛdayatantra',
 'Rasakāmadhenu',
 'Rasamañjarī',
 'Rasaprakāśasudhākara',
 'Rasaratnasamuccaya',
 'Rasaratnasamuccayabodhinī',
 'Rasaratnasamuccayadīpikā',
 'Rasaratnasamuccayaṭīkā',
 'Rasaratnākara',
 'Rasaratnākara Rasakhaṇḍa',
 'Rasasaṃketakalikā',
 'Rasataraṅgiṇī',
 'Rasendracintāmaṇi',
 'Rasendracūḍāmaṇi',
 'Rasendrasārasaṃgraha',
 'Rasikapriyā',
 'Rasikasaṃjīvanī',
 'Rasādhyāya',
 'Rasādhyāyaṭīkā',
 'Rasārṇava',
 'Rasārṇavakalpa',
 'Ratnadīpikā',
 'Ratnaṭīkā',
 'Rājamārtaṇḍa',
 'Rājanighaṇṭu',
 'Rāmāyaṇa',
 'Saddharmapuṇḍarīkasūtra',
 'Sarvadarśanasaṃgraha',
 'Sarvāṅgasundarā',
 'Saundarānanda',
 'Saṃvitsiddhi',
 'Saṅghabhedavastu',
 'Skandapurāṇa',
 'Skandapurāṇa (Revākhaṇḍa)',
 'Smaradīpikā',
 'Spandakārikā',
 'Spandakārikānirṇaya',
 'Sphuṭārthāvyākhyā',
 'Suśrutasaṃhitā',
 'Sāmavidhānabrāhmaṇa',
 'Sātvatatantra',
 'Sāṃkhyakārikā',
 'Sāṃkhyakārikābhāṣya',
 'Sāṃkhyatattvakaumudī',
 'Sūryasiddhānta',
 'Sūryaśataka',
 'Sūryaśatakaṭīkā',
 'Taittirīyabrāhmaṇa',
 'Taittirīyasaṃhitā',
 'Taittirīyopaniṣad',
 'Taittirīyāraṇyaka',
 'Tantrasāra',
 'Tantrākhyāyikā',
 'Tantrāloka',
 'Tarkasaṃgraha',
 'Tattvavaiśāradī',
 'Toḍalatantra',
 'Trikāṇḍaśeṣa',
 'Uḍḍāmareśvaratantra',
 'Vaikhānasadharmasūtra',
 'Vaikhānasagṛhyasūtra',
 'Vaikhānasaśrautasūtra',
 'Vaitānasūtra',
 'Vaiśeṣikasūtra',
 'Vaiśeṣikasūtravṛtti',
 'Varāhapurāṇa',
 'Vasiṣṭhadharmasūtra',
 'Vetālapañcaviṃśatikā',
 'Viṃśatikākārikā',
 'Viṃśatikāvṛtti',
 'Viṣṇupurāṇa',
 'Viṣṇusmṛti',
 'Vājasaneyisaṃhitā (Mādhyandina)',
 'Vārāhagṛhyasūtra',
 'Vārāhaśrautasūtra',
 'Vātūlanāthasūtras',
 'Vātūlanāthasūtravṛtti',
 'Vṛddhayamasmṛti',
 'Yogaratnākara',
 'Yogasūtra',
 'Yogasūtrabhāṣya',
 'Yājñavalkyasmṛti',
 'Ānandakanda',
 'Āpastambadharmasūtra',
 'Āpastambagṛhyasūtra',
 'Āpastambaśrautasūtra',
 'Āryāsaptaśatī',
 'Āyaraṅga',
 'Āyurvedadīpikā',
 'Āśvalāyanagṛhyasūtra',
 'Āśvālāyanaśrautasūtra',
 'Śatakatraya',
 'Śatapathabrāhmaṇa',
 'Śikṣāsamuccaya',
 "Śira'upaniṣad",
 'Śivapurāṇa',
 'Śivasūtra',
 'Śivasūtravārtika',
 'Śukasaptati',
 'Śvetāśvataropaniṣad',
 'Śyainikaśāstra',
 'Śāktavijñāna',
 'Śārṅgadharasaṃhitā',
 'Śārṅgadharasaṃhitādīpikā',
 'Śāṅkhāyanagṛhyasūtra',
 'Śāṅkhāyanaśrautasūtra',
 'Śāṅkhāyanāraṇyaka',
 'Ṛgveda',
 'Ṛgvedakhilāni',
 'Ṛgvedavedāṅgajyotiṣa',
 'Ṛgvidhāna',
 'Ṛtusaṃhāra',
 'Ṣaḍviṃśabrāhmaṇa',
'Ṭikanikayātrā']
st.set_page_config(
        page_title="आवृत्तिसमीक्षणम्",
        page_icon="📚",
        initial_sidebar_state="expanded"
    )


# Apply a light saffron background to the entire page
st.markdown(
    """
    <style>
    /* Set the background color for the whole page */
    .stApp {
        background-color: #F3D0D7;  /* Light saffron */
    }
    /* Header with no specific width, just styling */
    .header {
        text-align: center;         /* Center the text */
        color: white;               /* White text color */
        font-size: 100px;           /* Large font size */
        padding: 0px 0; 
        text-shadow: 0px 0px 8px rgba(0, 0, 0, 0.4); /* Adding texshado*/
	width: 750px           /* Vertical padding inside the header */
    }
    </style>
    """,
    unsafe_allow_html=True
)  # Header without background, styled for dynamic width
st.markdown(
    "<h1 class='header'>आवृत्तिसमीक्षणम्</h1>",
    unsafe_allow_html=True
)


# Adding masala
def book_top_n(book_name, n):
    with open(rf"{book_name}.json") as book_:
        book = json.load(book_)
    book_word_dict = {}
    for line in book['lines']:
        word_list = line['root_words']
        for word in word_list:
            if word in book_word_dict:
                book_word_dict[word] += 1
            else:
                book_word_dict[word] = 1
    book_word_arr = [key for key,value in sorted(book_word_dict.items(), key=lambda item: item[1], reverse=True)[:n]]
    return book_word_arr

def graph_these(words, abs=True, yr_range=[-1500, 1200]):
    fig, ax = plt.subplots()
    n = len(words)
    offsets = [(i * 20) - (n - 1) * 10 for i in range(n)]
    colors = generate_distinct_colors(n)
    for i in range(n):
        graph_this(words[i], ax, abs=abs, yr_range=yr_range, label=f"{words[i]}", offset=offsets[i], color=colors[i])
    ax.legend()
    st.pyplot(plt)


def generate_distinct_colors(n):
    colors = []
    for i in range(n):
        # Generate evenly spaced hues
        hue = i / n
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Full saturation and value
        # Convert RGB from 0-1 range to 0-255 and format as hex
        hex_color = "#{:02X}{:02X}{:02X}".format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        # Ensure white is not in the list
        if hex_color != "#FFFFFF":
            colors.append(hex_color)

    # Shuffle to avoid sequential hues
    random.shuffle(colors)
    return colors


def graph_this(word, ax, label, offset=0, color='#F4C430', abs=True, yr_range=[-1500, 1200]):
    buckets = np.array(27 * [0])
    word_info = count_lookup.get(f'{word}', [])

    if len(word_info):
        for book_info in word_info:
            book_name = book_info['name']
            time = time_lookup.get(f'{book_name}', (0, 0))
            idx_range = [(time[0] // 100) + 15, (time[1] // 100) + 15]
            count = book_info['count']
            for idx in range(idx_range[0], idx_range[1]):
                buckets[idx] += count

        total = np.sum(buckets)
        for i in range(len(buckets)):
            if not abs:
                buckets[i] = buckets[i] * 100 / total

        req_start_idx = (max(yr_range[0], -1500) // 100) + 15
        req_end_idx = (min(yr_range[1], 1200) // 100) + 15
        bucket_labels = [i for i in range(max(yr_range[0], -1500), min(yr_range[1], 1200), 100)]
        bucket_width = np.diff(bucket_labels) * 0.4  # Reduce width to fit two bars side by side

        # Shift the position of the bars by the offset
        ax.bar(np.array(bucket_labels[:-1]) + offset, buckets[req_start_idx: req_end_idx - 1], width=bucket_width,
               edgecolor='black', align='edge', color=color, label=label)
        ax.set_xlabel('Years')
        if not abs:
            ax.set_ylabel('Percentage of occurrences')
        else:
            ax.set_ylabel('Frequency of occurrences')

    else:
        st.write("Occurrence of the word not profiled yet.")


# Sidebar configuration
st.sidebar.title("Options")

# Dropdown for Mode of Study
mode_of_study = st.sidebar.selectbox("Mode of Study", ["Select", "Comparative Study", "Word Analysis","Book Analysis"])

# Dropdown for Mode of Analysis
mode_of_analysis = st.sidebar.selectbox("Mode of Analysis", ["Select", "abs", "percentage"])

# Show input fields based on the selected Mode of Study
if mode_of_study == "Comparative Study":
    num_words = st.sidebar.number_input("Enter number of words for comparative study", min_value=1, step=1)
    if num_words > 0:
        word_inputs = []
        for i in range(num_words):
            word = st.sidebar.selectbox(f"Select word {i + 1}", options=word_list, key=f"word_input_{i}")
            word_inputs.append(word)
        # Range sliders always present
        lower_range = st.sidebar.slider("Lower range", min_value=-1500, max_value=1500, step=100, key="lower_range")
        upper_range = st.sidebar.slider("Upper range", min_value=-1500, max_value=1500, step=100, key="upper_range")
        st.subheader("Time Analysis Graph")
        if mode_of_analysis == "percentage":
            graph_these(word_inputs, abs="False", yr_range=[lower_range, upper_range])
        else:
            graph_these(word_inputs, abs="True", yr_range=[lower_range, upper_range])


elif mode_of_study == "Word Analysis":
    selected_word = st.sidebar.selectbox("Select word for analysis", options=word_list, key="word_analysis_input")
    word_info = count_lookup.get(f'{selected_word}', [])
    with open("similar_words.pkl", "rb") as f:
        similar_words_load = pickle.load(f)

    # Display the chosen word and its meaning
    st.header(selected_word)
    if selected_word in sanskrit_dict:
        st.subheader(f"Meaning: {sanskrit_dict[selected_word]}")
    st.subheader("Similar words")
    sim_words = similar_words_load[selected_word]
    cols = st.columns(3)
    ranger = min(len(sim_words), 3)
    i = 0
    for col, word in zip(cols, sim_words[i:i + ranger]):
        col.write(word)
        col.text(sanskrit_dict.get(word, "Meaning not available"))

    # Range sliders always present
    lower_range = st.sidebar.slider("Lower range", min_value=-1500, max_value=1500, step=100, key="lower_range")
    upper_range = st.sidebar.slider("Upper range", min_value=-1500, max_value=1500, step=100, key="upper_range")
    st.subheader("Time Analysis Graph")
    if mode_of_analysis == "percentage":
        graph_these([selected_word], abs="False", yr_range=[lower_range, upper_range])
    else:
        graph_these([selected_word], abs="True", yr_range=[lower_range, upper_range])

    # Display the book occurrences with examples
    st.subheader("Book Occurrences")
    for i in range(len(word_info)):
        st.markdown(f"### {word_info[i]['name']}")
        st.markdown("**Examples:**")
        for example in word_info[i]['examples']:
            st.write(f"- {example}")

elif mode_of_study == "Book Analysis":
    book_name=st.sidebar.selectbox("Select book", options=book_list,key="book_input")
    top_words=book_top_n(book_name, 5)
    st.subheader(book_name)
    bullet=1
    for word in top_words:
        st.markdown(f"{bullet}.{word}")
        st.markdown(f"**Meaning:** {sanskrit_dict[word]}")
        bullet=bullet+1





