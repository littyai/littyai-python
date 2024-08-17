#!/usr/bin/python
import time

def check(condition):
    print("Initializing AI analysis... 🤖")
    time.sleep(1)  
    print("Analyzing data... 📊")
    time.sleep(1.5)  

    if condition:
        response = "✔️ Analysis complete!\n" \
                   "Outcome: Positive - The condition meets all criteria! 🟢"
    else:
        response = "❌ Analysis complete!\n" \
                   "Outcome: Negative - The condition failed to meet the criteria. 🔴"
    
    return response

result = check(5 > 3)
print(result)
