from bok_choy.page_object import PageObject
import re

class GitHubSearchPage(PageObject):
    url = 'http://www.github.com/search'
    def is_browser_on_page(self):
        #return 'code search' in self.browser.title.lower()
        return self.q(css='button.btn').is_present()

    def enter_search_terms(self,text):
        self.q(css='#search_form input[type="text"]').fill(text)

    def search(self):
        self.q(css='button.btn').click()
        GitHubSearchResultsPage(self.browser).wait_for_page()

    def search_for_terms(self,text):
        self.enter_search_terms(text)
        self.search()


class GitHubSearchResultsPage(PageObject):
    """
    GitHub's search results page
    """
    # You do not navigate to this page directly
    url = None
    def is_browser_on_page(self):
        url = None
        # This should be something like: u'Search "foo bar" GitHub'
        title = self.browser.title
        matches = re.match(u'^Search .+ GitHub$', title)
        return matches is not None

    @property
    def search_results(self):
        return self.q(css='ul.repo-list > div > div > h3 > a').text


