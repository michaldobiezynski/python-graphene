import graphene
import json

class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info): 
        return "world"

    def resolve_is_admin(self, info):
        return True

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        is_admin
    }    
    '''
)

# print(result.data.items())
# print(result.data['hello'])

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
