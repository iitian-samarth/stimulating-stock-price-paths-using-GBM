import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


s,mu,sigma=100,0.08,0.20
N=1000
total_time=1
dt=1/252
strike_price=105
steps=int(total_time/dt)



Z=np.random.normal(0,1,(steps,N))
S=np.zeros((steps+1,N))
S[0]=s

for i in range(1,steps+1):
    S[i]=S[i-1]* np.exp((mu-0.5*sigma**2)*dt+sigma*dt**0.5*Z[i-1])

plt.figure(figsize=(10,5))
plt.plot(S)
plt.title("stock price paths:GBM")
plt.xlabel("days")
plt.ylabel("stock price")
plt.show()

ST=S[-1]


plt.figure(figsize=(10,5))
plt.hist(ST,bins=35)
plt.title("histogram of final stock prices after 1 year")
plt.xlabel("final prices")
plt.ylabel("Frequency")
plt.show()

payoffs=np.maximum(ST-105,0)
expected_value_call_option=np.mean(payoffs)

theo_mean=s*np.exp(mu*total_time)
theo_std=s*np.exp(mu*total_time)*(np.exp(sigma**2*total_time)-1)**0.5

simulated_mean=np.mean(ST)
simulated_std=np.std(ST)

final_summary=pd.DataFrame([[theo_mean,simulated_mean],[theo_std,simulated_std]],
                           columns=["theoretical","simulated"],
                           index=["Mean Final price","std final price"])


print(f"the final summary table is: \n {final_summary}\n")


print(f"the call option simulated price is: {expected_value_call_option}")







