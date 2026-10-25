from django.shortcuts import render



def serve_tailwind(req):
    return render(req, 'chai/all_chai.html')