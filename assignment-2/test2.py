import unittest
import urllib.request

class WebsiteTest(unittest.TestCase):
    def test_website_loading(self):
        url = "http://hello-world-496529738.ap-northeast-3.elb.amazonaws.com/"  # Updated URL

        # Step 1: Send a request to the website
        print("Sending request to", url)
        response = urllib.request.urlopen(url)

        # Step 2: Check the HTTP status code
        print("Checking HTTP status code...")
        status_code = response.getcode()
        self.assertEqual(status_code, 200, "Website failed to load. Status code: {}".format(status_code))

        # Step 3: Check if the website content is not empty
        print("Checking website content...")
        content = response.read()
        self.assertTrue(content, "Website content is empty.")

        # Step 4: Print the website title
        print("Website loaded successfully!")
        try:
            title = content.decode('utf-8').split('<title>')[1].split('</title>')[0]
        except IndexError:
            title = "Title not found"
        print("Website Title:", title)

if __name__ == '__main__':
    unittest.main()
