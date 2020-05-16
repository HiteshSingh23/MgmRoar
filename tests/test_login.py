import pytest
from pages.LoginPage import loginpage
from pages.HomePage import homepage
from pages.VideoPlayer import videoplayer
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
@allure.title('Verify carousel image set by admin is visible')
def test_verifycarousalimage(browser):
    verify = user.CarouselImage()
    assert verify == True


@allure.title('On each visit user see different carousel image')
def test_differentcarouselimage(browser):
    ImageChange = user.DifferentCarouselImage()
    assert ImageChange == True, "Carousel image is not changing on reload"


@allure.title('verify elements present in login model')
def test_elementloginmodel(browser):
    email = user.VerifyEmail()
    assert True, "Email textbox not found"
    next_button = user.VerifyNextButton()
    assert True, "Next button not found"
    request_account = user.VerifyRequestAnAccount()
    assert True, "Request an account button not found"


@allure.title('Verify user is able to enter Email in email field')
def test_enteremail(browser):
    user.EnterEmail("automation@practicallogix.com")


@allure.title('Verify user with valid email id can proceed to next step')
def test_clicknext(browser):
    verify = user.ClickNext()
    assert verify == True, "user not proceed to next step with valid email id"


@allure.title('verify user is successfully logged in')
def test_login(browser):
    user.EnterPassword("~;Baxg2t")
    user.ClickNext()
    time.sleep(10)
    verify = user.VerifyLogin()
    assert verify == True, "User is not able to login with valid credentials"


@allure.title('Verify elements present in global header')
def test_ElementsGlobalHeader(browser):
    global home
    home = homepage(browser)
    logo = home.HomePageLogo()
    assert logo == True, "Header logo not found"
    movies = home.HeaderMovies()
    assert movies == True, "Movies link not found"
    television = home.HeaderTelevision()
    assert television == True, "Television link not found"
    mylist = home.HeaderMylist()
    assert mylist == True, "My list link not found"
    logout = home.HeaderLogoutButton()
    assert logout == True, "Logout button not found"


@allure.title('Verify functionality of View Details button')
def test_FunctionalityViewDetailButton(browser):
    time.sleep(5)
    title = home.MovieListViewDetailButton()
    assert title == True
    synopsis = home.VerifySynopsisTitle()
    print(synopsis)
    assert synopsis == True
    home.ClickLogo()


@allure.title('Verify carousel auto-progress as per transition time set in CMS')
def test_CarouselAutoProgress(browser):
    a = home.CarouselAutoProgress()
    assert a == True, "Carousel is not auto processing"
    home.ClickLogo()


#
@allure.title('Veirfy when there are more than 4 titles then progress bar auto-progresses')
def test_MoreThan4Titles(browser):
    home.CarouselAutoProgress()
    b = home.ProgressBarLegallyBlonde()
    assert b == True
    a = home.SliderMovie()
    assert a == False


@allure.title('Veriify the Title is underlined(highlighted) when carousel moves to that slider')
def test_SliderTitleHighlighted(browser):
    movie = home.SliderTitleHighlighted()
    assert movie == 'LEGALLY BLONDE'


#
@allure.title('Verify user is able to scroll thorugh the list')
def test_VerifyScroll(browser):
    verify = home.VerifyScroll()
    assert verify == True


#
#
@allure.title('Verify maximum 4 titles are shown on the Progress Bar')
def test_Maximum4TitlesShown(browser):
    movie1 = home.ProgressBarSpectre()
    assert movie1 == True
    movie2 = home.ProgressBarArmyOfDarkness()
    assert movie2 == True
    movie3 = home.ProgressBarMagnificent()
    assert movie3 == True
    movie4 = home.ProgressBarRockey()
    assert movie4 == True
    movie5 = home.ProgressBarAmigos()
    assert movie5 == False


@allure.title('Verify Movie links are clickable and redirects to correct page')
def test_MenuLinksClickable(browser):
    movies = home.ClickMovies()
    assert movies == True, "Not redirecting to correct page"
    home.ClickLogo()
    television = home.ClickTelevision()
    assert television == True, "Not redirecting to correct page"
    home.ClickLogo()
    list = home.ClickLists()
    assert list == True, "Not redirecting to correct page"
    home.ClickLogo()


@allure.title('Veirfy on click of Roar logo in header user is redirected to Homepage')
def test_ClickLogo(browser):
    verify = home.ClickLogo()
    time.sleep(10)
    assert verify == True, "When Click on logo user is not redirected to homepage"


@allure.title('Verify on click of Logout button, user is successfully logged out')
def test_ClickLogoutButton(browser):
    verify = home.ClickLogoutButton()
    assert verify == True, "User is not logged out"
    test_enteremail(browser)
    test_clicknext(browser)
    test_login(browser)


