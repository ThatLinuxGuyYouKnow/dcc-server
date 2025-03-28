import os
from supabase import create_client, Client
from dotenv import load_dotenv


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url=url, supabase_key=key)

load_dotenv()
def signUpUser( request):
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    try:
     supabase.auth.sign_up({'email':email, 'password':password})
     return true
    except Exception as e: 
     return e