from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Registration(models.Model):
     
     GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Women', 'Women'),
        ('Prfer Not to say', 'Prfer Not to say'),
        )
     
     STATES_CHOICES= (
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CT', 'Chhattisgarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PY', 'Puducherry'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal')
        )
     
     Full_Name = models.CharField(max_length = 200)
     Email_address = models.EmailField(max_length=200)
     Phone_number = models.CharField(max_length = 12,null=True, blank=True)
     Gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
     Street_address = models.CharField(max_length=200,null=True, blank=True)
     state=models.CharField(choices=STATES_CHOICES, max_length=50)
     City = models.CharField(max_length=100,null=True, blank=True)
     Age = models.IntegerField(default=0,null=True, blank=True)
     dob = models.DateField(null=True, blank=True)

