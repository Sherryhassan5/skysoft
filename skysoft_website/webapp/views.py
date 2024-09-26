from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .models import job as jb
from .models import job_application as jb_ap
from django.core.mail import EmailMessage
from django.db.models import Q
# Create your views here.


# def base_template(request):
#     social_data = social.objects.all()
#     context = {'social', social_data}
#     return render(request,'webapp/base.html',context)



def home(request):
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    qualities_section_data = qualities_section.objects.get(id=1)
    qualities_section_cards = qualities_section_data.card.all()
    big_card_data = big_card.objects.all()
    big_card_card_data = big_card_card.objects.all()
    social_data = social.objects.all()
    context = {'header_data':header_data,
               'logos':logos,
               'qualities_section_data':qualities_section_data,
               'qualities_section_cards':qualities_section_cards,
               'big_card_data':big_card_data,
               'big_card_card':big_card_card_data,
               'social':social_data,
               }
    
    return render(request, 'webapp/index.html',context)
    


def about(request):
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    main_data = about_header.objects.get(id=1)
    about_header_cards = main_data.card.all()
    about_big_card_data = about_big_card.objects.all()
    about_banner_data = about_banner.objects.get(id=1)
    social_data = social.objects.all()
    
    
    
    context = {
        'logos':logos,
        'main_data':main_data,
        'about_header_cards':about_header_cards,
        'about_big_card':about_big_card_data,
        'about_banner':about_banner_data,
        'social':social_data,
        }
    
    return render(request, 'webapp/about_us.html',context)


# def career(request):
    
#     job_data = jb.objects.all()  # Default query to get all job listings

#     if request.method == 'GET':
#         searched_job = request.GET.get('Searched_job', '')  # Get the search term from the query params
#         if searched_job:
#             job_data = jb.objects.filter(title__icontains=searched_job)  # Filter jobs based on search term
#         print(searched_job)  # Useful for debugging; remove or log in production
    
#     # Fetch header data, handle cases where no header exists
#     try:
#         header_data = home_header.objects.get(id=1)
#         logos = header_data.header_logos.all()  # Assuming a Many-to-Many relationship
#     except home_header.DoesNotExist:
#         header_data = None
#         logos = None  # Handle missing header data gracefully
    
#     context = {'job_data': job_data, 'logos': logos}
#     return render(request, 'webapp/career.html', context)


def career(request):
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    job_data = jb.objects.all()  # Default query to get all jobs
    search_term = request.GET.get('Searched_job', '')  # Get search term from the request
    print(search_term)
    # Check if there's a search term
    if search_term:
        # Use Q objects to search in multiple fields
        job_data = jb.objects.filter(
            Q(title__icontains=search_term) |
            Q(location__icontains=search_term) |
            Q(role__icontains=search_term) |
            Q(job_type__icontains=search_term) |
            Q(work_time__icontains=search_term)
        )
    
    # Handle the case where no jobs match the search term
    if not job_data.exists():
        message = "No jobs found matching your search criteria."
    else:
        message = None

    # Fetch header data, handle potential missing header
    

    # Pass job data and message to the context
    context = {'job_data': job_data, 'logos': logos, 'message': message}
    return render(request, 'webapp/career.html', context)




















def job(request,id):
    job_data = jb.objects.get(id = id)
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    
    context = {
        'job_data':job_data,
        'logos':logos,
    }
    return render(request, 'webapp/job.html',context)

