from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from django.http.response import JsonResponse,HttpResponse
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.decorators import parser_classes
from .serializers import EmployeeSerializers,AdminSerializers
from .models import employee
from rest_framework.request import Request
from django.shortcuts import redirect


@csrf_exempt
def register(request):
    if request.method=='POST':
       employeedata=JSONParser().parse(request)
       email=employeedata.get('email')
       try:
           employee.objects.get(email=email)
           return JsonResponse("Employee with this email ID already exists",safe=False)
       except employee.DoesNotExist:
        employeeserializers = EmployeeSerializers(data=employeedata)
        if employeeserializers.is_valid():
            employeeserializers.save()
            return JsonResponse("Employee added successfully",safe=False)
        else:
            return JsonResponse("Cannot add Employee",safe=False)
@csrf_exempt
def login(request):
    if request.method=='POST':
       employeedata=JSONParser().parse(request)
       email=employeedata.get('email')
       password=employeedata.get('password')
       try:
            Employee=employee.objects.get(email=email)
            if email == Employee.email and Employee.roles == "General User":
                if email == Employee.email and password != Employee.password:
                    return JsonResponse("Invalid Password For General User",safe=False)
                elif email == Employee.email and password == Employee.password:
                    return JsonResponse("Login Successful For General User",safe=False)
            elif email == Employee.email and Employee.roles == "Admin":
                 if email == Employee.email and password != Employee.password:
                     return JsonResponse("Invalid Password For Admin",safe=False)
                 elif email == Employee.email and password == Employee.password:
                     return JsonResponse("Login Successful For Admin",safe=False)
       except:
            return JsonResponse("Invalid Credentials",safe=False)

@csrf_exempt
def profile(request):
    if request.method=="POST":
       employeedata=JSONParser().parse(request)
       email=employeedata.get('email')
       Employee=employee.objects.get(email=email)
       profileimage=Employee.ProfileImage
       profileimg_url=""
       if not profileimage:
           pass
       else:
           profileimg_url=profileimage.url
       employeedata={
            'firstname':Employee.FirstName,
            'lastname':Employee.LastName,
            'designation':Employee.Designation,
            'email':Employee.email,
            'phone':Employee.Mobno,
            'address':Employee.address,
            'gender':Employee.Gender,
            'Dob':Employee.DOB,
            'profileimg':profileimg_url
        }
       return JsonResponse(employeedata,safe=False)

@csrf_exempt
def edit(request):
    if request.method=="POST":
       employeedata=JSONParser().parse(request)
       email=employeedata.get('email')
       Employee=employee.objects.get(email=email)
       profileimage=Employee.ProfileImage
       aadharimage=Employee.AadharImage
       if not profileimage:
           profileimg_url="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3.webp"
       else:
           profileimg_url=profileimage.url
       if not aadharimage:
           aadharimage_url="https://www.bing.com/images/search?view=detailV2&ccid=SjAyAH0I&id=094DED0186956EA031E046990AF9913EC49F7222&thid=OIP.SjAyAH0IdYCvSm7_UGNGWQHaFP&mediaurl=https%3a%2f%2fwww.91-cdn.com%2fpricebaba-blogimages%2fwp-content%2fuploads%2f2021%2f01%2fAadhar-card.png&exph=426&expw=602&q=aadhar+transparent+image&simid=608031575608872258&FORM=IRPRST&ck=F2977A66BB9018D09DDD95C6DADC1339&selectedIndex=6"
       else:
           aadharimage_url=aadharimage.url
       employeedata={
            'firstname':Employee.FirstName,
            'lastname':Employee.LastName,
            'designation':Employee.Designation,
            'department':Employee.Department,
            'email':Employee.email,
            'phone':Employee.Mobno,
            'address':Employee.address,
            'gender':Employee.Gender,
            'Dob':Employee.DOB,
            'profileimg':profileimg_url,
            'aadharno':Employee.AadharNumber,
            'aadharimg':aadharimage_url
        }
       return JsonResponse(employeedata,safe=False)

