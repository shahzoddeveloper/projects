def kvadrat():
    tall = input("Tall: ")
    tall = int(tall)

    print(tall, "*", tall, "=", tall * tall)

a = True 
b = False

if a:
    kvadrat()

if b:
    kvadrat()

print("En gang til:")
kvadrat()
