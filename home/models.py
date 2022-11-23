from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image as IMG
from django.contrib.auth.models import User
# Create your models here.

########################################################################

# class User(models.Model):
#     Username = models.CharField(max_length=25)
#     Password = models.CharField(max_length=25)

#     def __str__(self):
#         return self.Username

########################################################################

class Feedback(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    # AddedBy = models.ForeignKey(User, on_delete = models.CASCADE , default=1)
    Ip = models.GenericIPAddressField(null=True)

    # Additional
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    Website = models.CharField(max_length=50)
    Message = models.TextField()

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Name

########################################################################

class About(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Title = models.CharField(max_length=50)
    Mission = models.TextField()
    Vision = models.TextField(null=True,blank=True)
    Description = RichTextField(null=True,blank=True)
    Image = models.ImageField(blank=True,null=True,upload_to='about_us')
    Url = models.CharField(max_length=20000,null=True,unique=True)

    #seo
    SMTitle = models.CharField(max_length=2000,blank=True,null=True)
    SMDescription = models.TextField(blank=True,null=True)
    SMKeywords = models.CharField(max_length=2000,blank=True,null=True)

    def __str__(self):
        return self.Title

########################################################################

class Blog(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='blog')
    Url = models.CharField(max_length=20000,unique=True)
    
    # seo
    SMTitle = models.CharField(max_length=2000,blank=True,null=True)
    SMDescription = models.TextField(blank=True,null=True)
    SMKeywords = models.CharField(max_length=2000,blank=True,null=True)

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Title

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Image.path)

    #     if img.height > 600 or img.width > 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)
    #     elif img.height < 600 or img.width < 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)

########################################################################

class Album(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Title = models.CharField(max_length=50)
    Thumbnail = models.ImageField(blank=True,null=True,upload_to='album')
    Images = models.IntegerField(default=0,)
    Url = models.CharField(max_length=20000,null=True,unique=True)

    # seo
    SMTitle = models.CharField(max_length=2000,blank=True,null=True)
    SMDescription = models.TextField(blank=True,null=True)
    SMKeywords = models.CharField(max_length=2000,blank=True,null=True)

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Title


    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Thumbnail.path)

    #     if img.height > 400 or img.width > 400:
    #         output_size = (400,400)
    #         img.thumbnail(output_size)
    #         img.save(self.Thumbnail.path)
    #     elif img.height < 400 or img.width < 400:
    #         output_size = (400,400)
    #         img.thumbnail(output_size)
    #         img.save(self.Thumbnail.path)

########################################################################

class Album_Image(models.Model):
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Album_Name = models.ForeignKey(Album, on_delete=models.CASCADE)
    Image = models.ImageField(blank=True,null=True,upload_to='album-image')

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Album_Name.Title

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Image.path)

    #     if img.height > 800 or img.width > 800:
    #         output_size = (800,800)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)
    #     elif img.height < 800 or img.width < 800:
    #         output_size = (800,800)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)

########################################################################

