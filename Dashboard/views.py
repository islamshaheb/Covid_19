from django.shortcuts import render
import  requests

# Create your views here.

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None;
    district=["Comilla", "Feni", "Brahmanbaria","Rangamati","Noakhali", "Chadpur", "Lakkhipur", "Chittagong", "CoxsBazar", "Khagrasari", "Bandarban", "Shirajganj", "Pabna", "Bagura", "Rajshahi", "Nator", "Jaypurhat", "ChapayNababganj", "Nauga", "Jessor", "Shatkhira","Meherpur","Narayl", "Chuadanga", "Kustia", "Magura", "Khulna", "Bagerhat", "Jhinaydaha", "Jhalkathi", "Patuakhali", "Pirojpur", "Barishal","Bhola","Barguna", "Shylet","Moulavibazar", "Habiganj", "Shunamganj", "Narshingshi", "Gazipur", "Shariotpur", "Narayanganj", "Tangail", "kishorganj", "Manikganj", "Dhaka", "Munshiganj", "Rajbari", "Madaripur", "Gopalganj", "Faridpur", 	"Panchaganj", "Dinajpur", "Lalmonirhat", "Nilfamari", "Gaybandha", "Thakurgau", "Rangpur", "Kurigram", "Sherpur", "Maymanshing", "Jamalpur", "Netrokona"]
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    all= zip(district, countries)
    return render(request , 'dash.html' , {'globalSummary' : globalSummary ,'all' : all})
