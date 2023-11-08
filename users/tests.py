from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        """
        Set up the test environment.

        This function initializes the test environment by creating an instance of the APIClient class and a test user.
        The APIClient instance is assigned to the 'client' attribute, and the test user is assigned to the 'user' attribute.

        Parameters:
            self (object): The current instance of the TestCase class.

        Returns:
            None
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_list_users(self):
        """
        Test the functionality of listing users.

        The `test_list_users` function sends a GET request to the `user-list` endpoint and asserts that the response status code is 200 (OK).

        Parameters:
            self (TestClass): The instance of the test class.

        Returns:
            None
        """
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Test the creation of a new user.

        This function sends a POST request to the 'user-list' endpoint with the provided
        user data. It then asserts that the response status code is 201 (HTTP_CREATED),
        indicating that the user was successfully created. Additionally, it checks that
        the total number of User objects has increased by 1 and that the username of the
        last User object is equal to the provided username.

        Parameters:
        - self: The test case instance.

        Returns:
        - None
        """
        url = reverse('user-list')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().username, 'newuser')

    def test_retrieve_user(self):
        """
        Test the retrieval of a specific user.

        This function sends a GET request to the API endpoint for retrieving a specific user. It constructs the URL using the reverse() function and passes in the user's primary key as a URL parameter. The response is then checked to ensure it has a status code of 200 (OK) and that the username in the response data matches the username of the user object.

        Parameters:
        - self: The test case instance.

        Returns:
        None
        """
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        """
        Test the update user functionality.

        This function tests the update user functionality by sending a PATCH request to the 'user-detail'
        endpoint with updated user data. It then asserts that the response status code is 200 (OK) and
        checks that the user's username in the database has been successfully updated.

        Parameters:
            self (TestCase): The test case instance.

        Returns:
            None
        """
        url = reverse('user-detail', args=[self.user.pk])
        data = {'username': 'updateduser'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=self.user.pk).username, 'updateduser')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)