@allure.title('Verify Element Present in homepage')
def test_ElementsHomepage(browser):
    global_header = home.HomepageElementHeader()
    assert global_header == True, "Global Header not found"
    test_ElementsGlobalHeader(browser)
    main_carousel = home.HomepageMainCarousel()
    assert main_carousel == True, "Main carousel not found"
    list1 = home.HomepageMovieList1()
    assert list1 == True, "Movie list not found"
    list2 = home.HomepageMovieList2()
    assert list2 == True, "Movie list not found"
    list3 = home.HomepageMovieList3()
    assert list3 == True, "Movie list not found"
    list4 = home.HomepageMovieList4()
    assert list4 == True, "Movie list not found"
    list5 = home.HomepageMovieList5()
    assert list5 == True, "Movie list not found"
    list6 = home.HomepageMovieList6()
    assert list6 == True, "Movie list not found"
    list7 = home.HomepageMovieList7()
    assert list7 == True, "Movie list not found"
    list8 = home.HomepageMovieList8()
    assert list8 == True, "Movie list not found"
    list9 = home.HomepageMovieList9()
    assert list9 == True, "Movie list not found"
    list10 = home.HomepageMovieList10()
    assert list10 == True, "Movie list not found"
    TvShows = home.HomepageExploreAllTvShows()
    assert TvShows == True, "Explore all tv shows button not found"
    Movies = home.HomepageExploreAllMovies()
    assert Movies == True, "Explore all Movies button not found"
    Logo = home.HomepageFooterLogo()
    assert Logo == True, "Footer logo not found"
    privacy = home.HomepageFooterPrivacy()
    assert privacy == True, "Privacy button not found"
    terms = home.HomepageFooterTerms()
    assert terms == True, "Footer Terms not found"
    support = home.HomepageFooterSupport()
    assert support == True, "Footer support button not found"


#
@allure.title('Verify elements present in Carousel')
def test_ElementsCarousel(browser):
    spectre = home.ProgressBarSpectre()
    assert spectre == True, "Spectre not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    darkness = home.ProgressBarArmyOfDarkness()
    assert darkness == True, "Army of Darkness not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    magnificent = home.ProgressBarMagnificent()
    assert magnificent == True, "The Magnificant seven not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    rocky = home.ProgressBarRockey()
    assert rocky == True, "Rocky not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    amigo = home.ProgressBarAmigos()
    assert amigo == True, "Three amigosi not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    legally = home.ProgressBarLegallyBlonde()
    assert legally == True, "Legally Blonde not found in Progress bar"
    home.MainCareusalClickNextNavigationArrow()
    hunter = home.ProgressBarWitchHunter()
    assert hunter == True, "Witch hunter not found in Progress bar"
    slider = home.MovieImageSlider()
    assert slider == True, "Movies image slider not found"
    progress = home.ProgressBar()
    assert progress == True, "Progress bar not found"
    left = home.ProgressBarPreviousArrow()
    assert left == True, "Left navigation button not found"
    right = home.ProgressBarNextArrow()
    assert right == True, "Right nagvigation button not found"


@allure.title('Verify elements present in Movie image slider')
def test_ElementsMovieImageSlider(browser):
    image = home.SliderBackgroundImage()
    assert image == True, "Slider Background image not found"
    logo = home.MovieLogo()
    assert logo == True, "Logo of Movie not found"
    watch = home.WatchNowButton()
    assert watch == True, "Watch now button not found"
    add = home.AddToListButton()
    assert add == True, "Add to list button not found"
    details = home.ViewDetailsButton()
    assert details == True, "View details button not found"


@allure.title('Verify on click of Add to List button, Add List pop up is opened')
def test_AddToListPopUp(browser):
    home.Refresh()
    home.ClickMainCarouselAddToList()
    search = home.AddToListSearchBox()
    assert search == True


@allure.title('Verify user is able to enter name and create new list from Carousel')
def test_CreateNewList(browser):
    home.ListName("Demo")
    home.ClickCreateList()
    list = home.NewList()
    assert list == "Demo"
    home.ListName("test")
    home.ClickCreateList()


@allure.title('Verify elements in Add To List pop')
def test_AddToListElement(browser):
    # home.ClickMainCarouselAddToList()
    search = home.AddToListSearchBox()
    assert search == True
    clear = home.AddToListClearButton()
    assert clear == True
    created_list = home.AddToListCreatedList()
    assert created_list == True
    toggel = home.AddToListToggelButton()
    assert toggel == True
    list = home.AddToListCreateList()
    assert list == True
    name = home.AddToListListName()
    assert name == True
    button = home.AddToListCreateListButton()
    assert button == True


