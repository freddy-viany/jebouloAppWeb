from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import  CustomerModel,AnnounceModel
from .forms import AnnounceForm, FilterForm
from django.db import  models
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q , F, Case, When, Value, IntegerField
#API paiement
from  payDex import payDex
import random

# Create your views here.


###paiement section
#Api paiement --payunit
payment = payDex({
	"apiUsername": 'payunit_sand_MEBLfTkpu',
	"apiPassword": '9babe1c0-08b4-474b-b2b9-816cdb78cd52',
	"api_key": 'a5187e43ea45627e4a6a51953b057f828f2a0b37',
	"return_url": "http://127.0.0.1:8000/paiementSucces",
	"notify_url": "",
	"mode": "test",
	"name": "",
	"description": "",
	"purchaseRef": "",
	"currency": "XAF",
	"transaction_id":  "123456786",
})


#variable globale pour transaction
#global b
b=1 # b begin with 1 and should be increase after each transaction 
def paiementpremiumview(request):
	global b
	if request.user.is_authenticated:
		random_number=random.randint(0,10)
		fone_number= CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
		id_user = CustomerModel.objects.filter(userid = request.user.id)[0].userid
		#transaction_ID = str(fone_number)+"U"+str(id_user)+ "a" +str(b)+ "pre" + str(random_number)
		transaction_ID = str(fone_number)+"U"+str(id_user)+ "a" +str(b)+ "pre"
		b= b+1
	
	

	payment1 = payDex({
	"apiUsername": 'payunit_sand_MEBLfTkpu',
	"apiPassword": '9babe1c0-08b4-474b-b2b9-816cdb78cd52',
	"api_key": 'a5187e43ea45627e4a6a51953b057f828f2a0b37',
	"return_url": "http://127.0.0.1:8000/paiementProcces",
	"notify_url": "",
	"mode": "test",
	"name": "",
	"description": "premium_paiement",
	"purchaseRef": "",
	"currency": "XAF",
	"transaction_id": transaction_ID,
})
	#amount = request.POST['amount']
	#payment1[transaction_id]="415"
	payment1.makePayment(1500)
	#if amount is not None:
	   #payment.makePayment(500)
	context ={'payment':payment1, 'transaction_ID':transaction_ID}
	return render(request,'jeboulo/thanks.html',context)

def paiementproview(request):
	global b
	if request.user.is_authenticated:
		random_number=random.randint(0,10)
		fone_number= CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
		id_user = CustomerModel.objects.filter(userid = request.user.id)[0].userid
		transaction_ID = str(fone_number)+"U"+str(id_user)+ "a" +str(b)+ "pro"
		#transaction_ID = str(fone_number)+ "a" + str(b) + "pro" + str(random_number)
		b = b +1

	payment2 = payDex({
	"apiUsername": 'payunit_sand_MEBLfTkpu',
	"apiPassword": '9babe1c0-08b4-474b-b2b9-816cdb78cd52',
	"api_key": 'a5187e43ea45627e4a6a51953b057f828f2a0b37',
	"return_url": "http://127.0.0.1:8000/paiementProcces",
	"notify_url": "",
	"mode": "test",
	"name": "",
	"description": "pro_paiement",
	"purchaseRef": "",
	"currency": "XAF",
	"transaction_id": transaction_ID,
})
	#amount = request.POST['amount']
	#payment1[transaction_id]="415"
	payment2.makePayment(5000)
	#if amount is not None:
	   #payment.makePayment(500)
	context ={'payment':payment2, 'transaction_ID':transaction_ID}
	return render(request,'jeboulo/thanks.html',context)


