from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.template.loader import render_to_string
from .models import transaction
import json
from datetime import datetime

# Create your views here.
def home(request):
    transactions = transaction.objects.all().order_by('-created_at')
    
    # Calculate totals
    total_income = sum(t.amount for t in transactions if t.is_income)
    total_expenses = sum(t.amount for t in transactions if not t.is_income)
    balance = total_income - total_expenses
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
    }
    return render(request, 'index.html', context)

def create_transaction(request):
    if request.method == 'POST':
        try:
            amount = float(request.POST.get('amount'))
            description = request.POST.get('description')
            date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
            category = request.POST.get('category')
            is_income = bool(request.POST.get('is_income'))
            
            # Create new transaction
            transaction.objects.create(
                amount=amount,
                description=description,
                date=date,
                category=category,
                is_income=is_income
            )
            
            return redirect('home')
        except Exception as e:
            # Handle error - you could add error messages here
            return redirect('home')
    return redirect('home')

def update_transaction(request, id):
    if request.method == 'POST':
        try:
            transaction_obj = get_object_or_404(transaction, id=id)
            
            amount = float(request.POST.get('amount'))
            description = request.POST.get('description')
            date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
            category = request.POST.get('category')
            is_income = bool(request.POST.get('is_income'))
            
            # Update transaction fields
            transaction_obj.amount = amount
            transaction_obj.description = description
            transaction_obj.date = date
            transaction_obj.category = category
            transaction_obj.is_income = is_income
            transaction_obj.save()
            
            return redirect('home')
        except Exception as e:
            return redirect('home')
    return redirect('home')

def delete_transaction(request, id):
    if request.method == 'POST':
        try:
            transaction_obj = get_object_or_404(transaction, id=id)
            transaction_obj.delete()
            return redirect('home')
        except Exception as e:
            return redirect('home')
    return redirect('home')

def get_transaction(request, id):
    try:
        transaction_obj = get_object_or_404(transaction, id=id)
        return JsonResponse({
            'success': True,
            'transaction': {
                'id': str(transaction_obj.id),
                'amount': transaction_obj.amount,
                'description': transaction_obj.description,
                'date': transaction_obj.date.strftime('%Y-%m-%d'),
                'category': transaction_obj.category,
                'is_income': transaction_obj.is_income,
                'created_at': transaction_obj.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error fetching transaction: {str(e)}'
        }, status=400)