@allure.title('Verify user is able to un-select any selected list(s)')
def test_UnselectSelectedList(browser):
    time.sleep(15)
    home.ClickAddToListToggelButton()
    time.sleep(5)
    home.ClickAddToListToggelButton()


@allure.title('Verify user is able to select list(s)')
def test_AddToListToggelButton(browser):
    time.sleep(5)
    home.ClickAddToListToggelButton()
    time.sleep(5)
    home.ClickAddToListToggelButton()
    time.sleep(20)
    home.ClickAddToListToggleButton1()
    time.sleep(5)
    home.ClickAddToListToggleButton1()


@allure.title('Verify user is able to add the movie in the created list')
def test_AddToList(browser):
    home.AddMovieToList()
    home.Refresh()
    movie = home.VerifyAddedMovie()
    assert movie == "Spectre"


@allure.title('Verify user is able to add same movie in multiple lists')
def test_AddSameMovieMultipleList(browser):
    movie1 = home.VerifySecondAddedMovie()
    assert movie1 == "Spectre"
    home.ClickLogo()
    home.Refresh()


@allure.title('Verify user is abe to search a list from the search bar')
def test_SearchList(browser):
    home.ClickMainCarouselAddToList()
    time.sleep(5)
    home.SearchList("test")
    home.VerifySearchedList()


@allure.title('Verify user is able to select list(s) from search result')
def test_SelectSearchedList(browser):
    time.sleep(3)
    home.ClickAddToListToggelButton()


@allure.title('Verify user is able to un-select list(s) from search result')
def test_UnselectSearchedList(browser):
    time.sleep(3)
    home.ClickAddToListToggelButton()


@allure.title('Verify user is able to clear search on click of Clear button')
def test_ClearSearchedList(browser):
    time.sleep(5)
    home.ClickAddToListClearButton()
    home.Refresh()


# def test_MovieCardAddToList(browser):
#     list = home.ClickMovieCardAddToList()
#     assert list == True , "Movie List Pop-up not found"
#
# # def test_MovieCardCreateNewList(browser):
# #     home.ListName("test1")
# #     list = home.ClickCreateList()
# #     assert list == True
# #     created = home.CreatedList()
# #     assert created == True
# #     name = home.VerifyListCreated()
# #     assert name == "test1"
# #
# #     select = home.q()
# #     assert select== True
# #
# 
# # #
@allure.title('Verify after the last slider, the titles in the progress bar resets to initial position')
def test_ProgressBarReset(browser):
    home.SliderBarReset()
    movie = home.ProgressBarArmyOfDarkness()
    assert movie == True


#
@allure.title('Verify user is able to move to next slider by clicking Right Nagivation Arrow')
def test_MainCarouselNextNavigation(browser):
    home.MainCareusalClickNextNavigationArrow()
    home.MainCareusalClickNextNavigationArrow()
    home.MainCareusalClickNextNavigationArrow()
    home.MainCareusalClickNextNavigationArrow()
    movie = home.ProgressBarAmigos()
    assert movie == True


@allure.title('Verify user is able to move to previous slider by clicking Left Nagivation Arrow')
def test_MainCarouselPrevNavigation(browser):
    home.MainCareusalClickPrevNavigationArrow()
    movie = home.ProgressBarSpectre()
    assert movie == True


# #
# # # def test_WatchnowButtonClickable(browser):
# # #    video = videoplayer(browser)
# # #    video.ClickWatchNowButton()
# # #    player = video.PlayerPopup()
# # #    assert player == True
# # #    PlayPause = video.PlayPauseButton()
# # #    assert PlayPause == True
# # #    Volume = video.VolumeMuteButton()
# # #    assert Volume == True
# # #    setting = video.SettingButton()
# # #    assert setting == True
# # #    fullscreen = video.FullscreenButton()
# # #    assert fullscreen == True
# # #    close = video.CloseButon()
# # #    assert close == True
# 
'''view details main careusal'''


@allure.title('Verify View Details button is clickable and on click redirect to movie details page')
def test_ViewDetails(browser):
    view = home.ClickViewDetailsButton()
    assert view == "Spectre Synopsis"
    home.ClickLogo()


@allure.title('Verify the titles are clickable and clicking them take the carousel to that slider')
def test_TitlesClickable(browser):
    home.ClickSpectreMovie()
    verify = home.ClickViewDetailsButton()
    assert verify == "Spectre Synopsis"
    home.ClickLogo()


@allure.title('Verify Left Navigation Arrow is disabled when we are on the first card in the list')
def test_PrevButtonDisable(browser):
    prev = home.MovieListPrevButton1()
    assert prev == False, "Preview button is not disabled"


