import stock_ingredientes_semanal as stock
import pandas as pd

def ingredientes_excel_sheet(ingredients_dict: dict[dict], excel: pd.ExcelWriter) -> None:
    
    df = pd.DataFrame(ingredients_dict)
    df.to_excel(excel,sheet_name='Weekly ingredients')

def monthly_sold_pizzas_and_profit_excel_sheets(pizzas: list[stock.Pizza], orders: list[stock.Order], excel: pd.ExcelWriter) -> None:

    d = {month: {pizza.id: 0 for pizza in pizzas} for month in stock.MONTHS}
    
    # Monthly sold pizzas
    for order in orders:
        for c in order.command:
            d[stock.MONTHS[order.get_month()-1]][c] += order.command[c] 
    df = pd.DataFrame(d)
    df.to_excel(excel, sheet_name='Pizzas sold monthly')

    # Monthly profit
    d['TOTAL'] = {}
    t_list = [0 for i in range(len(stock.MONTHS))]
    for pizza in pizzas:
        t = 0
        i = 0
        for month in stock.MONTHS:
            d[month][pizza.id] *= pizza.price
            p = d[month][pizza.id]
            t += p
            t_list[i] += p
            i += 1
        d['TOTAL'][pizza.id] = t
    
    for j in range(len(stock.MONTHS)):
        d[stock.MONTHS[j]]['TOTAL'] = t_list[j]
    d['TOTAL']['TOTAL'] = sum(t_list)
    df = pd.DataFrame(d)
    df.to_excel(excel, sheet_name='Monthly profit')

def create_mavens_excel_report():

    pizzas, orders = stock.extract()
    ingredients_dict = stock.weekly_dicts_all_months(pizzas, orders)
    
    print('\n·Creating MAVENS report...')
    excel = pd.ExcelWriter('mavens_report.xls')
    ingredientes_excel_sheet(ingredients_dict, excel)
    monthly_sold_pizzas_and_profit_excel_sheets(pizzas, orders, excel)
    excel.close()
    print('<DONE>')
    

if __name__ == '__main__':

    create_mavens_excel_report()
    



