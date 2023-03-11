import pytest

class TestExample():
    
    @classmethod
    def setup_class(cls):
        print(">>> setup_class se ejecuta antes de todas las pruebas")
     
    @classmethod
    def teardown_class(cls):
        print(">>> teardown_class se ejecuta despues de todas las pruebas")
    
    def setup_method(self):
        self.numero_uno = 10
        self.numero_dos = 20
        
    def teardown_method(self):
        pass

    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 30, 'Lo sentimos, la suma no es correcta'
    
    def test_resta_dos_numeros(self):
        assert self.numero_uno - self.numero_dos == -10, 'Lo sentimos, la resta no es correcta'
        

class TestExample2():
    
    def test_multiplicacion_dos_numeros(self):
        assert 10 * 10 == 100, 'Lo sentimos, la multiplicación no es correcta'
        