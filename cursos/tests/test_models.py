from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest

# def test_config():
#     assert 1==1

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'Java',
        data_do_curso = date.today(),
        carga_horaria = '40'
    )
    return curso
   
@pytest.mark.django_db  
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2024-02-28 - 40'
