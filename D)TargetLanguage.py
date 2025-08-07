Model_name = "facebook/nllb-200-distilled-600M"
print("\n🔄 Loading NLLB model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
language_options = {
        "1": "eng_Latn", "2": "hin_Deva", "3": "tel_Telu", "4": "tam_Taml",
        "5": "kan_Knda", "6": "mal_Mlym", "7": "mar_Deva", "8": "ben_Beng",
        "9": "guj_Gujr", "10": "pan_Guru", "11": "urd_Arab", "12": "ori_Orya",
        "13": "asm_Beng", "14": "san_Deva", "15": "nep_Deva", "16": "bho_Deva",
        "17": "mlt_Latn", "18": "fra_Latn", "19": "spa_Latn", "20": "zho_Hans",
        "21": "ara_Arab", "22": "rus_Cyrl", "23": "deu_Latn", "24": "jpn_Jpan", "25": "ita_Latn"
    }
print("\n🌍 Select target language:")
for key, value in language_options.items():
    print(f"{key}. {value.split('_')[0]}")

choice = input("\nEnter the number of your choice: ")
tgt_lang = language_options.get(choice, "eng_Latn")
