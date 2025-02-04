from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(300), unique=True)
    cpf = db.Column(db.String(15), nullable=True, unique=True)
    password = db.Column(db.String(150), nullable=True)
    full_name = db.Column(db.String(200))
    data_nasc = db.Column(db.DateTime(timezone=True), nullable=True)
    data_criacao = db.Column(db.DateTime(timezone=True), default=datetime.now())
    cliente_tina = db.Column(db.Integer, nullable=False)
    assinante   = db.Column(db.Integer, nullable=True, default=0)
    google_linked = db.Column(db.Integer, nullable=False, default=0)
    is_active = db.Column(db.Integer, nullable=False, default=1)
    is_adm = db.Column(db.Integer, nullable=False, default=0)
    email_authenticated = db.Column(db.Integer, default=0)
    email_authentication_code = db.Column(db.String(7), nullable=True)
    
    def set_password(self, password: str):
        self.password = generate_password_hash(password)
    
    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)

class CursosEmProgresso(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), primary_key=True)
    progresso = db.Column(db.Integer)
    data_final = db.Column(db.DateTime(timezone=True))

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), unique=True)
    descricao = db.Column(db.Text)
    nAulas = db.Column(db.Integer)
    image_URL = db.Column(db.String(150))

class Questionario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    q1 = db.Column(db.Integer, db.ForeignKey("questao.id"))
    q2 = db.Column(db.Integer, db.ForeignKey("questao.id"))
    q3 = db.Column(db.Integer, db.ForeignKey("questao.id"))
    q4 = db.Column(db.Integer, db.ForeignKey("questao.id"))
    q5 = db.Column(db.Integer, db.ForeignKey("questao.id"))
    pontos_min = db.Column(db.Integer)
    pontos_max = db.Column(db.Integer)
    minutos_max = db.Column(db.Integer)

class Ementa(db.Model):
    aula_id = db.Column(db.Integer, db.ForeignKey("aula.id"), primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"), primary_key=True)


class Aula(db.Model):
    curso_id = db.Column(db.Integer, db.ForeignKey("curso.id"))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(150))
    titulo = db.Column(db.String(150))
    descricao = db.Column(db.Text)

class AcervoDeQuestoes(db.Model):
    questionario_id = db.Column(db.Integer, db.ForeignKey("aula.id"), primary_key=True)
    questao_id = db.Column(db.Integer, db.ForeignKey("curso.id"), primary_key=True)
    valor_pontos_questao = db.Column(db.Integer)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_curso = db.Column(db.Integer, db.ForeignKey("curso.id"))
    enunciado = db.Column(db.Text)
    alternativa_A = db.Column(db.Text)
    alternativa_B = db.Column(db.Text)
    alternativa_C = db.Column(db.Text)
    alternativa_D = db.Column(db.Text)
    alternativa_E = db.Column(db.Text)
    resposta_correta = db.Column(db.String(1))

class RespostaAoQuestionario(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    questionario_id = db.Column(db.Integer, db.ForeignKey("questionario.id"), primary_key=True)
    pontuacao = db.Column(db.Integer)
    data_realizacao = db.Column(db.DateTime(timezone=True))

class Assinaturas(db.Model):
    assinatura_id   = db.Column(db.Integer, primary_key=True, autoincrement="ignore_fk")
    user_id         = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    inicio          = db.Column(db.Date)
    fim             = db.Column(db.Date)
    TipoAssinatura  = db.Column(db.Integer, nullable = True)
