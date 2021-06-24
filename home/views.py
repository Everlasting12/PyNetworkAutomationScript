from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from home.models import Contact, Script, Tutorial
from home.forms import TutorialRegistration, ScriptFormRegistration
from django.http import HttpResponse 
import time
# mail function and HTML as an email
from django.core.mail import send_mail, EmailMessage

# for class based views
# from django.views import View

from django.core.mail import EmailMultiAlternatives
#to send a tepmplate as an email
from django.template.loader import render_to_string, get_template

from django.utils.html import strip_tags
#  importing settings module
from django.conf import settings

# Create your views here.
# def box(request):
#     return render(request,'box.htm')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def home(request):
    context = {'home':'active'}
    return render(request, 'home.htm', context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def services(request):
    if request.user.is_authenticated:    
        scriptfiles = Script.objects.all()
        context = {'services':'active', 'scriptfiles': scriptfiles}
        return render(request, "services.htm", context)
    else:
        messages.error(request,'Sign Up is required!')
        messages.info(request,'We are redirecting you to registration page as you are not a registered user. If you are, then please go to Login Page.')
        return redirect('registration')


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def contact(request):
    context = {'contact':'active'}
    if request.method == 'POST':
            uname = request.POST['uname']
            email = request.POST['email']
            phone = request.POST['phone']
            desc = request.POST['desc']
            contact = Contact(uname=uname, email=email, phone=phone, desc=desc, date=datetime.today())


            if User.objects.filter(username=uname).exists():
                if User.objects.filter(email=email).exists():
                    to = request.POST.get('email')
                    send_mail(
                            #subject
                            "Contact", 
                            #  message 
                            "Thank you for contacting us on the PyNAS portal.\nWe will look into the matter very soon and update you regarding the same. \nThank you for using our Services",
                            # from email
                        #    
                        settings.EMAIL_HOST_USER,
                            # to recipient mail, 
                            [to]
                        )

                    send_mail(
                            #subject
                            "Contact", 
                            #  message 
                            "From : "+email+",\n\nMessage:\n"+desc,
                            # from email
                        #   
                            to,
                            [settings.EMAIL_HOST_USER]
                            # to recipient mail, 
                            
                        )
                


                    contact.save()
                    messages.success(request, 'Message sent successfully !')
                    return render(request, 'contact.htm',context)
                else:
                    messages.error(request, 'Email does not exits')
                    return render(request, 'contact.htm',context)
            else:
                messages.info(request, 'Username does not exist! Register Yourself ')
                return redirect('registration')
    else:
        return render(request, 'contact.htm',context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def tutorials(request):
    scriptfiles = Script.objects.all()
    tutorialfile = Tutorial.objects.all()
    context = {'tutorial':'active','scriptfiles':scriptfiles,'tutorialfile':tutorialfile}
    return render(request, 'tutorials.htm',context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def about(request):
    context = {'about':'active'}
    return render(request, 'about.htm',context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def login(request):
    context = {'user':'active'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.htm',context)



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('home')


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def registration(request):
    context = {'user':'active'}
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
      
     
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email ID is Taken ! Try Another')
            return redirect('registration')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken! Try Another ')
                return redirect('registration')
            else:
                if password1 == password2:
                    
                    # To send email 
                    subject = "Registration"
                    content = "Thank you for registering on the PyNAS portal. \nThank you for using our Services."
                    to = request.POST.get('email')
                   
                    # send_mail(
                    #     #subject
                    #     "Registration", 
                    #     #  message 
                    #     " Thank you for registering on the PyNAS portal. \n Thank you for using our Services",
                    #     # from email
                    # #    
                    # settings.EMAIL_HOST_USER,
                    #     # to recipient mail, 
                    #     [to]
                    # )
                    
                    
                   
                    email_html_template = get_template(template_name="emailtemp.html").render({'content':content})
                    emailmsg = EmailMessage(subject,email_html_template, settings.EMAIL_HOST_USER, [to])
                    emailmsg.content_subtype = 'html'
                    emailmsg.send(fail_silently=False)
                   


                    user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, f"Your account created Successfully! Please check your Email, {username}")
                    return redirect('login')
                else:
                    messages.error(request, 'Password and Confirm Password should be Same !')
                    return redirect('registration')
    else:
        return render(request, 'registration.htm',context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def search_services(request):
    query = request.GET['search']
    if len(query)>50:
        scriptfiles = Script.objects.none()
    else:
        scriptfilesName = Script.objects.filter(script_name__icontains=query)
        scriptfilesAuthor = Script.objects.filter(script_author__icontains=query)
        scriptfilesDesc = Script.objects.filter(description__icontains=query)
        scriptfiles = scriptfilesName.union(scriptfilesAuthor, scriptfilesDesc)
    
    if scriptfiles.count() == 0:
        messages.warning(request, 'No search result found. Please refine your query !')
    files = {'scriptfiles': scriptfiles,'query':query}
    return render(request, 'search.htm', files) 

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def addscript(request):
    scriptfiles = Script.objects.all()
    tutorialfile = Tutorial.objects.all()
    tutfm = TutorialRegistration()
    scffm = ScriptFormRegistration()
    context = {'addscript':'active','form':tutfm,'scriptform':scffm,'scriptfiles':scriptfiles,'tutorialfile':tutorialfile}  
    return render(request, 'addscript.html',context)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def upload_files(request):
    if request.method == 'POST' and request.FILES:
        scr_form  = ScriptFormRegistration(request.POST,request.FILES)
        if scr_form.is_valid():
            sn = scr_form.cleaned_data['script_name']
            sd= scr_form.cleaned_data['description']
            sf = scr_form.cleaned_data['script_file']
            an = scr_form.cleaned_data['script_author']
            scr = Script(script_name=sn,description=sd,script_file=sf,script_author=an,date=datetime.today())
            scr.save()
            messages.success(request, 'File uploaded successfully !')
            return redirect('addscriptfile') 
        else: 
            messages.error(request, "Something went wrong, Please try again ! Thank You.") 
            return redirect('addscriptfile')
    else:
        return redirect('addscriptfile')


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def deleteScript(request, pk):
    script = Script.objects.get(pk=pk)
    if request.method == 'POST':
        script.delete()
        messages.success(request, "File deleted successfully!")
        return redirect('services')
    else:
        messages.danger(request, "Error occured while deleting the file!")
        return redirect('services')


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def manual_page(request):            #      Code for the add script template for adding the steps for manual page.
    if request.method=='POST':
        form = TutorialRegistration(request.POST)
        if form.is_valid():
            sn = form.cleaned_data['scriptName']
            pr = form.cleaned_data['preRequisites']
            st = form.cleaned_data['Steps']
            tut = Tutorial(script_name=sn,prerequisite=pr,steps=st,date=datetime.today())
            tut.save()
            messages.success(request, "Manual page created successfully!")
            return redirect('addscriptfile')
        else:
            messages.error(request, "Manual page fail to upload!")
            return redirect('addscriptfile')
    else:
        return redirect('addscriptfile')



# //////////////////////////////////////////////////////////////////////////


def tutorial_view(request,pk):
    try:
        script_info = Script.objects.get(id=pk)
        scriptfiles = Script.objects.all()
        tut_info = Tutorial.objects.get(script_name_id=pk)
        return render(request, 'Searched_tutorial.htm', {'scf':script_info,'tut':tut_info,'scriptfiles':scriptfiles})
    except:
        messages.error(request, "Manual page for the selected Script have not been created yet! ")
        return redirect('tutorials')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def update_script(request,pk):
    script_info = Script.objects.get(id=pk)
    form = ScriptFormRegistration(instance=script_info)
    context = {'form':form,'script_info':script_info}
    return render(request, 'editscript.html',context)

def edit_script(request, pk):
    script_info = Script.objects.get(id=pk)
    form = ScriptFormRegistration(instance=script_info)
    context = {'form':form}
    if request.method == 'POST':
        form = ScriptFormRegistration(request.POST, request.FILES, instance = script_info)
        if form.is_valid():
            form.save()
            messages.success(request,'Script updated successfully!')
            return redirect('services')
        else:
            messages.error(request,'Script fail update!')
            return redirect('update_script')
    else:
        messages.error(request,'Script fail update!')
        return redirect('update_script')
