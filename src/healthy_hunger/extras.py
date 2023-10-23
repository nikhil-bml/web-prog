from django.contrib.postgres.search import SearchVector
from .models import Product

def full_text_search(factor:list,model:str,search_term:str):
    """
    factor is a list ["username","email"] these are fields to be searched < usage is here, arguments are supposed to be passed like this
    Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    search_term is the string you want to search
    """
    return eval(model).objects.annotate(search=SearchVector(*factor)).filter(search=search_term)
