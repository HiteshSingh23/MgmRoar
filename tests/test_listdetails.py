import pytest
from pages.LoginPage import loginpage
from pages.ListDetails import ListDetails
from pages.moviedetails import moviedetails
from pages.tvdetails import tvdetails
from pages.homepg import homepg
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
#
#
# @allure.title('Verify carousel image set by admin is visible')
# def test_verifycarousalimage(browser):
#     verify = user.CarouselImage()
#     assert verify == True
#
#
# @allure.title('verify elements present in login model')
# def test_elementloginmodel(browser):
#     email = user.VerifyEmail()
#     assert email == True, "Email textbox not found"
#     next_button = user.VerifyNextButton()
#     assert next_button == True, "Next button not found"
#     # request_account = user.VerifyRequestAnAccount()
#     # assert request_account == True, "Request an account button not found"
#
#
# @allure.title('Verify user is able to enter Email in email field')
# def test_enteremail(browser):
#     user.EnterEmail(email)
#
#
# @allure.title('Verify user with valid email id can proceed to next step')
# def test_clicknext(browser):
#     verify = user.ClickNext()
#     assert verify == True, "user not proceed to next step with valid email id"
#
#
# @allure.title('verify user is successfully logged in')
# def test_login(browser):
#     user.EnterPassword(password)
#     user.ClickNext()
#     time.sleep(10)
#     verify = user.VerifyLogin()
#     assert verify == True, "User is not able to login with valid credentials"
#
#
# @allure.title('tc-35,Verify elements in mylist details page')
# def test_mylistdetails(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     listdet.verify_addmovietolist()
#     listdet.verify_mylist()
#     assert listdet.verify_listheadername() == 'movietest', "title not found in list details page"
#     assert listdet.verify_listgridbutton() == True, "grid button not found in list details page"
#     assert listdet.verify_listbutton() == True, "list button not found in list details page"
#     assert listdet.verify_sharebutton() == True, "share button not found in list details page"
#     assert listdet.verify_deletebutton() == True, "delete button not found in list details page"
#     assert listdet.verify_moviedetail() == True, "movie details not found in list details page"
#     assert listdet.verify_moviecheckbox() == True, "movie checkbox not found in list details page"
#     # assert listdet.verify_listcheckbox() == True, "checkbox button not found in list details page"

