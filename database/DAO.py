from database.DB_connect import DBConnect
from model.Retailer import Retailer
from model.TopVendita import TopVendita


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select distinct YEAR(gds.`Date`) as year
                    from go_daily_sales gds"""
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getBrands():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_brand
                    from go_products gp 
                    order by gp.Product_brand """
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row["Product_brand"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from go_retailers gr 
                    order by gr.Retailer_name """
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTopVendite1():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """select gds.`Date`, (gds.Unit_sale_price*gds.Quantity) as Ricavo, gds.Retailer_code, gds.Product_number
                    from go_daily_sales gds, go_retailers gr, go_products gp 
                    where gds.Retailer_code=gr.Retailer_code 
                    and gp.Product_number=gds.Product_number
                    order by ricavo desc 
                    limit 5"""
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(TopVendita(row["Date"], row["Ricavo"], row["Retailer_code"], row["Product_number"]))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    print(DAO.getAnni())
    print(DAO.getRetailers())
    print(DAO.getBrands())
    print(DAO.getTopVendite1())

