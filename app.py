from flask import Flask, render_template

meu_web_app = Flask('meu_web_app')

SIMÃO = {
    'nome': 'Eduardo Simão',
    'descricao': 'Universitario, Fã de filmes e séries e blogayro nas horas vagas(rsrs).',
    'url': 'http://intagram.com/1niverse',
    'nome_url': 'Instagram',
    'foto': 'https://avatars0.githubusercontent.com/u/41209185?s=460&v=4'}

LOPES = {'nome': 'Thais Lopes',
          'descricao': 'Universitaria.',
          'url': 'https://github.com/Tclsantos09',
          'nome_url': 'GitHub',
          'foto': 'https://avatars2.githubusercontent.com/u/37407940?s=460&v=4'}

RODOVALHO = {'nome': 'Victoria Rodovalho',
          'descricao': 'Universitaria.',
          'url': 'https://github.com/rodovalhovic',
          'nome_url': 'GitHub',
          'foto': 'https://avatars3.githubusercontent.com/u/37520274?s=460&v=4'}



PERFIS = {'simao': SIMÃO,
          'lopes': LOPES,
          'rodovalho': RODOVALHO}



@meu_web_app.route('/<perfil>')
def pagina_inicial(perfil):
    perfil = PERFIS[perfil]
    return render_template('home.html', perfil=perfil)



if __name__ == '__main__':
    meu_web_app.run(debug=True)