import graphene
from graphene_django.types import DjangoObjectType
from .models import Employee, Department
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphql_relay import from_global_id
from graphql_jwt.decorators import login_required


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = {
            "name": ["exact", "icontains"],
            "join_year": ["exact", "icontains"],
            "department__dept_name": ["icontains"]
        }
        interfaces = (relay.Node,)
