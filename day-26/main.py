import pandas
df=pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict={row['letter']:row['code'] for letter,row in df.iterrows()}
print(new_dict)

def generate_phenotic():
    phenotic=input("Enter the word to convert:")
    phenotic_upper=phenotic.upper()
    try:
        list=[new_dict[words] for words in phenotic_upper]
    except KeyError:
        print("only alphebets are allowed")
        generate_phenotic()

    else:
        print(list)
generate_phenotic()