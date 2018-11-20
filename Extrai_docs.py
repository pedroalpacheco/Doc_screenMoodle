from selenium import webdriver
"""Pedro Al Pacheco, 19/11/2018 - pedro.pacheco.a@gmail.com - version: 0.01"""
"""Tira print e documenta configurações do moodle"""

usuario = input("Digite o usuario : ")
senha = input("Digite a senha: ")


def screenconf(url, nome):
    driver = webdriver.PhantomJS(executable_path='.venv/bin/phantomjs')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(usuario)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(senha)
    driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
    driver.save_screenshot(nome+'.png')
    driver.close()

try:
    """Tira print de olugins adicionais"""
    screenconf('http://moodle35.furb.br/moodlesec/admin/plugins.php?updatesonly=0&contribonly=1', 'pluginsAdicionais')

    """Tira print de configurações de office365"""
    screenconf('http://moodle35.furb.br/moodlesec/admin/settings.php?section=authsettingoidc', 'confOf365')
    print('Prints realizados com sucesso!!, obs.: Caso aparecer tela de usuario e senha no print é por que a senha ou usuário esta errada')
except:
    print("Ocorreu um erro, favor verificar usuário e senha!")