def paiementvipview(request):
	global b
	if request.user.is_authenticated:
		random_number=random.randint(0,10)
		fone_number= CustomerModel.objects.filter(userid = request.user.id)[0].phoneno
		id_user = CustomerModel.objects.filter(userid = request.user.id)[0].userid
		transaction_ID = str(fone_number)+"U"+str(id_user)+ "a" +str(b)+ "vip"
		#transaction_ID = str(fone_number)+ "a" + str(b) + "vip" + str(random_number)
		b = b +1

	payment3 = payDex({
	"apiUsername": 'payunit_sand_MEBLfTkpu',
	"apiPassword": '9babe1c0-08b4-474b-b2b9-816cdb78cd52',
	"api_key": 'a5187e43ea45627e4a6a51953b057f828f2a0b37',
	"return_url": "http://127.0.0.1:8000/paiementProcces",
	"notify_url": "",
	"mode": "test",
	"name": "",
	"description": "vip_paiement",
	"purchaseRef": "",
	"currency": "XAF",
	"transaction_id": transaction_ID,
})
	#amount = request.POST['amount']
	#payment1[transaction_id]="415"
	payment3.makePayment(10000)
	#if amount is not None:
	   #payment.makePayment(500)
	context ={'payment':payment3, 'transaction_ID':transaction_ID}
	return render(request,'jeboulo/thanks.html',context)


def paiementProcessview(request):
	return render(request,'jeboulo/paiementProcces.html')
###end paiement section


def helloword(request):
	name="fred"
	context = {'name' : name}
	return render(request,"Helloword/helloword.html", context)


def homepageview(request):
	# on recupere le user pour compter les competences deja inscrites
	user = AnnounceModel.objects.all()
	return render (request, "jeboulo/homepage.html", {'user':user})

def gohomepageview(request):
	return redirect ('homepage')

def donatepageview(request):
	return render(request, "jeboulo/donate.html")

def donateview(request):
	global b
	random_number=random.randint(0,10)
	transaction_ID ="donate" +str(b)
	#transaction_ID = str(fone_number)+ "a" + str(b) + "vip" + str(random_number)
	b = b +1

	amount= request.POST['amount']

	
	paymentdonate = payDex({
	"apiUsername": 'payunit_sand_MEBLfTkpu',
	"apiPassword": '9babe1c0-08b4-474b-b2b9-816cdb78cd52',
	"api_key": 'a5187e43ea45627e4a6a51953b057f828f2a0b37',
	"return_url": "http://127.0.0.1:8000/paiementProcces",
	"notify_url": "",
	"mode": "test",
	"name": "",
	"description": "vip_paiement",
	"purchaseRef": "",
	"currency": "XAF",
	"transaction_id": transaction_ID,
})


	paymentdonate.makePayment(int(amount))
	#if amount is not None:
	   #payment.makePayment(500)
	context ={'payment':paymentdonate, 'transaction_ID':transaction_ID}
	return render(request,'jeboulo/thanksdonate.html',context)

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']
	phoneno = request.POST['phoneno']

	#if username alredy exists
	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR, message=_('User already exists'))
		return render (request, "jeboulo/usersignuppage.html")
		#return redirect('signupuserpage')
	
	#if the phone number is already using for another account
	if CustomerModel.objects.filter(phoneno__iexact=phoneno).exists():
		messages.add_message(request,messages.ERROR, message=_('This number already belongs to another account'))
		return render (request, "jeboulo/usersignuppage.html")
	
	#if username doesn't already exists
	User.objects.create_user(username = username, password=password).save()
	lastobject = len(User.objects.all())-1
	CustomerModel(userid= User.objects.all()[int(lastobject)].id, phoneno=phoneno).save()
	messages.add_message(request,messages.SUCCESS, message=_('User succesfully created ---Please login.'))
	return redirect('customerpage')
		
def modifieprofilview(request):
	return render (request, "jeboulo/modifieprofilpage.html")
	
def modifiepasswordview(request):
	new_password = request.POST['password']

	if not request.user.is_authenticated:
		return redirect('userloginpage')


	username = request.user.username
	usr = User.objects.get(username=username)
	usr.set_password(new_password)
	usr.save()
	return render (request, "jeboulo/userloginpage.html")	


def userloginview(request):
	return render(request, "jeboulo/userloginpage.html")

def usersignupview(request):
	return render(request, "jeboulo/usersignuppage.html")

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	#user exits
	#if user is not None and user.username=="admin":
	if user is not None:
		login(request, user)
		return redirect('customerpage')

	#user doesn't exists
	if user is None:
		messages.add_message(request,messages.ERROR, "invalid credentials --- identifiant ou mot de passe invalide")
		#return render (request, "jeboulo/userloginpage.html")
		return redirect('userloginpage')


