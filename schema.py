import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from model import \
            Documento as DocumentoModel, \
            Zona as ZonaModel, \
            MapaContribs as MapaContribsModel, \
            TipoRegisto as TipoRegistoModel, \
            LivroContas as LivroContasModel, \
            ContribGrupo as ContribGrupoModel, \
            Grupo as GrupoModel, \
            Publicacao as PublicacaoModel, \
            Assinatura as AssinaturaModel, \
            Contribuicao as ContribuicaoModel, \
            Balanco as BalancoModel, \
            DonativoPublicacao as DonativoPublicacaoModel, \
            Registo as RegistoModel, \
            LivroRegisto as LivroRegistoModel, \
            Proveniencia as ProvenienciaModel, \
            TipoContribuicao as TipoContribuicaoModel, \
            Rubrica as RubricaModel, \
            TipoEntrada as TipoEntradaModel, \
            Pessoa as PessoaModel, \
            Entrada as EntradaModel, \
            TipoRubrica as TipoRubricaModel


# Documento = Base.classes.documento
class Documento(SQLAlchemyObjectType):
    class Meta:
        model = DocumentoModel
        interfaces = (relay.Node, )


# Zona = Base.classes.zona
class Zona(SQLAlchemyObjectType):
    class Meta:
        model = ZonaModel
        interfaces = (relay.Node, )


# MapaContribs = Base.classes.mapacontribs
class MapaContribs(SQLAlchemyObjectType):
    class Meta:
        model = MapaContribsModel
        interfaces = (relay.Node, )


# TipoRegisto = Base.classes.tiporegisto
class TipoRegisto(SQLAlchemyObjectType):
    class Meta:
        model = TipoRegistoModel
        interfaces = (relay.Node, )


# LivroContas = Base.classes.livrocontas
class LivroContas(SQLAlchemyObjectType):
    class Meta:
        model = LivroContasModel
        interfaces = (relay.Node, )


# ContribGrupo = Base.classes.contribgrupo
class ContribGrupo(SQLAlchemyObjectType):
    class Meta:
        model = ContribGrupoModel
        interfaces = (relay.Node, )


# Grupo = Base.classes.grupo
class Grupo(SQLAlchemyObjectType):
    class Meta:
        model = GrupoModel
        interfaces = (relay.Node, )


# Publicacao = Base.classes.publicacao
class Publicacao(SQLAlchemyObjectType):
    class Meta:
        model = PublicacaoModel
        interfaces = (relay.Node, )


# Assinatura = Base.classes.assinatura
class Assinatura(SQLAlchemyObjectType):
    class Meta:
        model = AssinaturaModel
        interfaces = (relay.Node, )


# Contribuicao = Base.classes.contribuicao
class Contribuicao(SQLAlchemyObjectType):
    class Meta:
        model = ContribuicaoModel
        interfaces = (relay.Node, )


# Balanco = Base.classes.balanco
class Balanco(SQLAlchemyObjectType):
    class Meta:
        model = BalancoModel
        interfaces = (relay.Node, )


# DonativoPublicacao = Base.classes.donativopublicacao
class DonativoPublicacao(SQLAlchemyObjectType):
    class Meta:
        model = DonativoPublicacaoModel
        interfaces = (relay.Node, )


# Registo = Base.classes.registo
class Registo(SQLAlchemyObjectType):
    class Meta:
        model = RegistoModel
        interfaces = (relay.Node, )


# LivroRegisto = Base.classes.livroregisto
class LivroRegisto(SQLAlchemyObjectType):
    class Meta:
        model = LivroRegistoModel
        interfaces = (relay.Node, )


# Proveniencia = Base.classes.proveniencia
class Proveniencia(SQLAlchemyObjectType):
    class Meta:
        model = ProvenienciaModel
        interfaces = (relay.Node, )


# TipoContribuicao = Base.classes.tipocontribuicao
class TipoContribuicao(SQLAlchemyObjectType):
    class Meta:
        model = TipoContribuicaoModel
        interfaces = (relay.Node, )


# Rubrica = Base.classes.rubrica
class Rubrica(SQLAlchemyObjectType):
    class Meta:
        model = RubricaModel
        interfaces = (relay.Node, )


# TipoEntrada = Base.classes.tipoentrada
class TipoEntrada(SQLAlchemyObjectType):
    class Meta:
        model = TipoEntradaModel
        interfaces = (relay.Node, )


# Pessoa = Base.classes.pessoa
class Pessoa(SQLAlchemyObjectType):
    class Meta:
        model = PessoaModel
        interfaces = (relay.Node, )


# Entrada = Base.classes.entrada
class Entrada(SQLAlchemyObjectType):
    class Meta:
        model = EntradaModel
        interfaces = (relay.Node, )


# TipoRubrica = Base.classes.tiporubrica
class TipoRubrica(SQLAlchemyObjectType):
    class Meta:
        model = TipoRubricaModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # all_groups = SQLAlchemyConnectionField(Grupo)
    all_livros_registo = SQLAlchemyConnectionField(LivroRegisto)
    all_rubrica = SQLAlchemyConnectionField(Rubrica)


schema = graphene.Schema(query=Query)
