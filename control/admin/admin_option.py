def admin_dashboard_option():
    print("""
0. LOG OUT
1. PRODUCT LIST
2. CUSTOMER LIST
3. SALES RECORD
          """)
    
def product_list_option():
    print("""
0. Main menu
1. Add Product
2. Update Product
3. Delete Product
4. Sort Product
5. Filter Product
          """)
    
    
def filter_search_option():
    print("""
0. Back
1. Filter by Name
2. Filter by Price 
          """)

def sort_by_option():
    print("""
0. Back
1. Sort By Stock
2. Sort By Price
          """)

def pagination_option( page, current_page, total_page):
        if page == 0 and total_page > 1 :
                print("""
0. Back
1. First Page       4. Descending
2. Last Page        5. Next Page
3. Ascending        
""")
        elif page == 0 and total_page == 1:
                print("""
0. Back
1. First Page       4. Descending
2. Last Page      
3. Ascending      

""")
        elif current_page < total_page : 
                print("""
0. Back
1. First Page       4. Descending
2. Last Page        5. Next Page
3. Ascending        6. Prev Page
""")
        else :
                print("""
0. Back
1. First Page       4. Descending
2. Last Page      
3. Ascending        6. Prev Page
""")
         