import graphene

import qzzzme_app.graphql.schema
import qzzzme_app.graphql.mutations


class Query(qzzzme_app.graphql.schema.Query, graphene.ObjectType):
    pass


class Mutation(qzzzme_app.graphql.mutations.Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
