import platform
from django.shortcuts import render

def laptop_details(request):
    details = {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
    }
    return render(request, 'config/laptop_details.html', {'details': details})
