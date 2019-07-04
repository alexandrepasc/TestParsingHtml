class myAsync():
    async def get_sapo(asession, url):
        r = await asession.get(url)

    async def get_net_emprego(asession, url):
        r = await asession.get(url)
