import os
from supabase import create_client, Client
from dotenv import load_dotenv


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url=url, supabase_key=key)

load_dotenv()
def signUpUser( request):
    first_name = request.get('first_name')
    last_name = request.get('last_name')
    email = request.get('email')
    password = request.get('password')
    age = request.get('age')
    try:
     supabase.auth.sign_up({'email':email, 'password':password})
    except Exception as e: 
     return e