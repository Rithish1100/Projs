import pandas
df=pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict={row['letter']:row['code'] for letter,row in df.iterrows()}
phenotic=input("Enter the word to convert:")
phenotic_upper=phenotic.upper()
list=[new_dict[words] for words in phenotic_upper if words in new_dict]  
print(list)