def customerwelcomeview(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	customermod = CustomerModel.objects.filter(userid = request.user.id)[0]
	#context = {'username': username,'pizzas':PizzaModel.objects.all()}

	context = {'username': username, 'customermod':customermod}
	return render(request,'jeboulo/customerpage.html',context)


def customerwelcomeview_Zeroannounce(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	username = request.user.username
	customermod = CustomerModel.objects.filter(userid = request.user.id)[0]
	#context = {'username': username,'pizzas':PizzaModel.objects.all()}

	context = {'username': username, 'customermod':customermod}
	return render(request,'jeboulo/customerpage-zeroannounce.html',context)

def userlogout(request):
	logout(request)
	return redirect('homepage')



#add announce
def addannounce(request):
	# Construire le formulaire, soit avec les données postées,
	# soit vide si l'utilisateur accède pour la première fois
	# à la page.
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	form= AnnounceForm()
	return render(request, 'jeboulo/registerannounce.html', {'form':form})
		
#publish announce
def pubannounce(request):
	if not request.user.is_authenticated:
		return redirect('userloginpage')

	if len(request.POST)>0:
		form=AnnounceForm(request.POST or None, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.customermodel =CustomerModel.objects.filter(userid = request.user.id)[0]
			post.type_announce = post.customermodel.type_account
			post.save()

			#ici on recupere l'object en instance. Il servira a afficher les informations utiles dans le templates
			username = request.user.username
			customermod = CustomerModel.objects.filter(userid = request.user.id)[0]
			context = {'username': username, 'customermod':customermod}

			#Reporter.objects.all().update(stories_filed=F('stories_filed') + 1)
			if post.customermodel.number_of_publication_announce > 0:
				#on decremente le nombre de publication
				post.customermodel.number_of_publication_announce = F('number_of_publication_announce') - 1
				post.customermodel.save()
				post.customermodel.refresh_from_db()
				#si le nombre de publication est null on met le type de compte a standard.
				if post.customermodel.number_of_publication_announce==0:
					post.customermodel.type_account ='standard'
					post.customermodel.save()
					post.customermodel.refresh_from_db()
					return render(request,'jeboulo/customerpage.html',context)

				#ici le nombre de publication est non null
				#post.customermodel.save()
				#post.customermodel.refresh_from_db()
				return render(request,'jeboulo/customerpage.html',context)
	
			return render(request,'jeboulo/customerpage.html',context)
		else:
			form= AnnounceForm()
			return render(request, 'jeboulo/registerannounce.html', {'form':form})

#########################
##search views
#########################

class SearchView(ListView):
	model = CustomerModel
	#paginate_by = 100
	template_name = 'jeboulo/searchannounce.html'


	def get_queryset(self):
		query = self.request.GET.get('search')
		region = self.request.GET.get('region')
		# Do your filter and search here
		object_list = CustomerModel.objects.all()
		return object_list

		#return User_competence_entries.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['form'] = FilterForm(initial={
			'search': self.request.GET.get('search', ''),
			'region': self.request.GET.get('region', ''),
		})

		return context
		#return render( request, "exyohri/rechercheCompetence.html", context)


#################################
################################

class ResultView(ListView):
	model = AnnounceModel
	context_object_name = 'users'
	paginate_by = 9
	template_name = 'jeboulo/resultannounce.html'


	def get_queryset(self):
		queryset = super().get_queryset()
		search = self.request.GET.get('search')
		category = self.request.GET.get('category')
		region = self.request.GET.get('region')
		#object_list = User_competence_entries.objects.all()
		object_list = AnnounceModel.objects.all()

		# Do your filter and search here
		#si la recherche 'search' est bien selectionnee
		if search:
			#pour affciher les user on pourra utiliser:
			# "thecompetences" est la cle etranger dans le model annonce.
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			#
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			object_list = AnnounceModel.objects.filter(category__icontains=search)
			if len(object_list)>0:
				return object_list

		#recherche suivant 'region' et la categorie Entry.objects.extra(where=['type_announce=%s'],params=['premium']), extra(where=["type_announce='premium'"])
		#Blog.objects.extra(select={'a': '%s', 'b': '%s'},select_params=('one', 'two'),)
		if category and region:
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			#object_list = TheCompetence.objects.filter(category__iexact=category,region__iexact=region).annotate()

			########
			#######NOTE: The syntax for the CASE WHEN/THEN is database-specific.
			# #CASE_SQL = '(case when type_announce="vip" then 1 when type_announce="pro" then 2 when type_announce="premium" then 3 when type_announce="standard" then 4 end)'
			#The syntax above is for SQLite. For PostgreSQL, omit the parentheses 
			#and use escaped single quotes instead of double quotes.
			#####
			
			CASE_SQL = 'case when type_announce=\'vip\' then 1 when type_announce=\'pro\' then 2 when type_announce=\'premium\' then 3 when type_announce=\'standard\' then 4 end'
			#post_date__date=date.today()
			#today = date.today()
			#object_list = AnnounceModel.objects.filter(category__iexact=category,region__iexact=region).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order'])
			object_list = AnnounceModel.objects.filter(category__iexact=category,region__iexact=region).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order','-publication_date'])

			if len(object_list)>0:
				return object_list

		#recherche suivant la categorie
		if category:
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			CASE_SQL = 'case when type_announce=\'vip\' then 1 when type_announce=\'pro\' then 2 when type_announce=\'premium\' then 3 when type_announce=\'standard\' then 4 end'
			#object_list = AnnounceModel.objects.filter(category__iexact=category).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order']).order_by('-publication_date')
			object_list = AnnounceModel.objects.filter(category__iexact=category).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order','-publication_date'])
			if len(object_list)>0:
				return object_list

		#recherche suivant la region
		if region:
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			CASE_SQL = 'case when type_announce=\'vip\' then 1 when type_announce=\'pro\' then 2 when type_announce=\'premium\' then 3 when type_announce=\'standard\' then 4 end'
			#object_list = AnnounceModel.objects.filter(region__iexact=region).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order']).order_by('-publication_date')
			object_list = AnnounceModel.objects.filter(region__iexact=region).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order','-publication_date'])
			if len(object_list)>0:
				return object_list


		#recherche suivant 'search' et la categorie
		if category and search:
			#object_list = TheUser.objects.filter(thecompetences__competence__icontains=search, thecompetences__category=category, thecompetences__region=region )
			CASE_SQL = 'case when type_announce=\'vip\' then 1 when type_announce=\'pro\' then 2 when type_announce=\'premium\' then 3 when type_announce=\'standard\' then 4 end'
			object_list = AnnounceModel.objects.filter(category__iexact=category).extra(select={'publication_order': CASE_SQL}, order_by=['publication_order', '-publication_date'])
			if len(object_list)>0:
				return object_list



		####
		CASE_SQL = 'case when type_announce=\'vip\' then 1 when type_announce=\'pro\' then 2 when type_announce=\'premium\' then 3 when type_announce=\'standard\' then 4 end'
		#today = date.today()
		
		#return qs2
		object_list = AnnounceModel.objects.all().extra(select={'publication_order':CASE_SQL}, order_by=['publication_order', '-publication_date'])
		return object_list
		#return CustomerModel.objects.all().extra(select={'publication_order': CASE_SQL}, order_by=['publication_order'])
			

	def get_context_data(self, *args, **kwargs):
		context = super(ResultView, self).get_context_data(*args, **kwargs)
		context['form'] = FilterForm(initial={
			'search': self.request.GET.get('search', ''),
			'category': self.request.GET.get('category', ''),
			'region': self.request.GET.get('region', ''),
		})

		return context
		#return render( request, "exyohri/rechercheCompetence.html", context)


#details for announce
class DetailsUserView(DetailView):

	model = AnnounceModel
	template_name = 'jeboulo/userDetails.html'
	context_object_name = 'use'
	
	
	
	def get_context_data(self, **kwargs):
		context = super(DetailsUserView, self).get_context_data(**kwargs)
		# add extra field  
		#context["note"] = ""
		return context