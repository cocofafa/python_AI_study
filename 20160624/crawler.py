import pandas as pd

class CafeCrawler:
    """
    네이버 카페 게슬 정보 크롤러

    객체 생성시 HTML source 의 경로를 지정해주면
    해당 파일을 기반으로 self.df 변수에 Dataframe 이 저장된다.
    """

    def __init__(self,path):
        f= open(path, 'r', encoding="UTF-8")
        self.source=f.read()
        self.df = pd.Dataframe()

    def generate_dataframe(self):
        self._split_number()
        self._split_title()
        self._split_writer()
        self._split_date()
        self._split_view()
        self._split_like()

        self.df.set_index('게시글번호', inplace=True)

        return self.df

from crawler import CafeCrawler

crawler = CafeCrawler(path='html_source.txt')
print(crawler.generate_dataframe())