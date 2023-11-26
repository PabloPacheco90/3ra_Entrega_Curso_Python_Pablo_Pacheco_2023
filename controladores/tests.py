from django.test import TestCase
from .models import Departamento

class DepartamentoTest(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            nombre='Departamento de Pruebas',
            modalidad_trabajo='Tiempo completo',
            sueldo_promedio=5000.00
        )

    def test_valor_esperado(self):
        resultado_esperado = 100  
        resultado_real = self.departamento.sueldo_promedio()  
        self.assertEqual(resultado_real, resultado_esperado)

    def test_nombre_str(self):
        # Verificar el método __str__ del modelo
        departamento = Departamento.objects.get(nombre='Departamento de Pruebas')
        self.assertEqual(str(departamento), departamento.nombre)