from django.shortcuts import render
from myportfolio.forms import ContactForm, myProjectsForm
from myportfolio.models import NewProject
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.

def index(request):
    return render(request, 'myportfolio/index.html')

def home(request):
    return render(request, 'myportfolio/home.html')

def about(request):
    return render(request, 'myportfolio/about.html')

def projects(request):
    projects_list = NewProject.objects.all()
    projects_dict = {'projects': projects_list}
    return render(request, 'myportfolio/projects.html', context=projects_dict)

def skills(request):
    return render(request, 'myportfolio/skills.html')

def project_form(request):
    form = myProjectsForm
    added = False
    if request.method == 'POST':
        form = myProjectsForm(request.POST)
        if(form.is_valid()):
            added = True
            form.save(commit=True)
        else:
            added = False
    return render(request, 'myportfolio/projectform.html', {'form': form, 'added': added})

def contact(request):
    submitted = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if(form.is_valid()):
            submitted = True
            form.save(commit=True)
            firstname = str(form.cleaned_data['firstname'])
            lastname = str(form.cleaned_data['lastname'])
            email = str(form.cleaned_data['email'])
            phone = str(form.cleaned_data['phone'])
            comments = str(form.cleaned_data['comments'])

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login('info.portfolio1@gmail.com', 'iamlegend@1234')
            subject = 'New Contact Information Received !'
            html = '''\
            <html>
            <head>
            <style>
                .contactinfo{
                    border: 1px solid blue;
                    border-radius: 10px;
                    padding: 5px 15px;
                    width: 30%;
                    margin: 0 auto; 
                }
                .anchor-tag{
                    text-align: center;
	                background:green;
	                width:90%;
	                padding:10px;
                }
                .anchor-tag a{
                    text-decoration:none; 
                    color:#fff;
                }
            </style>
            </head>
            <body>
            <h2>
                Hey Uzval,<br><br> A new person is waiting to connect with you. Please find the info. below :) <br>
            </h2>
            <hr>
            <div class = 'contactinfo'>
                <p style='text-align:center; font-size: 24px'><u><b>Contact Information</b></u></p> 
            <h3>First name: 
            ''' +firstname+ '''</h3>
            <h3>Last name: 
            ''' +lastname+ '''</h3>
            <h3>Full name: 
            ''' +firstname+' '+lastname+ '''</h3>
            <h3>Email: 
            ''' +email+ '''</h3>
            <h3>Phone: 
            ''' +phone+ '''</h3>
            <h3>Comments: 
            ''' +comments+ '''</h3><br>
            <div class = 'anchor-tag'>
                <a href="https://uzvalmallepeddi.pythonanywhere.com/admin">Check out all submissions</a>
            </div>
            <br>
            </div>
            <hr>
            <h3>Thanks,<br>Uzval's Portfolio Team</h3>
            </body>
            </html>
            '''
            msg = MIMEMultipart()
            msg['To'] = 'uzval007@gmail.com'
            msg['From'] = 'info.portfolio1@gmail.com'
            msg['Subject'] = subject
            msg.attach(MIMEText(html, 'html'))
            message = msg.as_string()
            server.sendmail('info.portfolio1@gmail.com', 'uzval007@gmail.com', message)
            server.quit()

            #return home(request)
        else:
            submitted = False
    return render(request, 'myportfolio/contact.html', {'form':form, 'submitted': submitted})
