import os
from google import genai

from datetime import datetime

def get_current_time():
    """Vrátí aktuální datum a čas ve formátu HH:MM:SS."""
    now = datetime.now()
    return now.strftime("%H:%M:%S")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
try:
    
    aktualni_cas = get_current_time()
    
    
 

    dotaz = f"Napiš krátkou, vtipnou zprávu o tom, jak je pozdě/brzo, s ohledem na aktuální čas. Právě je {aktualni_cas}."

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=dotaz
    )



    print(resp.text)

except Exception as e:
    print(f"Došlo k chybě: {e}")




