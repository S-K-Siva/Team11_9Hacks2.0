from django.shortcuts import render 
import random
import schedule
from datetime import datetime
data_set = [
    "Full",
    "low",
    "Empty"
]





def Counter_Status(request):
    status = random.choice([0,1,2])
    status1 = random.choice([0,1,2])
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render(request,"index.html",{"status1":data_set[status],"status2":data_set[status1],"Time":current_time})

    