@given(u'que estou na pagina incial do site da americanas')
def step_impl(context):
    context.home.go_home()


@when(u'entro na pagina de cadastro de cupom')
def step_impl(context):
    context.home.selecionar_campo()


@when(u'entro com meu email')
def step_impl(context):
    context.home.entrar_email()


@then(u'o cadastro deve ser concluido')
def step_impl(context):
    context.home.entrar()