#
# @allure.title('tc-36,Verify overlay present in movie card')
# def test_mylistoverlaydetails(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     listdet.verify_overlaypanel()
#     assert listdet.verify_addolist() == True, "add to list element not found"
#     assert listdet.verify_watchmovie() == True, "watch movie element not found"
#     assert listdet.verify_watchtrailer() == True, "watch trailer element not found"
#     assert listdet.verify_viewdetails() == True, "view details element not found"
#
#
# @allure.title('tc-38,Verify list view is displayed')
# def test_listview(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     listdet.verify_listview()
#
#
# @allure.title('tc-39,Verify elements list view is displayed')
# def test_listelements(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_listelements() == 'TITLE', "title header in list not found"
#     assert listdet.verify_directedelements() == 'DIRECTED BY', "DIRECTED BY header in list not found"
#     assert listdet.verify_maincastelements() == 'MAIN CAST', "MAIN CAST header in list not found"
#     assert listdet.verify_synopsiselements() == 'SYNOPSIS', "SYNOPSIS header in list not found"
#
#
# @allure.title('tc-40,verify user is able to select title using checkbox')
# def test_titleselect(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_titleselect() == True, "list title is not selected"
#
#
# @allure.title('tc-41,To verify footer section when selected a title')
# def test_footersection(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_footersection() == True, "footer section not found"
#
#
# @allure.title('tc-42,To verify added title to the list')
# def test_addtitletolist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_addtitletolist() == True, "Added title in list not found"
#
#
# @allure.title('tc-43,To verify created list in add to list')
# def test_createlist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_createlist() == True, "created list not found in add to list items"
#
#
# @allure.title('tc-44,To verify title in created list')
# def test_titleincreatedlist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_createdlist() == True, "created list not found"
#     assert listdet.verify_titleincreatedlist() == True, "title not found in created list"
#
#
# @allure.title('tc-45,To verify user is able to share title')
# def test_sharelist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_sharewindow() == True, "share window not found"
#     assert listdet.verify_shareemail() == False, "List not shared through mail"
#
#
# @allure.title('tc-47,To verify user is able to download csv')
# def test_downloadcsv(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_downloadcsv() == True, "downloaded csv not found"
#
#
# @allure.title('tc-48,To verify select all titile checkbox')
# def test_selectalltitle(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_selectalltitle() == True, "select all checkbox not selected"
#
#
# @allure.title('tc-50,To Verify User is able to share list by clicking on Share button in header')
# def test_sharelistheader(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_sharelistheader() == False, "List not shared through mail"
#
#
# @allure.title('tc-46,To verify delete title in the list')
# def test_deletetitle(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     listdet.verify_deletetitle()
#
#
# @allure.title('tc-49,To Verify user is able to Delete list')
# def test_deletelist(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_deletelist() == False, "list not removed from my list page"
#
#
# @allure.title('tc-4,Verify My List is underlined in Menu')
# def test_listunderline(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_listunderline() == "ng-star-inserted active", "uderline uder list menu not found"
#
#
# @allure.title('tc-37,To verify Watch Movie should not be shown in case of a TV entity')
# def test_watchmovieintv(browser):
#     global listdet
#     listdet = ListDetails(browser)
#     assert listdet.verify_watchmovieintv() == False, "Watch Movie should shown in case of a TV entity"
#
#
# """moviedetails"""
#
#
# @allure.title('tc-26,Verify elements in movie details page')
# def test_moviedetails(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     listdet.verify_moviedetails()
#     assert listdet.verify_movieheader() == True, "movie header section not found"
#     assert listdet.verify_movietrailer() == True, "movie trailer section not found"
#     assert listdet.verify_moviephotos() == True, "movie photos section not found"
#     assert listdet.verify_moviecastprod() == True, "movie cast prod section not found"
#     # assert listdet.verify_moviesynopsis() == True, "movie synopsis section not found"
#
#
# @allure.title('tc-27,Verify elements in header of Movie Details page')
# def test_movieheaderdetails(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_movieheaderimage() == True, "movie header image not found"
#     assert listdet.verify_movielogo() == True, "movie title logo not found"
#     assert listdet.verify_watchmoviebutton() == True, "watch movie button not found"
#     assert listdet.verify_watchtrailerbutton() == True, "watch trailer button not found"
#     assert listdet.verify_addtolistbutton() == True, "Add to List button not found"
#
#
# @allure.title('tc-28,To verify watch movie on movie button click')
# def test_watchmovie(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_watchmovie() == True, "movie header image not found"
#
#
# @allure.title('tc-29,To verify watch trailer on watch trailer button click')
# def test_watchtrailer(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     listdet.verify_watchtrailer()
#     assert listdet.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
#                                                                                          "button trailer is not " \
#                                                                                          "getting played. "
#
#
# @allure.title('tc-30,To verify added movie in the list')
# def test_addedmovieinlist(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_addedmovieinlist() == True, "added movie is not found in the list"
#
#
# @allure.title('tc-31,Verify elements in Synopsis section of Movie Details page')
# def test_synopsiselement(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     listdet.verify_moviedetails()
#     assert listdet.verify_synopsisimage() == True, "Synopsis image not found"
#     assert listdet.verify_synopsisdesc() == True, "Synopsis desc not found"
#     assert listdet.verify_synopsisrate() == True, "Synopsis rate not found"
#     assert listdet.verify_synopsisgenre() == True, "Synopsis genre not found"
#     assert listdet.verify_synopsisrelease() == True, "Synopsis release date not found"
#     assert listdet.verify_synopsisdirector() == True, "Synopsis director date not found"
#     assert listdet.verify_synopsiscast() == True, "Synopsis cast not found"
#     assert listdet.verify_synopsiscopyright() == True, "Synopsis copy right not found"
#
#
# @allure.title('tc-32,Verify elements in Trailer section of Movie Details page')
# def test_trailerelements(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_trailerelements() == True, "Trailer title not found"
#     assert listdet.verify_trailerplayer() == True, "Player not found"
#
#
# @allure.title('TC: 33, Verify user is able to play the trailer of the movie')
# def test_trailerPlay(browser):
#     trailer = moviedetails(browser)
#     trailer.refresh()
#     time.sleep(30)
#     trailer.click_trailer_button()
#     time.sleep(15)
#     assert trailer.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
#                                                                                          "button trailer is not " \
#                                                                                          "getting played. "
#
#
# @allure.title('tc-34,Verify photo elements in Movie Details page')
# def test_photoelements(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_phototitle() == True, "Trailer title not found"
#     assert listdet.verify_photoslidearrow() == True, "slide arrow not found"
#     assert listdet.verify_photoviewport() == True, "view port not found"
#
#
# @allure.title('tc-35,User should be able to navigate between photos by clicking the arrows')
# def test_photoslidearrow(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_photoslidearrow() == True, "photo not changed"
#
#
# @allure.title('tc-37,Verify elements of Cast, Crew & Production')
# def test_castdetails(browser):
#     global listdet
#     listdet = moviedetails(browser)
#     assert listdet.verify_castdetails() == True, "Cast Details not found"
#     assert listdet.verify_directorname() == True, "Director name not found"
#     assert listdet.verify_producername() == True, "Producer name not found"
#     assert listdet.verify_execproducername() == True, "Exec. Producer name not found"
#
#
# """tv details"""
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
#
#
# @allure.title('tc-18,Verify Watch Now button is clikable and on click of it opens playout pop up')
# def test_watchnow(browser):
#     global listdet
#     listdet = homepg(browser)
#     assert listdet.verify_watchnow() == True, "play out popup not found"
#
#
# @allure.title('tc-20,Verify all controls of the pop up works correctly')
# def test_popupcontrols(browser):
#     listdet = homepg(browser)
#     assert listdet.verify_popupmutecontrols() == "bmpui-ui-volumetogglebutton bmpui-unmuted", "mute unmute button not found"
#     assert listdet.verify_popupplaycontrols() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "play pause button not found"
#
#
# def test_closeplayer(browser):
#     global listdet
#     listdet = homepg(browser)
#     listdet.verify_closeplayer()
#
#
# @allure.title('tc-36,Verify functionality of Add to List button')
# def test_addtolistbutton(browser):
#     global listdet
#     listdet = homepg(browser)
#     assert listdet.verify_addtolistbutton() == True, "add to list button not found"
#     listdet.browser.refresh()
