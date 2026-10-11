# Shopping amount input lo:
# - ₹5000+ → 20% discount
# - ₹3000–4999 → 10%
# - ₹1000–2999 → 5%
# - Below ₹1000 → No discount
# Final payable amount print karo.

amount=int(input("Enter your amount:"))

if(amount>5000):
    discount=amount - amount*(20/100)
    print("your total payable amount is:",discount)
elif(4999>amount>3000):
    discount=amount - amount*(10/100)
    print("your total payable amount is:",discount)
elif(2999>amount>1000):
    discount=amount - amount*(5/100)
    print("your total payable amount is:",discount)
else:
     print("your total payable amount is:" , amount)