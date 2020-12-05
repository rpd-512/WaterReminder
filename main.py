from notifypy import Notify #if not available, install with "pip3 install notify-py"
from time import sleep
from random import randint as rndint

d = 20 #notification duration. (in minutes)

notify = Notify()
facts = ["Only 1.1% of the water on earth is suitable for drinking as is.",
        "Our bodies consist of 55 – 75% water",
        "Depression and fatigue can often be symptoms of dehydration.",
        "Adult humans are 60 percent water, and our blood is 90 percent water.",
        "Water is essential for the kidneys and other bodily functions.",
        "When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling.",
        "Drinking water instead of soda can help with weight loss.",
        "Children in the first 6 months of life consume seven times as much water per pound as the average American adult.",
        "Water is Part of a Deeply Interconnected System.",
        "A Person Can Only Live About a Week Without Water.",
        "Water Regulates the Earth's Temperature.",
        "Approximately 80% of your brain tissue is made of water"]
while (True):
    sleep(60*d)
    notify.title = "Water Reminder | Please drink a glass of water"
    randfacts = facts[rndint(0,len(facts)-1)]
    notify.message = randfacts
    notify.icon = "icon/icon.png"
    notify.send()
