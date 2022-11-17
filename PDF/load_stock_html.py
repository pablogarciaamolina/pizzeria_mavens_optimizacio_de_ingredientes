from load_stock_xml import get_data_report_str, weekly_dicts_all_months, _get_dict_stock_as_str_
from xhtml2pdf import pisa

def mavens_html(file_name: str, report: str, stock_by_month: dict[str, dict], retorno=False) -> str or None:
    print('·Creating html file...')
    html_str = ''
    html_str += '<!DOCTYPE html>'
    html_str += '<html>'

    #HEAD
    html_str += '<head>'
    html_str += '<title>' + 'Mavens Report' + '</title>'
    html_str += '</head>'

    #BODY
    html_str += '<body>'
    html_str += '<h1>' + 'Evaluation' + '</h1>'
    html_str += '<p>'
    html_str += report
    html_str += '</p>'
    html_str += '<h2>' + 'Weekly stock by month' + '</h1>'
    html_str += '<p>'
    for month in stock_by_month:
        html_str += '<br><br>' + month.upper() + '<br>\n'
        html_str += _get_dict_stock_as_str_(stock_by_month[month])
    html_str += '</p>'
    html_str += '</body>'

    html_str += '</html>'

    with open('mavens_html.html', 'w', encoding='utf_8') as file:
        file.write(html_str)

    print('<DONE>')

    if retorno: return html_str

def create_html():
    report_str = get_data_report_str('evaluation_readme.txt')
    stock_by_month = weekly_dicts_all_months()
    mavens_html('mavens_html.html', report_str, stock_by_month)
    
def create_pdf_from_html():

    report_str = get_data_report_str('evaluation_readme.txt')
    stock_by_month = weekly_dicts_all_months()
    html_str = mavens_html('mavens_html.html', report_str, stock_by_month, retorno=True)

    print('Creating PDF...')
    #Transform HTML
    out_file = open('mavens_pdf.pdf', 'w+b')
    p = pisa.CreatePDF(html_str, out_file)
    out_file.close()
    print('<DONE>')

if __name__ == '__main__':

    create_pdf_from_html()