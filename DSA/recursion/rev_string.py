def reverse(string):
    if string == "":
        return ""
    return reverse(string[1:]) + string[0]


print(reverse("tareq"))

# Breakdown Call-Stack
# reverse('tareq')                                   #s = tareq
# =reverse('areq') + 't'                             #s[1:] = areq    s[0] = t
# =reverse('req') + 'a' stack: + 't'                 #s[1:] = req    s[0] = a
# =reverse('eq') + 'r' stack: + 'a' + 't'            #s[1:] = eq    s[0] = r
# =reverse('q') + 'e' stack: + 'r' + 'a' + 't'       #s[1:] = q    s[0] = e
# =reverse('') + 'q' stack: + 'e' + 'r' + 'a' + 't'  #s[1:] = q    s[0] = e
# ='qerat'
