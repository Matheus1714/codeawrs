from crawler.SolutionProblemCrawler import SolutionProblemCrawler

from utils.enums.EnumBrowserCrawler import EnumBrowserCrawler

if __name__ == '__main__':
    solution_problem_crawler = SolutionProblemCrawler(
        url_login='https://www.codewars.com/users/sign_in',
        url_scrapper='',
        browser=EnumBrowserCrawler.chrome.value
    )
    users = [
        {
            'email':'',
            'password':'',
            'nickname':''
        }
    ]
    solution_problem_crawler.main(users)