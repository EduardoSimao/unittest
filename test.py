import unittest
from app import meu_web_app


class TestSimao(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/simao')
        #o método setUP é executado ao iniciar cada teste! Auxilia no reaproveitamento do codigo,
        #uma vez que muitas dos métodos utilizado no teste utilizam os mesmos comando.
        #para isso, utilizamos o self para acessar os objetos do método 

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
        #verificar se é retornado o código 200(sucesso), ao fazer a requisição HTTP para a URL
       
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
        #verisica se a resposta obtida é um HTML

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Eduardo Simão</title>', str(response_str))
        self.assertIn('<h1>Eduardo Simão</h1>', str(response_str))
        self.assertIn('<p>Universitario, ', str(response_str))
        
    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)
        #verifica se o bootstrap esta funcionando

    
    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)
        #verifica se há imagem

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="http://intagram.com/1niverse"', response_str)
        self.assertIn('>Me siga no Instagram</a>', response_str)
        #verifica se há um link

class TestLopes(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/lopes')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Thais Lopes</title>', str(response_str))
        self.assertIn('<h1>Thais Lopes</h1>', str(response_str))
        self.assertIn('<p>Universitaria', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)
        
    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="https://github.com/Tclsantos09"', response_str)
        self.assertIn('>Me siga no GitHub</a>', response_str)

class TestRodovalho(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/rodovalho')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<title>Victoria Rodovalho</title>', str(response_str))
        self.assertIn('<h1>Victoria Rodovalho</h1>', str(response_str))
        self.assertIn('<p>Universitaria', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_profile_image(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<img src="', response_str)
        self.assertIn('class="img-circle"', response_str)

    def test_link(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('href="https://github.com/rodovalhovic"', response_str)
        self.assertIn('>Me siga no GitHub</a>', response_str)



if __name__ == '__main__':
    unittest.main()