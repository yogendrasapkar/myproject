from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

#for apis
from .serializers import medicalsummarySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import medicalsummary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = UserCreationForm()
    return render(request, "register.html", {"form": f})

def signin(request):
    if request.method == "POST":
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pd = f.cleaned_data['password']
            user = authenticate(username = un, password = pd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home')
    else:
        f = AuthenticationForm()
    return render(request, 'signin.html', {'form': f})

def home(request):
    return render(request, 'home.html',  {'name': request.user})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/signin')


# Medical summary api's
# Get all the records
@api_view(['GET'])
def getAllMedicalSummary(request):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.all()
        serialize = medicalsummarySerializer(medicalRecord, many=True)
        return Response(serialize.data)

# Get only one record based on id
@api_view(['GET'])
def getOneMedicalSummary(request, pk):
    if request.method == 'GET':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(medicalRecord, many=False)
        return Response(serialize.data)

# Add one record
@api_view(['POST'])
def addOneRecord(request):
    if request.method == 'POST':
        serialize = medicalsummarySerializer(data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)

# Update a record based on id
@api_view(['POST'])
def updateRecord(request, pk):
    if request.method == 'POST':
        medicalRecord = medicalsummary.objects.get(id=pk)
        serialize = medicalsummarySerializer(instance=medicalRecord, data=request.data)
        if(serialize.is_valid()):
            serialize.save()
            return Response(serialize.data)

# Delete a record
@api_view(['DELETE'])
def deleteRecord(request, pk):
    if request.method == 'DELETE':
        medicalRecord = medicalsummary.objects.get(id=pk)
        medicalRecord.delete()
        return Response("Record deleted successfully")

# class medicalsummaryView(APIView):
#     def get(self, request):
#         player1 = medicalsummary.objects.all()
#         serialize = medicalsummarySerializer(player1, many=True)
#         return Response(serialize.data)

#     def get(self, request, pk, format=None):
#         player1 = medicalsummary.objects.get(id=pk)
#         serialize = medicalsummarySerializer(player1, many=False)
#         return Response(serialize.data)
    
#     def post(self, request):
#         serialize = medicalsummarySerializer(data=request.data)
#         if(serialize.is_valid()):
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors)

