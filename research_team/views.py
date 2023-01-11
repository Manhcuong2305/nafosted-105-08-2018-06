from django.shortcuts import render

# Create your views here.


def research_team(request):
    return render(request, 'research_team/team.html')
