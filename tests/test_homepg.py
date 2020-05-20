import pytest
from pages.LoginPage import loginpage
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


@allure.title('tc-18,Verify Watch Now button is clikable and on click of it opens playout pop up')
def test_watchnow(browser):
    global listdet
    listdet = homepg(browser)
    assert listdet.verify_watchnow() == True, "play out popup not found"


@allure.title('tc-20,Verify all controls of the pop up works correctly')
def test_popupcontrols(browser):
    global listdet
    listdet = homepg(browser)
    assert listdet.verify_popupmutecontrols() == "bmpui-ui-volumetogglebutton bmpui-unmuted", "mute unmute button not found"
    assert listdet.verify_popupplaycontrols() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "play pause button not found"


@allure.title('tc-36,Verify functionality of Add to List button')
def test_addtolistbutton(browser):
    global listdet
    listdet = homepg(browser)
    listdet.verify_closeplayer()
    assert listdet.verify_addtolistbutton() == True, "add to list button not found"
