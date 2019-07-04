from requests_html import AsyncHTMLSession, HTMLSession
from bs4 import BeautifulSoup
from modules.MyAsync import myAsync


class main():
    print('hello')
    session = HTMLSession()
    asession = AsyncHTMLSession()

    search = 'informatica';
    city = 'aveiro'
    r = session.get('http://www.net-empregos.com/listagem_livre2_2.asp?CHAVES=' + search + '-' + city)
    # print(r.text)

    # result = asession.run(myAsync.get_sapo(asession, 'http://emprego.sapo.pt/'),
    #                      myAsync.get_net_emprego(asession, 'http://www.net-empregos.com/'))

    # soup = BeautifulSoup(r.text, 'html.parser')
    # view_state = soup.find_all(id='__VIEWSTATE')

    # print(view_state['value'])
    # print(soup.find_all(id='ctl00_ContentPlaceHolderMain_Search_ddlCountry'))
    # lol = view_state[0]['value']
    # print(lol)

    # url = 'http://emprego.sapo.pt/emprego/ofertas.htm/pais/portugal/distrito/aveiro/palavras-chave/it'

    # payload = {
    #     '__EVENTTARGET': '',
    #     '__EVENTARGUMENT': '',
    #     '__LASTFOCUS': '',
    #     '__VIEWSTATE': view_state[0]['value'],
    #     'ctl00$ContentPlaceHolderMain$Search$txtKeywords': 'it',
    #     'ctl00$ContentPlaceHolderMain$Search$ddlCategories': -1,
    #     'ctl00$ContentPlaceHolderMain$Search$ddlCountry': 620,
    #     'ctl00$ContentPlaceHolderMain$Search$ddlDistrict': 1,
    #     'ctl00$ContentPlaceHolderMain$Search$btnSearch': 'Pesquisar',
    #     '__VIEWSTATEGENERATOR': 'D5F5AE94'
    # }

    # session = session()
    # r = session.post(url, data=payload)
    # print(r.text)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # # print(soup.text)
    # print(soup.find_all(id='ctl00_ContentPlaceHolderMain_Search_txtKeywords'))


if __name__ == '__main__':
    main()
