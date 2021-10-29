

# ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄▄          ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄  
#█       █   ▄  █ █      █       █  █ █  █  █  █ █       █       █       █   █       █        █   ▄  █ █       █      █ 
#█       █  █ █ █ █  ▄   █▄▄▄▄   █  █▄█  █   █▄█ █    ▄▄▄█  ▄▄▄▄▄█  ▄▄▄▄▄█   █    ▄▄▄█        █  █ █ █ █   ▄   █  ▄    █
#█     ▄▄█   █▄▄█▄█ █▄█  █▄▄▄▄█  █       █       █   █▄▄▄█ █▄▄▄▄▄█ █▄▄▄▄▄█   █   █▄▄▄         █   █▄▄█▄█  █ █  █ █ █   █
#█    █  █    ▄▄  █      █ ▄▄▄▄▄▄█▄     ▄█  ▄    █    ▄▄▄█▄▄▄▄▄  █▄▄▄▄▄  █   █    ▄▄▄█        █    ▄▄  █  █▄█  █ █▄█   █
#█    █▄▄█   █  █ █  ▄   █ █▄▄▄▄▄  █   █ █ █ █   █   █▄▄▄ ▄▄▄▄▄█ █▄▄▄▄▄█ █   █   █▄▄▄         █   █  █ █       █       █
#█▄▄▄▄▄▄▄█▄▄▄█  █▄█▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█▄▄▄▄▄▄▄█        █▄▄▄█  █▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄█

     
     
# by crazynessie / RØD    
# https://github.com/crazynessie


from hashlib import sha256

entre = input("entrez le nom du fichier a chiffrer/dechiffrer : ")
sortie = input("entrez le nom du fichier final : ")
key = input("entrez la clé : ")

keys = sha256(key.encode('utf-8')).digest()


with open(entre,'rb') as f_entre:
  with open(sortie,'wb') as f_sortie:
    i = 0
    while f_entre.peek():
      c = ord(f_entre.read(1))
      j = i % len(keys)
      b = bytes([c^keys[j]])
      f_sortie.write(b)
      i = i + 1
