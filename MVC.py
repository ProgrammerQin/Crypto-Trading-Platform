################################################################################
# Model-View-Controller pattern for user interaction
#
# Purpose: The core application functionality is carried out using the MVC
# pattern, with a view for user interface (console), a model for database
# access, and controller for communication between view and model as well as
# business logic (in this case, report generation).  See the MVC pattern:
# https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller.
#
# Author: Qin Yang
# Contact: yangq90@mcmaster.ca
#
################################################################################

# View is responsible for user interface... i.e. presenting options to the user
# and collecting user input.
#
# Each method represents a different option page.
# We use decorator @staticmethod because the methods will access no object
# instance variables.

from time import time
from datetime import datetime
from report import *
from APP import *
from CoinAPI_for_database import *


class View():

    @staticmethod
    def currency_selection():
        print("****************************************")
        print("Please Select a Currency Type")
        print("We have 'BTC' and 'ETH")
        currency_type = input("Type either 'BTC' or 'ETH' for your selection")
        return currency_type

    @staticmethod
    def currency_amount():
        print("****************************************")
        print("Please Insert a Currency Amount in CAD")
        currency_amount = input("Enter number to select an option: ")
        return int(currency_amount)

    @staticmethod
    def holding_time_selection():
        print("****************************************")
        print("How long do we want to hold this currency?")
        print("(1) Daily")
        print("(2) Weekly")
        print("(3) Monthly")
        holding_time_option = input("Enter number 1 , 2 or 3 to select an option: ")
        return int(holding_time_option)

    @staticmethod
    def view_graph():
        print("****************************************")
        print("Do you want to view graph")
        print("(0) NO ")
        print("(1) YES")
        view_graph_option = input("Enter number to select an option: ")
        return int(view_graph_option)

    @staticmethod
    def read_news():
        print("****************************************")
        print("Do you want to read news?")
        print("(0) NO ")
        print("(1) YES")
        read_news_option = input("Enter number to select an option: ")
        return int(read_news_option)

# Controller uses the view object to present the UI to the user, and manipulates
# data in the database using the model.  The controller also handles business
# logic such as creating the decorator pattern objects necessary to write the
# report to a file.
class Controller():

    # Controller initialized with a view and model object
    def __init__(self,view, model):
        self.__view = view
        self.__model = model

    # Have the view present main page with options to gather user information
    def run(self):
        currency_type = self.__view.currency_selection()
        currency_amount = self.__view.currency_amount()
        holding_time_option = self.__view.holding_time_selection()
        view_graph_option = self.__view.view_graph()
        read_news_option = self.__view.read_news()

        if view_graph_option == 1:
           self.__view_graph(currency_type, currency_amount, holding_time_option)

        if read_news_option == 1:
           self.__read_news(currency_type, holding_time_option)


    # Create a graph and let user view it
    def __view_graph(self, currency_type, currency_amount, holding_time_option):
        self.__model.create_graph(self, currency_type,currency_amount,holding_time_option)


    # Search news and present it to user:
    def __read_news(self, currency_type, holding_time_option):
        self.__model.create_news_report(self, currency_type, holding_time_option)

        # Measure time to create and print the report.... record start time
        start_time = time()

        # create the report by creating the base report, and then decorating it
        source_id, title_search_terms= \
            self.__model.create_news_report(self, currency_type, holding_time_option)
        report = ReportBase(currency_type)

        if (len(title_search_terms) != 0):
            title_search_terms_list = title_search_terms.split(",")
            for search_term in title_search_terms_list:
                report = ReportTitleSearch(currency_type, holding_time_option)

        # output the report
        output_file = open(output_filename, "w")
        output_file.write(report.report_text())
        output_file.close()

        # Measure time to create and print the report using the end time
        end_time = time()
        total_time = round(end_time - start_time, 4)

# Model handles interaction with the database, used by the controller
class Model():

    # Create coin graph based on user coin and time selection
    def create_graph(self, currency_type,currency_amount,holding_time_option):
        if currency_type == BTC:
            data = get_BTC_price_json(self)
            table = dynamodb.table('BTC_Trading_Graph')

        if currency_type == ETH:
            data = get_ETH_price_json(self)
            table = dynamodb.table('ETH_Trading_Graph')


        print("Use",currency_amount, holding_time_option, "to draw graph on database" )
        print(table.creation_date_time)

    # Generate news report and call API
    def create_news_report(self, currency_type, holding_time_option):
        # get topic keyword and data keyword ready for searches

        title_search = currency_type

        # This is to get date and time information ready for time keyword
        # Time keyword will be based on currency trading time
        if holding_time_option = 1:
            yesterday = today - timedelta(days=1)
            time_search = datetime.date(yesterday)

        elif holding_time_opinion = 2:
            one_week_ago = today - timedelta(days=7)
            time_search = datatime.data(one_week_ago)

        else holding_time_opinion = 2:
            thirty_days_ago = today - timedelta(days=30)
            time_search = datetime.date(thirty_days_ago)

        return time_search, title_search

