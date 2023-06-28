import unittest
import urllib.request

class WebsiteTest(unittest.TestCase):
    def test_website_loading(self):
        url = "https://atg.world" 

        print("Sending request to" , url)
        response = urllib.request.urlopen(url)

        print("checking HTTP status code...")
        status_code = response.getcode()
        self.assertEqual(status_code, 200, "Website failed to load. Status code: {}".format(status_code))


        print("checking website content...")
        content = response.read()
        self.assertTrue(content, "Website content is empty.")


        print("Website loaded successfully!")
        title = content.decode('utf-8').split('<title>')[1].split('</title>')[0]
        print("Website Title:" , title)

if __name__ == '__main__':
    unittest.main()


