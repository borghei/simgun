
from django.shortcuts import render, get_object_or_404

from .models import SupportAgent, Ticket
# Create your views here.


def agent_profile(request, agent_id):
    agent = get_object_or_404(SupportAgent, pk=agent_id)
    tickets = Ticket.objects.filter(agent=agent)
    unanswered_tickets = tickets.filter(status=0)
    answered_tickets = tickets.filter(status__in=[1, 2])
    return render(request, 'support/agent-profile.html',
                  {'agent': agent, 'answered': answered_tickets, 'unanswered': unanswered_tickets})
