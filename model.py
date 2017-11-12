from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import (scoped_session, sessionmaker)
# from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

pwd = 'oQAyxuipqSafMFW5qQKWcFVh5umC5si3'

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine(
    "mysql+pymysql://root@localhost/mtc?password=" + pwd
)

# reflect the tables
Base.prepare(engine, reflect=True)

# get classes for each table
Documento = Base.classes.documento
Zona = Base.classes.zona
MapaContribs = Base.classes.mapacontribs
TipoRegisto = Base.classes.tiporegisto
LivroContas = Base.classes.livrocontas
ContribGrupo = Base.classes.contribgrupo
Grupo = Base.classes.grupo
Publicacao = Base.classes.publicacao
Assinatura = Base.classes.assinatura
Contribuicao = Base.classes.contribuicao
Balanco = Base.classes.balanco
DonativoPublicacao = Base.classes.donativopublicacao
Registo = Base.classes.registo
LivroRegisto = Base.classes.livroregisto
Proveniencia = Base.classes.proveniencia
TipoContribuicao = Base.classes.tipocontribuicao
Rubrica = Base.classes.rubrica
TipoEntrada = Base.classes.tipoentrada
Pessoa = Base.classes.pessoa
Entrada = Base.classes.entrada
TipoRubrica = Base.classes.tiporubrica

# session = Session(engine)
session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))