class Contact(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Company_Name = models.CharField(max_length=50,null=True)
    Adress = models.TextField(null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Mobile = models.CharField(max_length=15,null=True)
    Whatsapp = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=100,null=True)
    Website = models.CharField(max_length=250,null=True)
    Longitude = models.CharField(max_length=30,null=True)
    Latitude = models.CharField(max_length=30,null=True)
    Facebook = models.CharField(max_length=50,null=True)
    Instagram = models.CharField(max_length=50,null=True)
    Linkedin = models.CharField(max_length=50,null=True)
    Twitter = models.CharField(max_length=50,null=True)
    Image = models.ImageField(blank=True,null=True,upload_to='Company')
    Url = models.CharField(max_length=20000,null=True,unique=True)

    # seo
    SMTitle = models.CharField(max_length=2000,null=True)
    SMDescription = models.TextField(null=True)
    SMKeywords = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.Company_Name
    
########################################################################

class Product(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Title = models.CharField(max_length=50, null=True, default=None, blank=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='Product')
    Refer_number = models.CharField(max_length=6)
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Discount = models.IntegerField(default=10)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    Show_Feature = models.BooleanField(default=False, null=True, blank=True)
    Url = models.CharField(max_length=20000,unique=True ,null=True,)
    
    # seo
    SMTitle = models.CharField(max_length=2000, null=True, default=None, blank=True)
    SMDescription = models.TextField(blank=True,null=True)
    SMKeywords = models.CharField(max_length=2000, null=True, default=None, blank=True)

    def __str__(self):
        return self.Title

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Image.path)

    #     if img.height > 600 or img.width > 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)
    #     elif img.height < 600 or img.width < 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)

########################################################################

class Service(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Title = models.CharField(max_length=50, null=True, default=None, blank=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True,null=True,upload_to='Product')
    Refer_number = models.CharField(max_length=6)
    Show_Price = models.BooleanField(default=False, null=True, blank=True)
    Actual_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Offer_Price = models.CharField(max_length=15, null=True, default=None, blank=True)
    Discount = models.IntegerField(default=10)
    Show_Whatsapp = models.BooleanField(default=False, null=True, blank=True)
    Whatsapp_Number = models.CharField(max_length=15, null=True, default=None, blank=True)
    Show_Enquiry = models.BooleanField(default=False, null=True, blank=True)
    Show_Feature = models.BooleanField(default=False, null=True, blank=True)
    Url = models.CharField(max_length=20000,null=True,unique=True)
    
    # seo
    SMTitle = models.CharField(max_length=2000, null=True, default=None, blank=True)
    SMDescription = models.TextField(blank=True,null=True)
    SMKeywords = models.CharField(max_length=2000, null=True, default=None, blank=True)

    def __str__(self):
        return self.Title

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Image.path)

    #     if img.height > 600 or img.width > 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)
    #     elif img.height < 600 or img.width < 600:
    #         output_size = (600,600)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)

########################################################################

class Enquiry(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    # AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    # additional
    Name = models.CharField(max_length=50)
    Mobile_Number = models.CharField(max_length=15,null=True, default=None, blank=True)
    Email = models.EmailField(null=True, default=None, blank=True)
    Product_Name = models.CharField(max_length=50,null=True, default=None, blank=True)
    Whatsapp = models.CharField(max_length=15)
    District = models.CharField(max_length=25,null=True)
    Address = models.TextField()
    Refer_number = models.CharField(max_length=6,null=True, default=None, blank=True)

    class Meta:
        ordering =('-id',)

    def __str__(self):
        return self.Name

########################################################################

class Manage_Menu(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    About_Page = models.BooleanField(default=False, null=True, blank=True)
    Blog_Page = models.BooleanField(default=False, null=True, blank=True)
    Image_Gallery = models.BooleanField(default=False, null=True, blank=True)
    Contact_Page = models.BooleanField(default=False, null=True, blank=True)
    Products_Page = models.BooleanField(default=False, null=True, blank=True)
    Service_Page = models.BooleanField(default=False, null=True, blank=True)
    Feedback_Page = models.BooleanField(default=False, null=True, blank=True)
    Enquiry_Page = models.BooleanField(default=False, null=True, blank=True)
    Group_Company = models.BooleanField(default=False, null=True, blank=True)
    Testimonials = models.BooleanField(default=False, null=True, blank=True)

########################################################################

class Quick_Links(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    About_Page = models.BooleanField(default=False, null=True, blank=True)
    Blog_Page = models.BooleanField(default=False, null=True, blank=True)
    Image_Gallery = models.BooleanField(default=False, null=True, blank=True)
    Contact_Page = models.BooleanField(default=False, null=True, blank=True)
    Optional_Service = models.BooleanField(default=False, null=True, blank=True)
    Optional_Products = models.BooleanField(default=False, null=True, blank=True)
    Products_Page = models.BooleanField(default=False, null=True, blank=True)
    Service_Page = models.BooleanField(default=False, null=True, blank=True)
    Testimonials = models.BooleanField(default=False, null=True, blank=True)

########################################################################

class Group_Of_Companies(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Logo = models.ImageField(blank=True,null=True,upload_to='CompanyLogo')

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Logo.path)

    #     if img.height > 500 or img.width > 500:
    #         output_size = (500,500)
    #         img.thumbnail(output_size)
    #         img.save(self.Logo.path)
    #     elif img.height < 500 or img.width < 500:
    #         output_size = (500,500)
    #         img.thumbnail(output_size)
    #         img.save(self.Logo.path)

########################################################################

class Testimonial(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Tes_Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Testimonial = models.TextField()
    Tes_Image = models.ImageField(blank=True,null=True,upload_to='TestimonialImage')

    def __str__(self):
        return self.Tes_Name

    # image resize function
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Tes_Image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.Tes_Image.path)
    #     elif img.height < 300 or img.width < 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.Tes_Image.path)

########################################################################

class Banners(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Caption = models.CharField(max_length=100)
    Sub_Caption = models.CharField(max_length=100)
    Button_Label = models.CharField(max_length=30)
    Link = models.CharField(max_length=1000)
    Banner_Image = models.ImageField(blank=True,null=True,upload_to='BannerImage')

    def __str__(self):
        return self.Caption

    # image resize functions
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = IMG.open(self.Banner_Image.path)

    #     if img.height > 1500 or img.width > 1500:
    #         output_size = (1500,1500)
    #         img.thumbnail(output_size)
    #         img.save(self.Banner_Image.path)
    #     elif img.height < 1500 or img.width < 1500:
    #         output_size = (1500,1500)
    #         img.thumbnail(output_size)
    #         img.save(self.Banner_Image.path)

########################################################################

class Theme(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(null=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    # additional
    Primary = models.CharField(max_length=10,null=True,blank=True)
    Secondary = models.CharField(max_length=10,null=True,blank=True)