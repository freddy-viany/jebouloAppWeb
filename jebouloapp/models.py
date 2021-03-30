from django.db import models

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from cloudinary.models import CloudinaryField

# Create your models here.

class CustomerModel(models.Model):
	#type de compte
	TYPE_ACCOUNT_CHOICES = (
       ('standard', 'standard' ),
       ('premium', 'premium',),
	   ('pro', 'pro' ),
	   ('vip', 'vip' ),)

	TYPE_ACCOUNT_CHOICES_CERTIFIE = (
       ('certified', 'certified' ),
       ('non-certified', 'non-certified',),)

	userid = models.CharField(max_length=10)
	phoneno = models.CharField(max_length=20)

	#information supplementaires
	last_name = models.CharField(verbose_name =_("name"), max_length=30, help_text=_('Enter your name'),null=True)
	email = models.EmailField(verbose_name =_("Email"), max_length=50, help_text=_('Enter your email'),null=True)

	date_creation_account = models.DateTimeField(auto_now_add=True)
	current_date = models.DateTimeField(auto_now_add=True)
	state_acount = models.CharField(verbose_name=_("state account"), max_length = 75, default='actif')
	validty_acount = models.CharField(verbose_name=_("validity account"), max_length = 75,default='valid')
	num_CNI = models.IntegerField(verbose_name=_("number CNI"), null=True)
	type_account = models.CharField(max_length = 25,choices=TYPE_ACCOUNT_CHOICES, default='standard')
	type_account_certifie = models.CharField(max_length = 25,choices=TYPE_ACCOUNT_CHOICES_CERTIFIE, default='non-certified')
	number_of_publication_announce = models.IntegerField(verbose_name=_("number publication"), default=1)

	 #to have a specific url for one user
	def get_absolute_url(self):
		return reverse('detailsUser', args=[str(self.id)])

	def __str__(self):
		return "%s %s" % (self.userid, self.type_account)

	class Meta:
		ordering = ['type_account']


class AnnounceModel(models.Model):

	#type de compte certifie ou non
	TYPE_ANNOUNCE_CHOICES = (
       ('standard', 'standard' ),
       ('premium', 'premium',),
	   ('pro', 'pro' ),
	   ('vip', 'vip' ),)

	user_category = models.CharField(verbose_name =_("category user"), max_length = 15)
	civility = models.CharField(verbose_name =_("Civility"), max_length = 15)
	category = models.CharField(verbose_name =_("Category"), max_length = 75)
	city = models.CharField(verbose_name =_("City"), max_length = 25, help_text='Douala, yaounde,...')
	region = models.CharField(verbose_name =_("Region"), max_length = 40, help_text=_("Entrer the region"))
	available_time_work = models.CharField(verbose_name =_("Time of work"), max_length = 15)
	disponibility_periode_work = models.CharField(verbose_name =_("Period of work"), max_length = 25)
	competence = models.TextField(verbose_name =_("Describe your competences"), max_length = 100, help_text=_("Describe your expertise"), default='je suis capable de:')
	#picture_announce = models.ImageField(verbose_name =_("Picture announce"), upload_to='imgProfil/%Y/%m/%d',blank=True,null=True, help_text=_("Enter your profile picture (Optional)") )
	picture_announce = CloudinaryField(verbose_name =_("image"),blank=True,null=True, help_text=_("Enter your profile picture (Optional)"))
	
	first_name = models.CharField(verbose_name =_("First name"), max_length=30, help_text=_('Enter your First name'))
	last_name = models.CharField(verbose_name =_("name"), max_length=30, help_text=_('Enter your name'))
	email = models.EmailField(verbose_name =_("Email"), max_length=50, help_text=_('Enter your email'))
	phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(237)"))
	mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Phone"), max_length=27)

    #information supplementaires
	number_of_vote = models.IntegerField(default=0)
	note = models.IntegerField(default=0)
	publication_date = models.DateTimeField(verbose_name=_("publication date"), auto_now_add=True)
	type_announce = models.CharField(max_length = 25,choices=TYPE_ANNOUNCE_CHOICES, default='standard')

	customermodel = models.ForeignKey(CustomerModel, related_name='usermodel', on_delete=models.CASCADE)

	def __str__(self):
		return self.type_announce

	class Meta:
		ordering = ['-publication_date']
