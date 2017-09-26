print("welcome to burger simulation")
open=input("is the store open?")
if open == "yes":
    item={"cheese":{"amount":10,"price" : 5},
      "bun":{"amount":10,"price" : 2},
      "meat":{"amount":10,"price" : 5}}
    income=0
    for i in range(1, 11):
        item['bun']['amount'] -= 1
        income+=1*item['bun']['price']

    print("current income"+str(income))
    addition=input("any addition?")
    if addition =="yes":
        add=int(input("how much?"))
        print(income+add)
        print("store closed")
else:
    print("store closed")