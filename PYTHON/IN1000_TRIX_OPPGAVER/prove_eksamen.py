# #oppgave_1a
# tall = 4 + 3 * 2
# tall = tall + 3
# print(tall)

# #oppgave_1b
# tall = (4 + 3) * 2
# tall = tall + 3
# print(tall)

# #oppgave_1c
# null = 0
# en = 1
# to = 2
# a = 0
# if (null+1 > to) and (null < en):
#     a = to * null
# elif (null+1 > to) or(en < en):
#     a = 3
# else:
#     a = en + 4
# tall = a + 2
# print(tall)

# #oppgave_1d
# i = 0
# tall = 1
# while i < 4:
#     tall = tall * 2
#     i = i + 1
# print(tall)

# #oppgave_1e
# i = 0
# tall = 1
# while i < 99:
#     tall = tall * 2
#     i = i + 1
# print(i)

# #oppgave_1f
# tall = [0,1,3,5,7,9]
# sum2 = 0
# for i in range(len(tall)):
#     if tall[i] < 6:
#         sum2 = sum2 + tall[i]
#     else:
#         sum2 = sum2 + tall[1]
# print(sum2)

# #oppgave_1g
# def null_ut1(liste):
#     ny_liste = []
#     for i in liste:
#         ny_liste.append(0)
#     liste = ny_liste
# terningkast = [1,2,3,3,5,6]
# null_ut1(terningkast)
# print(terningkast[2])

# #oppgave_1h
# def null_ut1(liste):
#     ny_liste = []
#     for i in liste:
#         liste[i] = 0
# terningkast = [1,2,3,3,5,6]
# x = null_ut1(terningkast)
# print(terningkast[3])

# #oppgave_1l
# def doble (a):
#     aa = a + a
#     return aa
# svarA = doble(3)
# svarB = doble("abc")
# print(str(svarA)+str(svarB))

# #oppgave_1j
# tall = [0,1,3,5,7,9]
# liste = tall
# liste.pop(2)
# liste.append(99)
# print(tall[2])

# #oppgave_1K
# heltall = 1
# for tegn in "210202021122212":
#     heltall = heltall * int(tegn)
# print(heltall)

# #oppgave_2a
# def godkjent():
#     maks_poeng = [3,5,5,5,5,6,1,1]
#     oblig1_6 = list(maks_poeng[0:6])
#     oblig7_8 = list(maks_poeng[6:8])
#     sum1 = 0
#     sum2 = 0
#     for x in oblig1_6:
#         sum1 = sum1 + x
#     for y in oblig7_8:
#         sum2 = sum2 + y
#     if sum1 >= 19:
#         if sum2 == 2:
#             print("Du har nok poeng")
#         else:
#             print("Du mangler enten oblig_7 eller oblig_8")
#     else:
#         print("Du har ikke nok poeng for å løse neste obligene")
# godkjent()

#oppgave_2b
def godkjent():
    maks_poeng = [3,5,5,5,5,6,1,1]
    oblig1_6 = list(maks_poeng[0:6])
    oblig7_8 = list(maks_poeng[6:8])
    sum1 = 0
    sum2 = 0
    for x in oblig1_6:
        sum1 = sum1 + x
    for y in oblig7_8:
        sum2 = sum2 + y
    if sum1 >= 19:
        if sum2 == 2:
            return True
        else:
            return False
    else:
        return False
x = godkjent()
print(x)


class Student:
    def __init__(self, obliger):
        self._obliger = obliger
    
    def antall_obliger(self):
        return len(self._obliger)
    
    def oblig(self, nr):
        return self._obliger[nr-1]

from question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question._prompt)
        if answer == question._answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)

# #oppgave_2d
# def obliger_godkjent(student):
#     maks_poeng = [3, 5, 5, 5, 5, 6, 1, 1]
#     oblig1_6 = student.oblig(1) + student.oblig(2) + student.oblig(3) + student.oblig(4) + student.oblig(5) + student.oblig(6)
#     oblig7_8 = student.oblig(7) + student.oblig(8)
    
#     if oblig1_6 >= 19:
#         if oblig7_8 == sum(maks_poeng[6:8]):
#             return True
#         else:
#             return False
#     else:
#         return False
# student = Student([2, 4, 5, 6, 3, 4, 1, 1])
# x = obliger_godkjent(student)
# print(x)

#oppgave_3a
class Dato:
    def __init__(self, dd: int, mm: int, aaaa: int):
        assert len(str(dd))==2 and dd < 32, f"Lengden må være desimaltall"
        assert len(str(mm))==2 and mm < 13, f"Lengden må være desimaltall"
        assert len(str(aaaa))==4 and aaaa < 2024, f"Lengden må være desimaltall"
        self._dagnr = dd
        self._mnd = mm
        self._år = aaaa

    def dagnr(self):
        return self._dagnr
    
    def mnd(self):
        return self._mnd
    
    def år(self):
        return self._år
    
    def __repr__(self):
        return f" {self._dagnr}, {self._mnd}, {self._år}"

dato1 = Dato(23, 12, 2021)
print(Dato.__code__)

# print(dato1.__dict__)


    
# def lagkalender2023():
#     kalender = []
#     for dag in range (32):
#         for mnd in range (13):
#             kalender.append(Dato (dag, mnd, 2023))
#     return kalender

# x = lagkalender2023()
    
# def fjern_ugyldige_datoer(x):
#     dageriMnd = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#     gyldige_datoer = []
#     for dato in x:
#         dag = dato.dagnr()
#         måned = dato.mnd()
#         år = dato.år()
        
#         if (måned in dageriMnd) and (dag <= dageriMnd[måned]):
#             gyldige_datoer.append(dato)
    
#     return gyldige_datoer
# y = fjern_ugyldige_datoer(x)
# print(y)


