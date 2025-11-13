"""Module main contenant la fonction secondaire demandé afin de testé 
si une chaine est un palindrome une fonction pour suprimé les accents et la fonction principale
avec une série de test"""

#### Fonction secondaire

def ispalindrome(p):
    """ispalindrome prends en paramètre une chaine p
     et renvoit True lorsque qu'elle est un palindrome et False sinon"""
    p = p.lower()
    p = remove_accents(p)
    p_clean = ""
    for c in p:
        if 'a' <= c <= 'z' or '0' <= c <= '9':
            p_clean += c
    return p_clean == p_clean[::-1]

def remove_accents(s):
    """Remplace les lettres accentuées par leur équivalent sans accent"""
    accents = {
        'à':'a','á':'a','â':'a','ä':'a','ã':'a','å':'a',
        'è':'e','é':'e','ê':'e','ë':'e',
        'ì':'i','í':'i','î':'i','ï':'i',
        'ò':'o','ó':'o','ô':'o','ö':'o','õ':'o',
        'ù':'u','ú':'u','û':'u','ü':'u',
        'ç':'c','ñ':'n','ý':'y','ÿ':'y',
        'À':'A','Á':'A','Â':'A','Ä':'A','Ã':'A','Å':'A',
        'È':'E','É':'E','Ê':'E','Ë':'E',
        'Ì':'I','Í':'I','Î':'I','Ï':'I',
        'Ò':'O','Ó':'O','Ô':'O','Ö':'O','Õ':'O',
        'Ù':'U','Ú':'U','Û':'U','Ü':'U',
        'Ç':'C','Ñ':'N','Ý':'Y'
    }
    return ''.join(accents.get(c,c) for c in s)

#### Fonction principale
def main():
    """Renvoie une série de tests de ispalindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "anona"]:
        print(s, "→", ispalindrome(s))

print(ispalindrome("Kanan"))
print(ispalindrome("ete"))
if __name__ == "__main__":
    main()