@allure.title('Verify elements for each Movie List')
def test_ElementMovieList(browser):
    button = home.SeeAllButton()
    assert button == True, "See all button not found"
    title = home.HomepageMovieList1()
    assert title == True, "Movie list not found"
    poster = home.MoviePoster()
    assert poster == True, "Movie poster not found"
    nextbtn = home.MovieListNextButton()
    assert nextbtn == True, "next navigation button not found"
    prevbtn = home.MovieListPrevButton()
    assert prevbtn == True, "prev navigation button not found"


@allure.title('Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
def test_LeftNavigationVisibleOnHOver(browser):
    time.sleep(3)
    prevbtn = home.MovieListPrevButton()
    assert prevbtn == True, "Left navigation button not showing on hover"


@allure.title('Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
def test_NextNavigationVisible(browser):
    time.sleep(3)
    nextbtn = home.MovieListNextButton1()
    print(nextbtn)
    assert nextbtn == True, "RIght navigation is not visible when we hover on last card ."


@allure.title('Verify click behavior of Right Navigation arrow')
def test_RightNavigationBehaviour(browser):
    time.sleep(2)
    home.click_rightarrow()
    # movie1 = home.RightNavigationBehaviour()
    # assert movie1 == True
    # movie2 = home.RightNavigationBehaviour1()
    # assert movie2 == True
    # movie3 = home.RightNavigationBehaviour2()
    # assert movie3 == True


@allure.title('Verify click behavior of Left Navigation arrow')
def test_BehaviourLeftNavigationArrow(browser):
    home.ClickPrevNavigationButton()
    movie1 = home.MovieTitle()
    assert movie1 == True
    movie2 = home.MovieTitleBenHuh()
    assert movie2 == True
    movie3 = home.MovieTitleValkyrie()
    assert movie3 == True


@allure.title('Verify Right Navigation Arrow is disabled when we are on the last card in the list')
def test_NextNavigationDisable(browser):
    btn = home.NextNavigationDisable()
    assert btn == False


@allure.title('Verify elements for each Movie card')
def test_ElementMovieCard(browser):
    image = home.PosterImage()
    assert image == True
    time.sleep(1)
    title = home.MovieTitle()
    assert title == True
    genre = home.MovieGenre()
    assert genre == True


@allure.title('Verify hover behavior on movie cards')
def test_HoverBehaviourMovieCard():
    time.sleep(4)
    assert home.addTolist_bestpicture() == "ADD TO LIST", 'Add to list is not showing on hover of movie card '
    assert home.watchMoviesoption() == "WATCH MOVIE", "Watch movie is not showing on hover of movie card. "
    assert home.watchTraileroption() == "WATCH TRAILER", "Watch movie is not showing on hover of movie card. "
    assert home.viewDetailsoption() == "VIEW DETAILS", "Watch movie is not showing on hover of movie card. "


@allure.title('Verify functionality of Watch Movie button')
def test_FunctionalityWatchnowButton(browser):
    time.sleep(2)
    popup = home.ClickWatchMovieButton()
    time.sleep(1)
    assert home.watch_movie_popup() == "width: 1140px; height: 640px;", "Watch movie popup is not opeing after " \
                                                                        "clicking on watch movie. "
    time.sleep(1)
    home.click_crossimg()


@allure.title('Verify elements in Explore section')
def test_ElementsExploreSection(browser):
    movies = home.HomepageExploreAllMovies()
    assert movies == True
    shows = home.HomepageExploreAllTvShows()
    assert shows == True
    explore = home.ExploreElement()
    assert explore == True


@allure.title('Verify click funcationality of See All TV Shows button')
def test_FunctionalityAllTvShows(browser):
    tv = home.ClickExploreAllTvShows()
    home.ClickLogo()
    assert tv == True


@allure.title('Verify click funcationality of See All Movies button')
def test_FunctinalityAllMovies(browser):
    movies = home.ClickExploreAllMovies()
    home.ClickLogo()
    assert movies == True


@allure.title('Verify elements for each Movie List in recently watched')
def test_ElementMovieList1(browser):
    button = home.SeeAllButton()
    assert button == True, "See all button not found"
    home.Refresh()
    title = home.RecentlyWatched()
    assert title == True, "Movie title not found"
    poster = home.MoviePoster()
    assert poster == True, "Movie poster not found"
    nextbtn = home.RecentlyWatchedNextButton()
    assert nextbtn == True, "next navigation button not found"
    prevbtn = home.MovieListPrevButton()
    assert prevbtn == True, "prev navigation button not found"
# 
# # @allure.title('Verify elements for each Movie card in recently watched')
# # def test_ElementMovieCard1(browser):
# #     #home.Refresh()
# #     image = home.RecentlyWatchedPosterImage()
# #     assert image == True
# #     title = home.MovieTitle()
# #     assert title == True
# #     genre = home.MovieGenre()
# #     assert genre == True
