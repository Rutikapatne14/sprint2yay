# run from here, functions are called here
from Pom.appnshoes import Apparelshoes

class TestAp:
    def test_login(self, _driver):
        demo = Apparelshoes(_driver)
        demo.clickmodule()
        demo.clickdisplayfour()
        demo.clickdisplayeight()
        demo.clickdisplaytwelve()
        demo.clicksortbyatoz()
        demo.clicksortbyztoa()
        demo.clicksortbyhightolow()
        demo.clicksortbylowtohigh()
        demo.clicksortbycreatedon()
        demo.clickviewaslist()
        demo.clickviewasgrid()
        demo.clickopenproduct()
        demo.click_eachproducts_addtocart()















        # html report pytest test_appnshoes.py -vs --html="report.html"