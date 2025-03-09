from .models import Resume  

def latest_resume(request):
    latest_resume = Resume.objects.order_by("-uploaded_at").first()
    return {"resume": latest_resume}
