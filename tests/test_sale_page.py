
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_header_title('Products')
