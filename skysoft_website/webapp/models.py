from django.db import models

# Create your models here.





# home header 

class home_header_logos(models.Model):
    image_src = models.ImageField(upload_to='media/webapp/header_logos/')
    
    # def __str__(self) -> str:
    #     return str(self.image_src)


class home_header(models.Model):
    header_heading = models.CharField(max_length=160,blank=True,null=True)
    header_paragraph = models.TextField(blank=True, null=True)
    header_btn_title = models.CharField(max_length=25,blank=True,null=True)
    header_btn_link = models.TextField(blank=True,null=True)
    header_logos = models.ManyToManyField(home_header_logos)
    
    def __str__(self) -> str:
        return "Home header data"



# 2nd section



class qualities_cards(models.Model):
    card_img = models.ImageField(upload_to='media/webapp/qualities_card/',blank=True,null=True)
    card_title = models.TextField(blank=True,null=True)
    card_des = models.TextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.card_title


class qualities_section(models.Model):
    heading = models.TextField(blank=True,null=True)
    des = models.TextField(blank=True,null=True)
    domain_count = models.IntegerField(default=20)
    domain_count_des = models.TextField(blank=True,null=True)
    time_duration = models.CharField(max_length=30,blank=True,null=True)
    time_duration_des = models.TextField(blank=True, null=True)
    card = models.ManyToManyField(qualities_cards)


    def __str__(self) -> str:
        return "Qualities section data"




class big_card(models.Model):
    card_icon = models.ImageField(upload_to='media/webapp/big_card')
    small_heading = models.TextField(blank=True,null=True)
    heading = models.TextField(blank=True,null=True)
    des = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to='media/webapp/big_card')

    def __str__(self) -> str:
        return self.small_heading
    



class big_card_card(models.Model):
    img = models.ImageField(upload_to='media/webapp/big_card_card')
    heading = models.CharField(max_length=400, blank=True,null=True)
    des = models.TextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.heading
    


class social(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/webapp/social')
    link = models.TextField()
    
    def __str__(self) -> str:
        return self.name


#   about


class about_header_of_card(models.Model):
    icon = models.ImageField(upload_to='media/webapp/about_header')
    heading = models.CharField(max_length=100)
    des = models.TextField()
    
    def __str__(self) -> str:
        return self.heading

class about_header(models.Model):
    heading = models.TextField()
    des = models.TextField()
    card = models.ManyToManyField(about_header_of_card,blank=True)
    
    def __str__(self) -> str:
        return self.heading
    
    
class about_big_card(models.Model):
    img = models.ImageField(upload_to='media/webapp/about/big_card')
    small_heading = models.CharField(max_length=200)
    heading = models.TextField()
    des = models.TextField()
    
    
    def __str__(self) -> str:
        return self.heading      

    
class about_banner(models.Model):
    brief = models.CharField(max_length=200)
    heading = models.TextField()
    des = models.TextField()
    
    def __str__(self) -> str:
        return self.heading



# careers

class job(models.Model):
    JOB_TYPES = [
        ('On-Site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]
    JOB_TIMES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('On weekend', 'On weekend'),
    ]
    title = models.CharField(max_length=300)
    job_type = models.CharField(
        max_length=10,
        choices=JOB_TYPES,
        default='On-Site',  # Set a default value (optional)
    )
    location = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    work_time = models.CharField(
        max_length=20,
        choices=JOB_TIMES,
        default='Full Time',
    )
    des = models.TextField(verbose_name='Description')
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the time when the job is created


    def __str__(self) -> str:
        return self.title
    
    
    
class resume(models.Model):
    resume = models.FileField(upload_to='media/webapp/resumes')
    
    def __str__(self) -> str:
        return str(self.resume)    
    
    
class job_application(models.Model):
    job_id = models.ForeignKey(job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone =  models.CharField(max_length=14)
    company = models.CharField(max_length=500)
    exp = models.CharField(max_length=400)
    current_salary = models.CharField(max_length=16)
    expect_salary = models.CharField(max_length=16)
    resume = models.OneToOneField(resume , on_delete=models.CASCADE)
    note = models.TextField()
    consent = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.job_id.title
    
    
    
# contact

# contact datail

class our_contact_detail(models.Model):
    address = models.CharField(max_length=200)
    street_address = models.CharField(max_length=500)
    phone = models.CharField(max_length=16)
    timings = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    
    
    def __str__(self) -> str:
        return self.address
    
    
class contact_form_detail(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.subject
    
    
    # project
    
class project_details(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone =  models.CharField(max_length=14)
    company = models.CharField(max_length=500)
    region = models.CharField(max_length=400)
    detail = models.TextField()
    consent = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.first_name + " project"