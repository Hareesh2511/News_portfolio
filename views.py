from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'news.html')
def movies_info(request):
    head_msg = 'Movies Information'
    sub_msg1 = "Pushpa antey flower anukuntiva? Fire!"
    sub_msg2 = 'Prabhas plays the role of Rudra in the upcoming mythological film Kannappa'
    sub_msg3 = '"If this Veeramallu says it, you have to listen" '
    type = 'movies'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'news.html',my_dict)

def sports_info(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'a variation of volleyball where players form a single line'
    sub_msg2 = 'IPL will come in 2026'
    sub_msg3 = 'PKL 2025: Dabang Delhi KC beat Puneri Paltan in final to win Pro Kabaddi'
    type = 'sports'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'news.html',my_dict)

def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'The Bharatiya Janata Party is a conservative political party in India '
    sub_msg2 = 'The Telugu Desam Party is a political group in India'
    sub_msg3 = 'AP Deputy CM was Pawan Kalyan'
    type = 'politics'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'news.html',my_dict)
