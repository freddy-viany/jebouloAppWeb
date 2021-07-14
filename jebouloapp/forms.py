from django import forms

from jebouloapp.models import AnnounceModel
from django.utils.translation import gettext as _


class AnnounceForm(forms.ModelForm):
    class Meta:
        model = AnnounceModel  
        # fields = '__all__'        si l'on veut afficher tous les champs du model
        fields = ['user_category','civility','category', 'city', 'region','available_time_work','disponibility_periode_work','competence','picture_announce', 'first_name', 'last_name', 'email', 'mobile_phone']

        
       
        CATEGORY_USER = (
       ('', 'Select a title'),
       ('Independant-e', _('Independant-e') ),
       ('Entreprise', _('Entreprise')),)
        

        REGION_CHOICES = (
       ('', _('All regions') ),
       ('Littoral', _('Littoral') ),
       ('Centre', _('Center')),
       ('Ouest', _('West')),
       ('Nord', _('North')),
       ('Sud-Ouest', _('South-West')),
       ('Sud', _('South')),
       ('Est', _('East')),
       ('Nord-Ouest', _('North-west')),
       ('Extreme-Nord', _('Far-North')),
       ('Adamaoua', _('Adamaoua')),)


        CATEGORY_CHOICES=(
       ('', _('All categories') ),
       ('IT & Computer', _('IT & Computer') ),
       ('Banque, Comptabilite, Finance', _('Banking, Accounting, Finance')),
       ('community manager, Marketing', _('community manager, Marketing')),
       ('Arts, Design, Media', _('Arts, Design, Media')),
       ('Ingenierie', 'Ingenierie'),
       ('Agriculture, Elevage & Agro-industrie', _('Agriculture, Animal Production & Agro-industry')),
       ('Menagere, Nounou', _('house cleaner lady, Nounou')),
       ('BTP, Plomberie, Menuserie', _('Building and Public Works, Plumbing, Menustry')),
       ('Sante', _('Health')),
       ('Coiffure, Esthétique & Mode', _('Hairdressing, Beauty & Fashion')),
       ('Immobilier', _('real estate')),
       ('Restauration & Cuisine', _('Restoration & Cooking')),
       ('Education & Formation', _('Education & Learning')),
       ('Cabinet conseil', _('Consulting firm')),
       ('Chauffeur', _('Driver')),
       ('Vigile - Gardien', _('Security guard - Guardian')),
       ('Transport & Logistique', _('Transport & Logistics')),
       ('Journaliste, Redacteur Web', _('Journalist, Web Editor')),
       ('Traduction, Interprete', _('Translation, Interpreting')),
       ('Coaching', _('Coaching')),
       ('Secretariat', _('Secretariat')),
       ('Autres', _('Others')),)

        CIVILITY_CHOICES = (
                ('', _('Select a title')),
                ('M', _('M')), #First one is the value of select option and second is the displayed value in option
                ("Mme", _("Mme")),
                ("Pasteur", _("Pastor")),
                ("Dr", _("Dr")), 
                ("Pr", _("Pr")), 
                ("Ing", _("Ing")), 
                ("Me", _("Me")), 
                )

        AVAILABLE_TIME = (
                ('', _('Indicate your availability per day')),
                ('24h/24', '24h/24'), #First one is the value of select option and second is the displayed value in option
                ("12h/24", "12h/24"),
                ("8h/24", "8h/24"), 
                ("6h/24", "6h/24"),
                ("5h/24", "5h/24"),
                ("4h/24", "4h/24"),
                ("3h/24", "3h/24"),
                ("2h/24", "2h/24"),
                )

        DISPONIBILITY_CHOICES = (
                ('', _('Indicate your working days')),
                ('lundi-dimanche', _('Monday-Sunday')), #First one is the value of select option and second is the displayed value in option
                ("lundi-vendredi", _("Monday-Friday")),
                ("le week-end", _("the weekend")), 
                ("Autres", _("Others")),
                )

        widgets = {
            'user_category': forms.Select(choices=CATEGORY_USER, attrs={'class': 'form-control'}),
            'civility': forms.Select(choices=CIVILITY_CHOICES, attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            'region': forms.Select(choices=REGION_CHOICES, attrs={'class':'form-control'}),
            'available_time_work': forms.Select(choices=AVAILABLE_TIME, attrs={'class': 'form-control'}),
            'disponibility_periode_work': forms.Select(choices=DISPONIBILITY_CHOICES, attrs={'class': 'form-control'}),
            
        }

       
        


####################################
#formulaire pour seach des competences
####################################
class FilterForm(forms.Form):
    
    REGION_CHOICES = (
       ('', _('Toutes les regions') ),
       ('Littoral', _('Littoral') ),
       ('Centre', _('Centre')),
       ('Ouest', _('Ouest')),
       ('Nord', _('Nord')),
       ('Sud-Ouest', _('Sud-Ouest')),
       ('Sud', _('Sud')),
       ('Est', _('Est')),
       ('Nord-Ouest', _('Nord-Ouest')),
       ('Extreme-Nord', _('Extreme-Nord')),
       ('Adamaoua', _('Adamaoua')),)

    CATEGORY_CHOICES=(
       ('', _('Toutes les categories') ),
       ('IT & Computer', _('IT & Computer') ),
       ('Banque, Comptabilite, Finance', _('Banque, Comptabilite, Finance')),
       ('community manager, Marketing', _('community manager, Marketing')),
       ('Arts, Design, Media', _('Arts, Design, Media')),
       ('Ingenierie', 'Ingenierie'),
       ('Agriculture, Elevage & Agro-industrie', _('Agriculture, Elevage & Agro-industrie')),
       ('Menagere, Nounou', _('Menagere, Nounou')),
       ('BTP, Plomberie, Menuserie', _('BTP, Plomberie, Menuserie')),
       ('Sante', _('Sante')),
       ('Coiffure, Esthétique & Mode', _('Coiffure, Esthétique & Mode')),
       ('Immobilier', _('Immobilier')),
       ('Restauration & Cuisine', _('Restauration & Cuisine')),
       ('Education & Formation', _('Education & Formation')),
       ('Cabinet conseil', _('Cabinet conseil')),
       ('Chauffeur', _('Chauffeur')),
       ('Vigile - Gardien', _('Vigile - Gardien')),
       ('Transport & Logistique', _('Transport & Logistique')),
       ('Journaliste, Redacteur Web', _('Journaliste, Redacteur Web')),
       ('Traduction, Interprete', _('Traduction, Interprete')),
       ('Coaching', _('Coaching')),
       ('Secretariat', _('Secretariat')),
       ('Autres', _('Autres')),)
        

    search= forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Entrer les mots cles'}), label=_('Search'))
    region = forms.ChoiceField(choices = REGION_CHOICES, required=False, label=_('region'))
    category =forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label=_('Categorie'))


class Testform(forms.ModelForm):
    class Meta:
        model = AnnounceModel  
        # fields = '__all__'        si l'on veut afficher tous les champs du model
        fields = ['first_name']
