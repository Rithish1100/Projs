NAME="[name]"

with open ("list_to_invite.txt") as members:
    inv_members=members.readlines()
with open("letter.txt")as letter_file:
    letter_contents=letter_file.read()
    for name in inv_members:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(NAME,stripped_name)
        with open(f"letter_for_{stripped_name}.docx",mode="w") as new:
            new.write(new_letter)

