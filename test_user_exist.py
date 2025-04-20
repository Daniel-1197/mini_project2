import pytest
from pages.user_exist import ExistingUserPage

@pytest.mark.usefixtures("setup")

def test_existuser(login):
    driver = login
    exist_user_page = ExistingUserPage(driver)

    try:
        exist_user_page.navigate_to_admin_menu()
        exist_user_page.wait_for_system_users_page()
        exist_user_page.search_user("TestUser04")

        assert exist_user_page.verify_user_in_list("TestUser04"), "User 'TestUser04' not found in the search results."
        print("New user 'TestUser04' successfully found in the user list.")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")






