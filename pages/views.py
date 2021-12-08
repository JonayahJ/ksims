from django.shortcuts import render

# Index
def index(request):
    return render(request, "index.html", {})

# About
def about(request):
    return render(request, "about.html", {})

# Contact
def contact(request):
    return render(request, "contact.html", {})

################ RESEARCH PAGES ################

# The TITLE Study
#def about(request):
#    return render(request, "about.html", {})

# About
def health_retirement(request):
    return render(request, "health_retirement.html", {})

# The Jackson Heart Study
def jackson_heart(request):
    return render(request, "jackson_heart.html", {})