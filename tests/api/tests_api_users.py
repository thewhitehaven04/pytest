import pytest
from client.reqres import Reqres
from validation.user_model import EmptyModel, UserListResponse, UserResponse


class TestApiUsers:

    @pytest.mark.parametrize(argnames="value,expected_value",
                             argvalues=[(10, 10), (10, 12)])
    def test_user_id(self, value, expected_value):
        user = UserResponse(**Reqres().get_user(value).get_json())
        assert user.data.id == expected_value

    def test_userlist(self):
        page = 3
        userlist = UserListResponse(**Reqres().get_users(params={
            "page": page
        }).get_json())
        assert userlist.page == page

    def test_user_notfound(self):
        user_response = EmptyModel(**Reqres().get_user(23).get_json())
