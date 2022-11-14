'''
Creates a XML file with:

-> Info about data quality
-> Stock to buy weekly deppending on the month
'''
import stock_ingredientes_semanal as stock
import xml.etree.ElementTree as ET

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def get_data_report_str(file_name: str) -> str:
    
    with open(file_name, 'r', encoding='utf_8') as file:
        s = ''
        for line in file:
            s += line
    
    return s

def weekly_dicts_all_months() -> dict:

    d = {}
    pizzas, orders = stock.extract()
    
    for i in range(len(MONTHS)):
        optimized_ingredients = stock.transform(pizzas, orders, time_stamp=(i+1))
        d[MONTHS[i]] = optimized_ingredients

    return d

def _get_dict_stock_as_str_(weekly_dict: dict) -> str:

    s = ''

    for key in weekly_dict:
        s += f'{key}: {weekly_dict[key]},'
    
    return s[:-1]

def mavens_xml(file_name: str, report: str, stock_by_month: dict) -> None:
    root = ET.Element("Mavens_Report")

    analysis = ET.Element('Data_Analysis')
    root.append(analysis)

    evaluation = ET.SubElement(analysis, 'Evaluation')
    evaluation.text = report

    stock = ET.Element('Weekly_stock')
    root.append(stock)

    for month in MONTHS:
        m = ET.SubElement(stock, month)
        m.text = _get_dict_stock_as_str_(stock_by_month[month])

    tree = ET.ElementTree(root)
      
    with open(file_name, 'w', encoding='utf_8') as file:
        tree.write(file_name,encoding='utf_8')




if __name__ == '__main__':

    report_str = get_data_report_str('evaluation_readme.txt')
    stock_by_month = weekly_dicts_all_months()
    mavens_xml('mavens_xml.xml', report_str, stock_by_month)