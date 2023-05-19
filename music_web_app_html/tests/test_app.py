from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
When we visit /albums,
we see all the album records in the database
"""

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    heading_tag = page.locator('h1')
    div_tags = page.locator('div')
    expect(heading_tag).to_have_text('Albums')
    expect(div_tags).to_have_text([
        "Title: DoolittleReleased: 1989",
        "Title: Surfer RosaReleased: 1988",
        "Title: WaterlooReleased: 1974",
        "Title: Super TrouperReleased: 1980",
        "Title: BossanovaReleased: 1990",
        "Title: LoverReleased: 2019",
        "Title: FolkloreReleased: 2020",
        "Title: I Put a Spell on YouReleased: 1965",
        "Title: BaltimoreReleased: 1978",
        "Title: Here Comes the SunReleased: 1971",
        "Title: Fodder on My WingsReleased: 1982",
        "Title: Ring RingReleased: 1973"
    ])

"""
When I visit albums/1 or whichever number I please (so long as it's in range with the number of albums I have),
I get the album title, release year, and artist.
"""

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    heading_tag = page.locator('h1')
    expect(heading_tag).to_have_text('Doolittle')

def test_get_single_album_2(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/2")
    heading_tag = page.locator('h1')
    expect(heading_tag).to_have_text('Surfer Rosa')
    p_tags = page.locator('p')
    expect(p_tags).to_have_text('Release year: 1988\nArtist: Pixies')

def test_get_single_album_3(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/3")
    heading_tag = page.locator('h1')
    expect(heading_tag).to_have_text('Waterloo')
    p_tags = page.locator('p')
    expect(p_tags).to_have_text('Release year: 1974\nArtist: ABBA')

def test_album_links(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    link_to_album = page.get_by_role("link", name='Doolittle')
    expect(link_to_album).to_have_attribute('href', '/albums/1')
    #link_to_album.click()