print('''              
  ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                        |_|                    ''')



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def cipher(txt,shif,encoded_or_decoded):
    output=""
    if encoded_or_decoded == 'decode':
        if i in alphabet:
             shif*=-1
        for i in txt:
                if i not in alphabet:
                     output+=i
                else:
                     shifted_position=alphabet.index(i)+shif
                     shifted_position%= len(alphabet)
                     output+=alphabet[shifted_position]
    print(f"here is the {encoded_or_decoded} text:{output}")
should_continue=True
while should_continue:
    direction= input("Type 'encode' to encript, type 'decode' to decript:\n").lower()
    text= input("Type your message:\n").lower()
    shift =int(input("Type the shift number:\n"))
    cipher(txt=text,shif=shift,encoded_or_decoded=direction)

    restart=input("type y to continrue n to n\n").lower()
    if restart== "no":
        should_continue=False
        print("bye")