def job_application(request,id):
    job_data = jb.objects.get(id=id)
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    
    print('soomething')
    if request.method == 'POST':
        print("entered in post")
        data = request.POST
        first_name = data.get('first-name')
        last_name = data.get('last-name')
        email = data.get('email')
        phone = data.get('phone')
        company = data.get('company')
        experience = data.get('exp')
        current_salary = data.get('current-salary')
        expect_salary = data.get('expect-salary')
        note = data.get('note')
        consent = data.get('consent')
        if consent == 'on':
            consent = True
        else:
            consent=False
        print(consent,type(consent)) 
        
        # print("requested files",request.FILES)
        resume_file = request.FILES.get('resume')  # This is how you get the file from the form

        try:
            # Handle file upload and save the resume
            if resume_file:
                new_resume = resume(resume=resume_file)
                new_resume.save()
            else:
                print("file not uploaded")
                raise Exception("file not uplloaded")
            new_job_application = jb_ap(
                job_id=job_data,  # Foreign key to the job
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                company=company,
                exp=experience,
                current_salary=current_salary,
                expect_salary=expect_salary,
                resume=new_resume,  # Link the uploaded resume
                note=note,
                consent = consent,
            )
            new_job_application.save()
            
            
            email_from = 'sherazhassanxd@gmail.com'  # Default sender 
            

            # Email message
            subject = f"Application for {job_data}"
            message = f"""
            Hello,
            <br>
            We have got a application for <strong>{job_data}</strong> the person is <strong>{first_name} {last_name}</strong>.
            His email address is <strong>{email}</strong>, Phone <strong>{phone}</strong>, and having <strong>{experience}</strong> years of experience.
            <br>
            Please checkout the details in dashboard <br><br>
            I am also attaching the resume here<br><br>
            Thank you
            """

            # Fetch the specific GC's email using gc_id

            email = EmailMessage(
                subject,#type: ignore
                message,
                email_from,
                ['sherazhassan240@gmail.com'],  # Send email to the specific GC
                
            )
            email.content_subtype = 'html'

            # Attach the PDF if it's in the request
            pdf_file = resume_file
            if pdf_file:
                email.attach(pdf_file.name, pdf_file.read(), 'application/pdf')

            email.send()

            
            
            
            
            
            print("application submitted successfully")
            
            return redirect(home)
        except Exception as e:
            print(f'something bad has happend and data is not saved due to {e}')
    
    context = {'job_data':job_data,
               'logos':logos,}
    return render(request, 'webapp/job-application.html', context)


def contactus(request):
    our_details = our_contact_detail.objects.get(id=1)
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        msg = data.get('message')
        try:
            new_msg = contact_form_detail(
                name=name,
                email=email,
                subject=subject,
                message=msg,
            )
            new_msg.save()
            
            print("msg send succesfully")
            return redirect(contactus)
        except Exception as e:
            print(e)
    
    context = {
        'logos':logos,
        'our_details':our_details,
    }
    return render(request, 'webapp/Contact.html',context)





def contact_project(request):
    print("get outside")
    header_data = home_header.objects.get(id=1)
    logos = header_data.header_logos.all()
    
    if request.method == 'POST':
        print("get inside")
        data = request.POST
        first_name = data.get('first-name')
        last_name = data.get('last-name')
        email = data.get('email')
        phone = data.get('phone')
        region = data.get('region')
        company = data.get('company')
        detail = data.get('detail')
        consent = data.get('consent')
        if consent == 'on':
            consent = True
        else:
            consent=False
        print(consent,type(consent))        
        try:
            new_project = project_details(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                company=company,
                region=region,
                detail=detail,
                consent = consent,
            )
            new_project.save()
            email_from = 'sherazhassanxd@gmail.com'  # Default sender 
            

            # Email message
            subject = f"Project Details have recieved"
            message = f"""
            Hello,
            <br>
            We have got a recieved details for a project from <strong>{first_name} {last_name}</strong>some of the details are <strong>{detail}</strong>
            <br>
            Please checkout the details in dashboard <br><br>
            Thank you
            """

            # Fetch the specific GC's email using gc_id

            email = EmailMessage(
                subject,#type: ignore
                message,
                email_from,
                ['sherazhassan240@gmail.com'],  # Send email to the specific GC
                
            )
            email.content_subtype = 'html'

            # Attach the PDF if it's in the request
            
            email.send()

            
            
            print("project succesfully submitted")
            return redirect(contact_project)
        except Exception as e:
            print(e)

    context = {
        'logos':logos,
    }    
    return render(request, 'webapp/contact_project.html',context)


