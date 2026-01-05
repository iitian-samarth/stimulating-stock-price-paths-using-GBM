import matplotlib.pyplot as plt


def NPV(cash,rate):
    total=0
    for t,c in enumerate(cash):
        total += c / ((1+rate)**t)
    return total

def irr_bisection(cash):
    rate_low= -0.99
    rate_high=10
    epsilon=1e-6
    
    npv_lowest=NPV(cash,rate_low)
    npv_highest=NPV(cash,rate_high)
    
    if npv_lowest*npv_highest>0:
        return None
    
    for i in range(0,1000):
        mid_rate=(rate_low+rate_high)/2

        npv_mid=NPV(cash,mid_rate)

        if abs(npv_mid)<epsilon:
            return mid_rate
        elif npv_lowest*npv_mid<0:
            npv_highest=npv_mid
            rate_high=mid_rate
        else:
            npv_lowest=npv_mid
            rate_low=mid_rate
    return None

            
    
    
def plotting_npv(cash):

    rates=[i/100 for i in range(-90,101)]
    npv_rates=[NPV(cash,r)for r in rates]

    plt.figure(figsize=(10,5))
    plt.plot(rates,npv_rates)
    plt.axhline(0)
    plt.xlabel("discount rates")
    plt.ylabel("NPV fucntion")
    plt.title("NPV vs  DISCOUNT RATES")
    plt.show()

def npv_summary(cash):
    rates=[5*r/100 for r in range(0,5)]
    print("the summary table will be:")
    for i in rates:
          
          print(f" {int(i*100)}% : {NPV(cash,i)}\n")


simple_investment=[-10000,3000,4000,5000]
annuity=[-50000,15000,15000,15000,15000]

plotting_npv(simple_investment)
plotting_npv(annuity)

print(f"test case for simple investment with IRR first:{irr_bisection(simple_investment)}\n")

npv_summary(simple_investment)
print("\n\n\n")




print(f"test case for annuity with IRR first:{irr_bisection(annuity)}\n")

npv_summary(annuity)
  

    