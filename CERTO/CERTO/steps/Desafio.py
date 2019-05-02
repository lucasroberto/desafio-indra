@given(u'que estou na pagina principal')
def step_impl(context):
    context.home.go_home()


@when(u'seleciono o tipo Moda')
def step_impl(context):
    context.home.selecionar_moda()


@then(u'ele deve filtrar os produtos do menor para o maior')
def step_impl(context):
    context.home.filtrar()