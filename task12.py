#currency conversion for international billing

amount_in_inr=float(input("enter amount in INR:"))
conversion_rate=float(input("enter the conversion rate:"))

#converting INR to USD
amount_in_usd=amount_in_inr/conversion_rate

#applying %2 processing fee
processing_fee=amount_in_usd*0.02

#final amount
final_amount=amount_in_usd+processing_fee

print(f"Amount in USD{' '*2}:{' '*2}{amount_in_usd}")
print(f"Processing fee{' '*2}:{' '*2}{processing_fee}")
print(f"final amount{' '*2}:{' '*2}{final_amount}")
