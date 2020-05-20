import pytest
from pages.LoginPage import loginpage
from pages.moviedetails import moviedetails
from pages.tvdetails import tvdetails
from resources.variables import *
import allure
import time


@allure.title('Verify user lands on login page')
@pytest.mark.usefixtures("browser")
def test_loginpage(browser):
    global user
    user = loginpage(browser)
    verify = user.load()
    assert verify == "Log in to MGM ROAR", "Unable to load login page"
    print(verify)


@allure.title('Verify carousel image set by admin is visible')
def test_verifycarousalimage(browser):
    verify = user.CarouselImage()
    assert verify == True


@allure.title('verify elements present in login model')
def test_elementloginmodel(browser):
    email = user.VerifyEmail()
    assert email == True, "Email textbox not found"
    next_button = user.VerifyNextButton()
    assert next_button == True, "Next button not found"
    # request_account = user.VerifyRequestAnAccount()
    # assert request_account == True, "Request an account button not found"


@allure.title('Verify user is able to enter Email in email field')
def test_enteremail(browser):
    user.EnterEmail(email)


@allure.title('Verify user with valid email id can proceed to next step')
def test_clicknext(browser):
    verify = user.ClickNext()
    assert verify == True, "user not proceed to next step with valid email id"


@allure.title('verify user is successfully logged in')
def test_login(browser):
    user.EnterPassword(password)
    user.ClickNext()
    time.sleep(10)
    verify = user.VerifyLogin()
    assert verify == True, "User is not able to login with valid credentials"


@allure.title('tc-26,Verify elements in movie details page')
def test_moviedetails(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_moviedetails()
    assert listdet.verify_movieheader() == True, "movie header section not found"
    assert listdet.verify_movietrailer() == True, "movie trailer section not found"
    assert listdet.verify_moviephotos() == True, "movie photos section not found"
    assert listdet.verify_moviecastprod() == True, "movie cast prod section not found"
    # assert listdet.verify_moviesynopsis() == True, "movie synopsis section not found"


@allure.title('tc-27,Verify elements in header of Movie Details page')
def test_movieheaderdetails(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_movieheaderimage() == True, "movie header image not found"
    assert listdet.verify_movielogo() == True, "movie title logo not found"
    assert listdet.verify_watchmoviebutton() == True, "watch movie button not found"
    assert listdet.verify_watchtrailerbutton() == True, "watch trailer button not found"
    assert listdet.verify_addtolistbutton() == True, "Add to List button not found"


@allure.title('tc-28,To verify watch movie on movie button click')
def test_watchmovie(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_watchmovie() == True, "movie header image not found"


@allure.title('tc-29,To verify watch trailer on watch trailer button click')
def test_watchtrailer(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_watchtrailer()
    assert listdet.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
                                                                                         "button trailer is not " \
                                                                                         "getting played. "


@allure.title('tc-30,To verify added movie in the list')
def test_addedmovieinlist(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_addedmovieinlist() == True, "added movie is not found in the list"


@allure.title('tc-31,Verify elements in Synopsis section of Movie Details page')
def test_synopsiselement(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_moviedetails()
    assert listdet.verify_synopsisimage() == True, "Synopsis image not found"
    assert listdet.verify_synopsisdesc() == True, "Synopsis desc not found"
    assert listdet.verify_synopsisrate() == True, "Synopsis rate not found"
    assert listdet.verify_synopsisgenre() == True, "Synopsis genre not found"
    assert listdet.verify_synopsisrelease() == True, "Synopsis release date not found"
    assert listdet.verify_synopsisdirector() == True, "Synopsis director date not found"
    assert listdet.verify_synopsiscast() == True, "Synopsis cast not found"
    assert listdet.verify_synopsiscopyright() == True, "Synopsis copy right not found"


@allure.title('tc-32,Verify elements in Trailer section of Movie Details page')
def test_trailerelements(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_trailerelements() == True, "Trailer title not found"
    assert listdet.verify_trailerplayer() == True, "Player not found"


@allure.title('TC: 33, Verify user is able to play the trailer of the movie')
def test_trailerPlay(browser):
    trailer = moviedetails(browser)
    trailer.refresh()
    time.sleep(30)
    trailer.click_trailer_button()
    time.sleep(15)
    assert trailer.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
                                                                                         "button trailer is not " \
                                                                                         "getting played. "


@allure.title('tc-34,Verify photo elements in Movie Details page')
def test_photoelements(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_phototitle() == True, "Trailer title not found"
    assert listdet.verify_photoslidearrow() == True, "slide arrow not found"
    assert listdet.verify_photoviewport() == True, "view port not found"


@allure.title('tc-35,User should be able to navigate between photos by clicking the arrows')
def test_photoslidearrow(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_photoslidearrow() == True, "photo not changed"


@allure.title('tc-37,Verify elements of Cast, Crew & Production')
def test_castdetails(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_castdetails() == True, "Cast Details not found"
    assert listdet.verify_directorname() == True, "Director name not found"
    assert listdet.verify_producername() == True, "Producer name not found"
    assert listdet.verify_execproducername() == True, "Exec. Producer name not found"

#
#
# @allure.title('tc-31,Verify elements in synopsis section in tv details page')
# def test_tvdetails(browser):
#     global listdet
#     listdet = tvdetails(browser)
#     listdet.verify_Tvdetails()
#     assert listdet.verify_synopsisimage() == True, "Synopsis image not found"
#     assert listdet.verify_synopsisdesc() == True, "Synopsis desc not found"
#     assert listdet.verify_synopsisrate() == True, "Synopsis rate not found"
#     assert listdet.verify_synopsisgenre() == True, "Synopsis genre not found"
#     assert listdet.verify_synopsisrelease() == True, "Synopsis release date not found"
#     assert listdet.verify_synopsiscast() == True, "Synopsis cast not found"
#     assert listdet.verify_synopsiscopyright() == True, "Synopsis copy right not found"
#
#
# @allure.title('tc-32,Verify elements in Trailer section of TV Details page')
# def test_trailerelements(browser):
#     global listdet
#     listdet = tvdetails(browser)
#     assert listdet.verify_trailertitle() == True, "Trailer title not found"
#     assert listdet.verify_trailerscreen() == True, "Player screen not found"
#
#
# @allure.title('TC: 33, Verify user is able to play the trailer of the movie')
# def test_trailerPlay(browser):
#     trailer = tvdetails(browser)
#     time.sleep(15)
#     assert trailer.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
#                                                                                          "button trailer is not " \
#                                                                                          "getting played. "
#
#
# @allure.title('tc-34,Verify photo elements in tv Details page')
# def test_photoelements(browser):
#     global listdet
#     listdet = tvdetails(browser)
#     assert listdet.verify_phototitle() == True, "Trailer title not found"
#     assert listdet.verify_photoslidearrow() == True, "slide arrow not found"
#     assert listdet.verify_photoviewport() == True, "view port not found"
#
#
# @allure.title('tc-35,User should be able to navigate between photos by clicking the arrows')
# def test_photoslidearrow(browser):
#     global listdet
#     listdet = tvdetails(browser)
#     assert listdet.verify_photoslidearrow() == True, "photo not changed"
#
#
# @allure.title('tc-37,Verify elements of Cast, Crew & Production')
# def test_castdetails(browser):
#     global listdet
#     listdet = tvdetails(browser)
#     assert listdet.verify_castdetails() == True, "Cast Details not found"
#     assert listdet.verify_execproducername() == True, "Exec. Producer name not found"
