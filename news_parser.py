from patterns.template_method.parsers import GoogleParser, YahooParser

if __name__ == '__main__':
    google = GoogleParser()
    yahoo = YahooParser()

    print('Google: \n', google.print_top_new())
    print('Yahoo: \n', yahoo.print_top_new())
