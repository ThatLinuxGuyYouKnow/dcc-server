import os
from supabase import create_client, Client
from dotenv import load_dotenv


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url=url, supabase_key=key)

load_dotenv()
def signUpUser( request):
    data = request.get_json() #dddd
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    try:
     auth_response =  supabase.auth.sign_up({'email':email, 'password':password})
     data = {
        "user_id": auth_response.user.id,
        "last_name":last_name,
        "first_name": first_name,
        "email":email
     }
     return true,  data
    except Exception as e: 
     return e