@csrf_exempt
@parser_classes([MultiPartParser,FormParser])
def edit1(request,email):
    if request.method == 'PUT':
       drf_request = Request(request, parsers=[MultiPartParser(), FormParser()])
       employeedata=drf_request.data
       Employee=employee.objects.get(email=email)
       if 'FirstName' in employeedata and employeedata['FirstName'] != "":
           Employee.FirstName=employeedata['FirstName']
       
       if 'LastName' in employeedata and employeedata['LastName'] !="":
           Employee.LastName=employeedata['LastName']

       if 'Gender' in employeedata and employeedata['Gender'] != "":
            Employee.Gender = employeedata['Gender']
        
       if 'address' in employeedata and employeedata['address'] != "":
            Employee.address = employeedata['address']

       if 'DOB' in employeedata and employeedata['DOB'] != "":
            Employee.DOB = employeedata['DOB']
        
       if 'Department' in employeedata and employeedata['Department'] != "":
            Employee.Department = employeedata['Department']
        
       if 'Designation' in employeedata and employeedata['Designation'] != "":
            Employee.Designation = employeedata['Designation']
        
       if 'AadharNumber' in employeedata and employeedata['AadharNumber'] != "":
            Employee.AadharNumber = employeedata['AadharNumber']
        
       if 'ProfileImage' in employeedata and employeedata['ProfileImage'] != None and employeedata['ProfileImage'] != "" and employeedata['ProfileImage'] != "null":
            Employee.ProfileImage = employeedata['ProfileImage']

       if 'Mobno' in employeedata and employeedata['Mobno'] != "":
            Employee.Mobno = employeedata['Mobno']

       if 'AadharImage' in employeedata and employeedata['AadharImage'] != None and employeedata['AadharImage'] != "" and employeedata['AadharImage'] != "null":
            Employee.AadharImage = employeedata['AadharImage']
       Employee.save()
       return JsonResponse("Updated Sucessfully",safe=False)

@csrf_exempt
def getadmindata(request):
    if request.method=="GET":
         Employee=employee.objects.all()
         employeeserializers=EmployeeSerializers(Employee,many=True)
         return JsonResponse(employeeserializers.data,safe=False)

@csrf_exempt
def deleteadmindata(request,email): 
    if request.method=="DELETE":
         Employee=employee.objects.get(email=email)
         Employee.delete()
         return JsonResponse("Deleted Successfully",safe=False)




@csrf_exempt
def emailreq(request):
    if request.method == 'POST':
       employeedata=JSONParser().parse(request)
       ema=employeedata.get('email')
       firstname=employeedata.get('FirstName')
       lastname=employeedata.get('LastName')
       mobno=employeedata.get('Mobno')
       send_mail(
                "Request For joining In Bariflolabs",  # Email subject
                "Hello HR \n The Employee "+firstname +" "+lastname+" Wanted to Upload Documents. He has the Mob no as "+mobno+". \n And having email"+ema ,  # Email message
                 ema,  # Sender's email address
                ["gourabmohapatra300@gmail.com"],  # List of recipient email addresses
                 fail_silently=False,  # Raise an exception if sending fails
                 )
       return JsonResponse("Mail Sent Successfully",safe=False)


class adminview(viewsets.ModelViewSet):
      queryset=employee.objects.all()
      serializer_class=EmployeeSerializers

@csrf_exempt
def register_view(request):
    ema=request.POST['t1']
    un=request.POST['t2']
    p=request.POST['t3']
    try:
       employee.objects.get(email=ema)
       return HttpResponse("Employee Already Exists")
    except employee.DoesNotExist:
       employeedata={'uname':un,'password':p,'email':ema}
       adminserializers=AdminSerializers(data=employeedata)
       if adminserializers.is_valid():
          adminserializers.save()
          return HttpResponse('Employee Added Successfully')
       else:
          return HttpResponse('Cannot Add employee')
       
@csrf_exempt
def register_home(request):
    r=render(request,"admin_view.html")
    return r